import yfinance as yf
import pandas as pd
import numpy as np

def load_and_prepare(ticker: str, start: str, interval: str = "1d"):
    """Download and prepare raw price data."""
    df = yf.download(ticker, start=start, interval=interval, progress=False)
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    return df.dropna()
