# Live-Historical-Stock-Price-Tracker-India

A simple yet powerful **Streamlit web app** to track **live stock prices** and view **historical prices at specific times** during the day — powered by **Yahoo Finance (yfinance)**.

## 🚀 Features

✅ **Live Stock Price Updates** (auto-refresh every 5 seconds)  
✅ **Time-Based Price Lookup** — see the stock price at any specific time (e.g., 3:15 PM)  
✅ **Support for Indian NSE Stocks** like `RELIANCE.NS`, `TCS.NS`, `TATAMOTORS.NS`  
✅ **Clean Streamlit UI** with tabs for Live and Time-based tracking  
✅ **Lightweight & Free to use**


## 🖼️ Demo

*(Add a screenshot or GIF of your Streamlit app here)*

## 🧠 Tech Stack

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yfinance](https://pypi.org/project/yfinance/)
- [pandas](https://pandas.pydata.org/)
- [datetime](https://docs.python.org/3/library/datetime.html)

## 🧩 How It Works

🔴 Live Price Tab

Continuously fetches the latest stock price every few seconds

Displays timestamp of the last update

🕒 Time-based Price Tab

Lets you pick any time (e.g., 15:15)

Fetches the closest available price from today's 1-minute data

