from yahoo_fin import stock_info as si
from datetime import datetime
from typing import Dict

def get_current_price(ticker: str) -> Dict[str, str]:
    """
    Fetches the current stock price for a given ticker and returns it with the date and time.

    Parameters:
    - ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple, "UBS" for UBS Group AG).

    Returns:
    - dict: A dictionary containing the ticker, date/time, and the current stock price.
    """
    try:
        # Get the live price
        price = si.get_live_price(ticker)
        
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Return as a dictionary
        return {
            "ticker": ticker,
            "date_time": current_time,
            "price": round(price, 2),  # Round price to 2 decimal places
        }
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return {
            "ticker": ticker,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "price": None,
        }

if __name__ == "__main__":
    # Example usage
    ticker = "UBS"
    result = get_current_price(ticker)
    print(result)
