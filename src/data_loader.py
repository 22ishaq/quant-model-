import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches historical daily price data from Yahoo Finance.
    """
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    
    # Download data
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if df.empty:
        raise ValueError("No data fetched. Check your ticker symbol and dates.")
        
    # Keep only the columns we need for a basic MA strategy
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    # Drop any missing values that might mess up our moving averages
    df.dropna(inplace=True)
    
    return df