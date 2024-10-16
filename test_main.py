"""
Test goes here

"""

from mylib.extract import extract
from mylib.query import query
import os
from databricks import sql
from dotenv import load_dotenv


def test_extract():
    test = extract()
    return test


def test_transform():
    load_dotenv()
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http_path")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        table_name = "Murder2015"
        c.execute(f"SHOW TABLES FROM default LIKE '{table_name}'")
        result1 = c.fetchall()
        # Check if there are rows in your first table
        c.execute(f"SELECT * FROM {table_name}")
        result2 = c.fetchall()

        c.close()
        
    assert result1 is not None

    assert result2 is not None



def test_query():
    result = query()
    assert result is not None, "Failed to query the database"
    
if __name__ == "__main__":
    # assert test_func()["extract"] == "data/murder_2015_final.csv"
    # assert test_func()["transform"] == "Murder2015.db"
    # assert test_func()["create"] == "Create Success"
    # assert test_func()["read"] == "Read Success"
    # assert test_func()["update"] == "Update Success"
    # assert test_func()["delete"] == "Delete Success"
    test_extract()
    test_transform()
    test_query()


