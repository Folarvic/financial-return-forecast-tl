import pandas as pd
import pandas_ta as ta

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add technical indicators and lagged features."""
    df = df.copy()
    
    # Technical indicators
    df['rsi'] = ta.rsi(df['Close'], length=14)
    macd = ta.macd(df['Close'])
    df['macd'] = macd['MACD_12_26_9']
    bb = ta.bbands(df['Close'])
    df['bb_width'] = (bb['BBU_5_2.0'] - bb['BBL_5_2.0']) / df['Close']
    
    # Lagged returns
    for lag in [1, 3, 5, 10]:
        df[f'ret_lag_{lag}'] = df['log_return'].shift(lag)
    
    return df.dropna()
