import pandas as pd

def run_backtest(df: pd.DataFrame, initial_capital: float = 10000.0, trade_fee_pct: float = 0.001) -> pd.DataFrame:
    """
    Simulates portfolio value over time, accounting for trading fees/slippage.
    trade_fee_pct of 0.001 represents a 0.1% cost per trade.
    """
    print("Running backtest with real-life friction...")
    
    # Daily market return
    df['Market_Return'] = df['Close'].pct_change()
    
    # Strategy return: We shift the signal by 1 day. 
    # If a signal triggers today at close, we earn the return starting tomorrow.
    df['Strategy_Return'] = df['Market_Return'] * df['Signal'].shift(1)
    
    # Apply friction: Subtract trading fees every time our position changes
    # abs() is used because both buying (1) and selling (-1) incur fees
    df['Trading_Fees'] = df['Position_Change'].abs() * trade_fee_pct
    df['Strategy_Return'] -= df['Trading_Fees'].fillna(0)
    
    # Calculate cumulative portfolio value (Equity Curve)
    df['Equity_Curve'] = initial_capital * (1 + df['Strategy_Return']).cumprod()
    
    # Calculate a Buy & Hold equity curve for benchmark comparison
    df['Buy_Hold_Curve'] = initial_capital * (1 + df['Market_Return']).cumprod()
    
    # Strategy daily returns
    df["Strategy_Returns"] = df["Equity_Curve"].pct_change()

    # Benchmark daily returns
    df["Benchmark_Returns"] = df["Buy_Hold_Curve"].pct_change()
        
    # Strategy returns
    df["Strategy_Returns"] = df["Equity_Curve"].pct_change()

    # Benchmark returns
    df["Benchmark_Returns"] = df["Buy_Hold_Curve"].pct_change()

    # Running peak
    df["Equity_Peak"] = df["Equity_Curve"].cummax()

    # Drawdown
    df["Drawdown"] = (df["Equity_Curve"] - df["Equity_Peak"]) / df["Equity_Peak"]

    # Risk metrics
    max_drawdown = df["Drawdown"].min()
    volatility = df["Strategy_Returns"].std() * (252 ** 0.5)
    sharpe = (df["Strategy_Returns"].mean() / df["Strategy_Returns"].std()) * (252 ** 0.5)

    print("\n--- Risk Metrics ---")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")
    print(f"Annual Volatility: {volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")

    return df
