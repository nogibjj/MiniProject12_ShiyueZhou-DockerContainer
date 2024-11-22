from flask import Flask, jsonify, request
import pandas as pd
from mylib.extract import get_current_price

app = Flask(__name__)


# Route for a simple "Hello, world!" response
@app.route("/")
def hello_world():
    return "Hello, world!"


# Route to display the data
@app.route("/graddata")
def show_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/grad-students.csv"
    )
    return df.head(5).to_html()

# Route to display stock price
@app.route("/stockprice/<ticker>", methods=["GET"])
def stock_price(ticker):
    """
    Get the current stock price for a given ticker.

    URL format: /stockprice/<ticker>
    Example: /stockprice/UBS
    """
    # Call get_current_price and return the result as JSON
    dist = get_current_price(ticker)
    return jsonify(dist)
    

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)