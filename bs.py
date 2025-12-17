#used for logic in calls and puts 
import yfinance as yf
import numpy as np
from scipy.stats import norm


def black_scholes_call(S, K, T_days, r, sigma):
    """
    Calculate Black-Scholes call option price.
    
    Parameters:
    S: Current stock price
    K: Strike price
    T_days: Time to expiration in days
    r: Risk-free interest rate
    sigma: Volatility (annualized)
    """
    T = T_days / 365.0  # Convert days to years for Black-Scholes formula
    
    if T <= 0:
        return max(S - K, 0)  # Intrinsic value at expiration
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(S, K, T_days, r, sigma):
    """
    Calculate Black-Scholes put option price.
    
    Parameters:
    S: Current stock price
    K: Strike price
    T_days: Time to expiration in days
    r: Risk-free interest rate
    sigma: Volatility (annualized)
    """
    T = T_days / 365.0  # Convert days to years for Black-Scholes formula
    
    if T <= 0:
        return max(K - S, 0)  # Intrinsic value at expiration
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price


def calculate_and_display_prices(ticker_symbol, strike, risk_free_rate, expiration_times, volatility, current_price):
    """
    Calculate and display option prices for all expiration times.
    
    Parameters:
    ticker_symbol: Stock ticker symbol
    strike: Strike price
    risk_free_rate: Risk-free interest rate
    expiration_times: List of expiration times in days
    volatility: Annualized volatility
    current_price: Current stock price
    """
    results = []
    
    # Table width based on column widths
    TABLE_WIDTH = 75
    
    print(f"\n{'='*TABLE_WIDTH}")
    print(f"Option Pricing Results for {ticker_symbol}")
    print(f"{'='*TABLE_WIDTH}")
    print(f"Current Stock Price: ${current_price:.2f}")
    print(f"Strike Price: ${strike:.2f}")
    print(f"Risk-Free Rate: {risk_free_rate:.2%}")
    print(f"Volatility: {volatility:.2%}")
    print(f"{'='*TABLE_WIDTH}\n")
    
    # Header
    print(f"{'Expiration (days)':<20} {'Time to Exp (years)':<25} {'Call Price':<15} {'Put Price':<15}")
    print("-" * TABLE_WIDTH)
    
    # Loop through each expiration time in the list (time is in days)
    # sigma (volatility) is constant across all expiration times
    for days in expiration_times:
        T_years = days / 365.0  # Convert days to years for display
        
        call = black_scholes_call(current_price, strike, days, risk_free_rate, volatility)
        put = black_scholes_put(current_price, strike, days, risk_free_rate, volatility)
        
        results.append({
            'days': days,
            'years': T_years,
            'call': call,
            'put': put
        })
        
        print(f"{days:<20} {T_years:<25.4f} ${call:<14.2f} ${put:<14.2f}")
    
    print(f"\n{'='*TABLE_WIDTH}\n")
    
    return results