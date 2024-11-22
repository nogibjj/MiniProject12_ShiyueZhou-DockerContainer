from flask import Flask, request, render_template_string
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


@app.route("/stockprice", methods=["GET", "POST"])
def stock_price_form():
    """
    Displays a form to enter a stock ticker and shows the stock price information if submitted.
    """
    # Initialize the table as empty
    table_html = ""

    if request.method == "POST":
        # Get the ticker from the form and convert to uppercase
        ticker = request.form.get("ticker").upper()

        # Fetch stock price data
        dist = get_current_price(ticker)

        if dist:
            # Generate the table HTML if data is found
            table_html = f"""
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
            """
        else:
            # Show an error message if the ticker is invalid
            table_html = f"<h2>Data for ticker '{ticker}' is not available.</h2>"

    # Render the final HTML with the form and table (if available)
    return render_template_string(BASE_HTML, table=table_html)
    
BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Price Lookup</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            text-align: center;
        }
        form {
            margin-bottom: 20px;
        }
        table {
            width: 50%;
            margin: 20px auto;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
        h1 {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Enter Stock Ticker</h1>
    <form method="POST">
        <input type="text" name="ticker" placeholder="Enter stock ticker" required>
        <button type="submit">Get Stock Price</button>
    </form>
    <div>
        {% if table %}
            {{ table|safe }}
        {% endif %}
    </div>
</body>
</html>
"""



# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)