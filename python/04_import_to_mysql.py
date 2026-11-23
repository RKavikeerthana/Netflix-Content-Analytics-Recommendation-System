
import os
import pandas as pd
import mysql.connector

# Load the cleaned dataset
csv_path = "data/processed/netflix_cleaned.csv"
df = pd.read_csv(csv_path).fillna("Unknown")

# Connect to MySQL (set MYSQL_PASSWORD in your environment; do not hardcode credentials)
if not os.getenv("MYSQL_PASSWORD"):
    raise RuntimeError("Set the MYSQL_PASSWORD environment variable before running this script.")

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE", "netflix_project")
)

cursor = conn.cursor()

# Clear the incomplete import
cursor.execute("TRUNCATE TABLE netflix_titles")

# Insert records in batches
sql = """
INSERT INTO netflix_titles
(show_id, type, title, director, `cast`, country, date_added,
 release_year, rating, duration, listed_in, description)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

df = df.astype(object).where(pd.notna(df), None)
records = [tuple(row) for row in df.itertuples(index=False, name=None)]

for start in range(0, len(records), 500):
    cursor.executemany(sql, records[start:start + 500])
    conn.commit()

print("Records imported:", len(records))

cursor.execute("SELECT COUNT(*) FROM netflix_titles")
print("Records in MySQL:", cursor.fetchone()[0])

cursor.close()
conn.close()
