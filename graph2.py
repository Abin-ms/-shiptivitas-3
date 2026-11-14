
import sqlite3
import matplotlib.pyplot as plt

# Connect to SQLite database
db = sqlite3.connect("shiptivity.db")

# Count actual status changes for each card
query = """
SELECT
    cardID,
    COUNT(*) AS status_changes
FROM card_change_history
WHERE oldStatus IS NOT NULL
  AND oldStatus != newStatus
GROUP BY cardID
ORDER BY cardID;
"""

results = db.execute(query).fetchall()
db.close()

# Prepare graph data
card_ids = [row[0] for row in results]
changes = [row[1] for row in results]

print("Cards with status changes:", len(results))
print("Total status changes:", sum(changes))

# Create bar graph
plt.figure(figsize=(14, 6))
plt.bar(card_ids, changes, width=0.8)

plt.title("Shiptivitas - Number of Status Changes by Card")
plt.xlabel("Card ID")
plt.ylabel("Number of Status Changes")
plt.yticks(range(0, max(changes) + 1))
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()

# Save graph before displaying it
plt.savefig("graph2_card_status_changes.png", dpi=200)

print("Graph 2 saved successfully!")

plt.show()
