
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to database
db = sqlite3.connect("shiptivity.db")

# Fetch daily active users
query = """
SELECT
    DATE(login_timestamp, 'unixepoch') AS login_date,
    COUNT(DISTINCT user_id) AS daily_active_users
FROM login_history
GROUP BY DATE(login_timestamp, 'unixepoch')
ORDER BY login_date;
"""

rows = db.execute(query).fetchall()
db.close()

dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in rows]
users = [row[1] for row in rows]

release_date = datetime(2018, 6, 2)

# Calculate averages from recorded days
before = [
    count for date, count in zip(dates, users)
    if date < release_date
]

after = [
    count for date, count in zip(dates, users)
    if date >= release_date
]

before_avg = sum(before) / len(before)
after_avg = sum(after) / len(after)

print(f"Before release average DAU: {before_avg:.2f}")
print(f"After release average DAU: {after_avg:.2f}")

# Create graph
plt.figure(figsize=(12, 6))

plt.plot(dates, users, linewidth=1.5, label="Daily Active Users")

plt.axvline(
    release_date,
    linestyle="--",
    linewidth=2,
    label="Kanban Release — June 2, 2018"
)

plt.axhline(
    before_avg,
    linestyle=":",
    label=f"Before Average: {before_avg:.2f}"
)

plt.axhline(
    after_avg,
    linestyle="-.",
    label=f"After Average: {after_avg:.2f}"
)

plt.title("Shiptivitas — Daily Active Users Before and After Kanban Release")
plt.xlabel("Date")
plt.ylabel("Unique Active Users")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()

plt.savefig("graph1_daily_active_users.png", dpi=200)
plt.show()

print("Graph saved as graph1_daily_active_users.png")


