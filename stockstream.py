import streamlit as st
import yfinance as yf
from datetime import datetime, date, time as dtime, timedelta

# 🔹 Function to get intraday data for a selected date
def get_intraday_data(symbol, selected_date):
    today = datetime.now().date()
    delta = (today - selected_date).days

    # yfinance only allows 1m interval data for the past 7 days
    if delta > 7:
        return None, "⚠️ 1-minute data available only for the past 7 days."

    ticker = yf.Ticker(symbol)
    data = ticker.history(period="7d", interval="1m")  # fetch 7 days
    if data.empty:
        return None, "❌ No data available for this stock."

    data.index = data.index.tz_localize(None)  # remove timezone
    data = data[data.index.date == selected_date]  # filter only selected date

    if data.empty:
        return None, "⚠️ No trading data for this date (possibly weekend/holiday)."

    return data, None


# 🔹 Function to get price closest to given time
def get_price_at_time(data, target_time):
    data["time"] = data.index.time
    for i in range(len(data) - 1, -1, -1):
        if data["time"].iloc[i] <= target_time:
            return data["Close"].iloc[i], data.index[i]
    return None, None


# 🔹 Streamlit App
st.set_page_config(page_title="Stock Price at Specific Time", layout="centered")
st.title("📅 Live Stock Price (India)")

symbol = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS, TCS.NS, INFY.NS)", "RELIANCE.NS")

# Date & time selectors
selected_date = st.date_input("Select Date", value=datetime.now().date(), max_value=datetime.now().date())
selected_time = st.time_input("Select Time (HH:MM, 24-hour format)", value=dtime(15, 15))

# Fetch button
if st.button("Get Price at Selected Date & Time"):
    with st.spinner("Fetching data..."):
        data, error = get_intraday_data(symbol, selected_date)
        if data is not None:
            price, actual_time = get_price_at_time(data, selected_time)
            if price is not None:
                st.success(f"💹 **{symbol}** at {actual_time.strftime('%Y-%m-%d %H:%M:%S')} was ₹{price:.2f}")
                st.line_chart(data["Close"])
            else:
                st.warning("⚠️ No price data found for that time. Try an earlier time.")
        else:
            st.error(error)
