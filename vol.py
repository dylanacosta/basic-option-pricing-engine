# handles volatility calculations; uses date to find historical vol and uses that for implied volatility calculations
import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from scipy.stats import norm
from cli import get_volatility_period_from_user
from cli import get_ticker_from_user

temp = "MSFT"

ticker = yf.Ticker(get_ticker_from_user())

def get_historical_volatility(ticker_symbol, period_days=get_volatility_period_from_user()):
    """Calculate historical volatility for a given ticker symbol over a specified period."""
    # Handle both string ticker symbols and yf.Ticker objects
    if isinstance(ticker_symbol, str):
        ticker = yf.Ticker(ticker_symbol)
    else:
        ticker = ticker_symbol
    
    prices = ticker.history(period=f"{period_days}d")["Close"]
    print(f'{prices}')
    log_returns = np.log(prices / prices.shift(1)).dropna()
    #shifted by 1 to account for NaN in first position
    volatility = log_returns.std() * np.sqrt(252)
    # Annualizing the volatility; assuming 252 trading days in a year
    return volatility


print(get_historical_volatility(temp))
