"""
Test goes here

"""
from mylib.extract import extract
from mylib.query import query
import os
from databricks import sql
from dotenv import load_dotenv

def test_extract():
    # Test the extract function
    result = extract()
    assert result is not None, "Extract function failed"
    print("Extract test passed.")
    
def test_transform():
    # Load environment variables for Databricks
    #load_dotenv()
    server_h = os.getenv("SQL_SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP_PATH")
    
    try:
        with sql.connect(
            server_hostname=server_h,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            c = connection.cursor()
            table_name = "Murder2015"
            
            # Check if table exists
            c.execute(f"SHOW TABLES FROM default LIKE '{table_name}'")
            result1 = c.fetchall()
            assert len(result1) > 0, f"Table {table_name} not found"
            
            # Check if there are rows in the table
            c.execute(f"SELECT * FROM {table_name} LIMIT 1")
            result2 = c.fetchall()
            assert len(result2) > 0, f"No rows found in {table_name}"
            
            print("Transform test passed.")
    finally:
        c.close()



def test_query():
    # Test the query function
    result = query()
    assert result is not None, "Query function failed"
    assert len(result) > 0, "Query returned no results"
    print("Query test passed.")


if __name__ == "__main__":
    # Running the tests
    test_extract()
    test_transform()
    test_query()