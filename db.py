import csv
import sqlite3
import pandas as pd
import duckdb
from rich import print

duckdb.read_csv('jobs2025-09-18.csv')
con = duckdb.connect("job_posts.db")

con.execute("SELECT * FROM jobs")
print(con.fetchall())
