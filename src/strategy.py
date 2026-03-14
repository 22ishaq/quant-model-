import numpy as np
import pandas as pd

def apply_ma_crossover(df: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.DataFrame:
    """
    Calculates moving averages and generates buy/sell signals.
    """
    print(f"Applying MA Crossover strategy (Short: {short_window}, Long: {long_window})...")
    
    # Calculate Moving Averages
    df['SMA_Short'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window, min_periods=1).mean()
    
    # Create signals: 1.0 if Short MA > Long MA, else 0.0
    df['Signal'] = np.where(df['SMA_Short'] > df['SMA_Long'], 1.0, 0.0)
    
    # Calculate position changes (1 means we just bought, -1 means we just sold)
    df['Position_Change'] = df['Signal'].diff()
    
    return df