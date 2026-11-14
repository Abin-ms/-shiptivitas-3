
import sqlite3

# Connect to the SQLite database
db = sqlite3.connect("shiptivity.db")

# STEP 1: Display database tables and their structure
print("\nDATABASE TABLES")
print("=" * 50)

cursor = db.execute(
    "SELECT name, sql FROM sqlite_master WHERE type = 'table'"
)

for name, schema in cursor.fetchall():
    print(f"\nTABLE: {name}")
    print(schema)


# STEP 2: Read SQL queries from answer.sql
print("\n\nSQL QUERY RESULTS")
print("=" * 50)

with open("answer.sql", "r", encoding="utf-8") as file:
    sql_queries = file.read()

# Split the two SQL statements
queries = [
    query.strip()
    for query in sql_queries.split(";")
    if query.strip()
]


# STEP 3: Execute each SQL query
for i, query in enumerate(queries, start=1):

    print(f"\nPART {i} RESULTS")
    print("-" * 50)

    cursor = db.execute(query)

    # Skip statements that do not return rows
    if cursor.description is None:
      print("Statement executed (no result rows).")
      continue

    # Display column names
    columns = [column[0] for column in cursor.description]
    print(columns)

    # Display query results
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print(f"\nTotal rows: {len(rows)}")


# STEP 4: Close database connection
db.close()

print("\nAnalysis completed successfully!")
