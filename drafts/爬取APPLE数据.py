import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Basic settings
# ==============================
ticker = "AAPL"
start_date = "2021-01-01"
end_date = "2026-01-01"  # end date is excluded

# ==============================
# Download Apple price data
# ==============================
apple = yf.Ticker(ticker)

data = apple.history(
    start=start_date,
    end=end_date,
    interval="1d",
    auto_adjust=True
)

# Keep the required columns
data = data[["Open", "High", "Low", "Close", "Volume"]]

print(data.head())
print(data.tail())
print("\nNumber of trading days:", len(data))

# Save the data to a CSV file
data.to_csv("AAPL_2021_2025.csv")

print("Data saved as AAPL_2021_2025.csv")

# Read the data back from the CSV file
data = pd.read_csv(
    "AAPL_2021_2025.csv",
    index_col="Date",
    parse_dates=True
)

# Check for missing values and duplicate dates
print("Missing values:")
print(data.isna().sum())

print("\nDuplicate dates:")
print(data.index.duplicated().sum())

print("\nDate range:")
print(data.index.min(), "to", data.index.max())


