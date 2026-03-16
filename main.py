from src.data_loader import fetch_data
from src.strategy import apply_ma_crossover
from src.backtester import run_backtest
import matplotlib.pyplot as plt

def main():
    # 1. Define Parameters
    TICKER = "SPY"  # S&P 500 ETF
    START_DATE = "2015-01-01"
    END_DATE = "2023-12-31"
    INITIAL_CAPITAL = 10000.0
    
    # 2. Run Pipeline
    df = fetch_data("SPY", "2015-01-01", "2023-12-31")
    df = apply_ma_crossover(df, short_window=50, long_window=200)
    df = run_backtest(df, initial_capital=INITIAL_CAPITAL, trade_fee_pct=0.001) # 0.1% fee per trade
    
    # 3. Print Summary
    final_portfolio_value = df['Equity_Curve'].iloc[-1]
    buy_and_hold_value = df['Buy_Hold_Curve'].iloc[-1]
    
    print("\n--- Backtest Results ---")
    print(f"Initial Capital: ${INITIAL_CAPITAL:,.2f}")
    print(f"Final Strategy Value: ${final_portfolio_value:,.2f}")
    print(f"Final Buy & Hold Value: ${buy_and_hold_value:,.2f}")
    
    max_drawdown = df["Drawdown"].min()
    print(f"Max Drawdown: {max_drawdown:.2%}")

    # 4. Quick Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Equity_Curve'], label='MA Crossover Strategy', color='blue')
    plt.plot(df.index, df['Buy_Hold_Curve'], label='Buy & Hold (Benchmark)', color='gray', alpha=0.7)
    plt.title(f"Backtest Results for {TICKER}")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('equty_curve.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()