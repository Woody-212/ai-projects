import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# --- Config ---
TICKER = "AAPL"
PERIOD = "6mo"

# --- Fetch Data ---
print(f"Fetching data for {TICKER}...")
stock = yf.download(TICKER, period=PERIOD)

# --- Moving Averages ---
stock["MA20"] = stock["Close"].rolling(window=20).mean()
stock["MA50"] = stock["Close"].rolling(window=50).mean()

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(stock["Close"], label="Close Price", color="blue", linewidth=1.5)
plt.plot(stock["MA20"], label="20-Day MA", color="orange", linewidth=1.2)
plt.plot(stock["MA50"], label="50-Day MA", color="red", linewidth=1.2)

plt.title(f"{TICKER} Stock Price + Moving Averages (Last 6 Months)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("stock_chart.png")
plt.show()
print("Chart saved as stock_chart.png")
