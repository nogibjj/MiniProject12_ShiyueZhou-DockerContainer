"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_data, read_data, update_data, delete_data

# Extract
print("Extracting data...")
extract()

# # Transform and load
print("Transforming data...")
load()

# # Query
print("Querying data...")
create_data()
read_data()
update_data()
delete_data()
