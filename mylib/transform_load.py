"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,
avg_FPro_products,avg_distance_root,ingred_normalization_term,
semantic_tree_name,semantic_tree_node
"""

#import sqlite3
import csv
import os
from databricks import sql
from dotenv import load_dotenv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/murder_2015_final.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)

    load_dotenv()
    server_h = os.getenv("SQL_SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:

        # conn = sqlite3.connect("Murder2015.db")
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS Murder2015")
        result = c.fetchall()
        if not result:
            c.execute(
                """CREATE TABLE IF NOT EXISTS  Murder2015(
                    city string, 
                    state_s string, 
                    murders2014 int, 
                    murders2015 int, 
                    change int
                )"""
            )
        # insert
        c.executemany("INSERT INTO Murder2015 VALUES (?, ?, ?, ?, ?)", payload)
        connection.commit()
        connection.close()
        return "Load success"
        #return "success"


if __name__ == "__main__":
    load()
