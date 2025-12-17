# Entry point for the option pricing engine
import yfinance as yf
from cli import (
    get_ticker_from_user,
    get_strike,
    get_risk_free_rate_from_user,
    get_expiration_times, call_or_put_from_user,
    get_volatility_period_from_user,
    DEFAULT_VOLATILITY_PERIOD_DAYS
)
from vol import get_historical_volatility
from bs import calculate_and_display_prices


def main():
    """Main entry point for the option pricing engine."""
    # Get user inputs via CLI
    call_or_put = call_or_put_from_user()
    ticker_symbol = get_ticker_from_user()
    strike = get_strike()
    risk_free_rate = get_risk_free_rate_from_user()
    expiration_times = get_expiration_times()
    volatility_period = get_volatility_period_from_user(DEFAULT_VOLATILITY_PERIOD_DAYS)
    
    # Get stock data and calculate volatility
    underlying = yf.Ticker(ticker_symbol)
    volatility = get_historical_volatility(ticker_symbol, period_days=volatility_period)
    
    # Get current stock price
    current_price = underlying.history(period="1d")["Close"].iloc[-1]
    
    # Calculate and display option prices
    calculate_and_display_prices(
        ticker_symbol=ticker_symbol,
        strike=strike,
        risk_free_rate=risk_free_rate,
        expiration_times=expiration_times,
        volatility=volatility,
        current_price=current_price
    )


if __name__ == "__main__":
    main()
