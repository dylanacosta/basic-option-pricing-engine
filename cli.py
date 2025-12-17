# prompts, parsing, validation, table output

DEFAULT_RISK_FREE_RATE = 0.04  # 4%
DEFAULT_VOLATILITY_PERIOD_DAYS = 30  # 30 days

def call_or_put_from_user():
    while True:
        user_input = input("Enter 'c' for call or 'p' for put: ")
        if user_input.lower() == "c":
            return "call"
        elif user_input.lower() == "p":
            return "put"
        else:
            print("Invalid input. Please enter 'c' for call or 'p' for put.")

def _parse_rate_input(raw_value):
    """Convert a user string (decimal or percent) to a float."""
    cleaned = raw_value.strip()
    if not cleaned:
        raise ValueError("Empty value")
    if cleaned.endswith("%"):
        cleaned = cleaned[:-1].strip()
        return float(cleaned) / 100
    return float(cleaned)

def get_ticker_from_user():
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ").upper()
    return ticker

def get_strike():
    while True:
        try:
            strike = float(input("Enter the strike price: "))
            return strike
        except ValueError:
            print("Invalid input. Please enter a numeric value for the strike price.")

def get_expiration_times():
    while True:
        try:
            expirations = input("Enter expiration times in days (comma-separated, e.g., 30,60,90): ")
            expiration_list = [int(x.strip()) for x in expirations.split(",")]
            return expiration_list
        except ValueError:
            print("Invalid input. Please enter numeric values for expiration times.")


def get_risk_free_rate_from_user(default_rate=DEFAULT_RISK_FREE_RATE):
    prompt = (
        "Enter the risk-free interest rate as a decimal (0.05) or percent (5%).\n"
        f"Press Enter to use the default {default_rate:.2%}: "
    )
    while True:
        user_input = input(prompt)
        if not user_input.strip():
            return default_rate
        try:
            return _parse_rate_input(user_input)
        except ValueError:
            print("Invalid input. Please enter a number like 0.05 or 5%.")


def get_volatility_period_from_user(default_period=DEFAULT_VOLATILITY_PERIOD_DAYS):
    """Get the historical volatility period in days from the user."""
    prompt = (
        f"Enter the historical volatility period in days (e.g., 30, 60, 90, 252).\n"
        f"Press Enter to use the default {DEFAULT_VOLATILITY_PERIOD_DAYS} days: "
    )
    while True:
        user_input = input(prompt)
        if not user_input.strip():
            return DEFAULT_VOLATILITY_PERIOD_DAYS
        try:
            period = int(user_input.strip())
            if period <= 0:
                raise ValueError("Period must be positive")
            return period
        except ValueError:
            print("Invalid input. Please enter a positive integer for the period in days.")
 