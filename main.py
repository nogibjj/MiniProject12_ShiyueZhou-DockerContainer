from flask import Flask, jsonify
import pandas as pd
from mylib.extract import get_current_price

app = Flask(__name__)


# Route for a simple "Hello, world!" response
@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/graddata")
def show_data():
    # Load the data
    df = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/grad-students.csv"
    )
    
    # Query: Calculate the average 'Grad_unemployment_rate' by 'Major_category'
    average_grad_unemployment = (
        df.groupby("Major_category")["Grad_unemployment_rate"]
        .mean()
        .reset_index()
        .rename(columns={"Grad_unemployment_rate": "Average_Grad_Unemployment_Rate"})
    )
    
    # Convert both DataFrames to HTML
    df_html = df.head(5).to_html(index=False)
    avg_html = average_grad_unemployment.to_html(index=False)
    
    # Combine the HTML
    combined_html = f"""
    <h1>Original Data (First 5 Rows)</h1>
    {df_html}
    <h1>Average Grad Unemployment Rate by Major Category</h1>
    {avg_html}
    """
    
    # Return the combined HTML
    return combined_html


@app.route("/stockprice/<ticker>", methods=["GET"])
def stock_price(ticker):
    """
    Get the current stock price for a given ticker and return as an HTML table.

    URL format: /stockprice/<ticker>
    Example: /stockprice/UBS
    """
    # Fetch the stock price information
    ticker = ticker.upper()
    dist = get_current_price(ticker)

    if not dist:
        return f"<h1>Data for ticker '{ticker}' is not available.</h1>", 404

    # Create an HTML table dynamically
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stock Price for {dist['ticker']}</title>
        <style>
            table {{
                width: 50%;
                margin: 20px auto;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: center;
            }}
            h1 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>Stock Price for {dist['ticker']}</h1>
        <table>
            <tr>
                <th>Ticker</th>
                <th>Date/Time</th>
                <th>Stock Price</th>
            </tr>
            <tr>
                <td>{dist['ticker']}</td>
                <td>{dist['date_time']}</td>
                <td>${dist['price']:.2f}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html
    

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)