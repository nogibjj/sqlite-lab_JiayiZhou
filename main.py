"""
ETL-Query script
"""
# fire --command line tool
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
query()
