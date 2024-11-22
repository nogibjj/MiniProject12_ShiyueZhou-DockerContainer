from flask import Flask
import pandas as pd

app = Flask(__name__)


# Route for a simple "Hello, world!" response
@app.route("/")
def hello_world():
    return "Hello, world!"


# Route to display the data
@app.route("/data")
def show_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/grad-students.csv"
    )
    return df.head(5).to_html()


# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)