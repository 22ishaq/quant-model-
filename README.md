# Quantitative Trading Model: Moving Average Crossover

# by Ishaq Ansary and Adebola Williams Dosunmu 

The aim of our project was to build a modular quantitative trading backtester in Python. It uses the Yahoo Finance API (`yfinance`) to fetch historical market data and evaluates the performance of a Moving Average Crossover strategy against a standard Buy & Hold benchmark.

## File purposes

* **`src/data_loader.py`**: Handles fetching price data from Yahoo Finance.
* **`src/strategy.py`**: Contains the core trading logic such as calculating the 50-day and 200-day Simple Moving Averages and generating Buy/Sell/Hold signals.
* **`src/backtester.py`**: Simulates real-world trading by calculating daily returns, applying a 1-day execution delay to prevent look-ahead bias, and factoring in trading fees/slippage (0.1% per trade).
* **`main.py`**: Generates the performance chart.

## How to Run the Model
1. run python -m pip install -r requirements.txt
2. execute the test python main.py

## Analysis 
The model uses a Golden Cross / Death Cross strategy on the S&P 500 ETF. A buy signal is triggered when the 50 day Short Moving Average crosses above the 200 day Long Moving Average, and a sell signal is generated when its below it. 

![MA Crossover Equity Curve](Figure_1.png)

When you run the model, it generates an Equity Curve (shown above) chart comparing two lines, both starting at an initial capital of $10,000:

The Gray Line (Buy & Hold Benchmark): This represents a passive investment strategy—buying SPY on day one and holding it for the entire duration. It perfectly tracks the natural highs and severe crashes of the broader market.

The Blue Line (MA Crossover Strategy): This represents the active portfolio value driven by the algorithm.

## Key behaviors to observe within the chart:

Cash Preservation (Flatlines): During prolonged bear markets or sudden crashes, like early 2020 due to the disruption with the supply chain causing interest rates to rise, the blue line may go perfectly horizontal. This means the algorithm successfully triggered a "Sell" signal, moved the portfolio into cash, and avoided the market drop.

Whipsawing (The Drawback): In sideways markets, the moving averages may cross frequently. This can result in the algorithm buying and selling rapidly, losing money on minor price drops, and eating into profits due to trading fees.

Absolute Return vs. Risk-Adjusted Return: The active strategy (blue line) may not always end up with a higher final dollar amount than the benchmark (gray line). However, quantitative models are often designed to minimize severe drawdowns (risk) rather than solely maximizing raw profit.

