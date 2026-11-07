
import sqlite3
import time

# AIM: AI Complaint Analysis and Database Indexing

# Step 1: Sentiment analysis dictionaries
POSITIVE = {
    "good", "clean", "fast", "helpful", "improved",
    "excellent", "better", "safe"
}

NEGATIVE = {
    "bad", "dirty", "slow", "rude", "smoke",
    "broken", "poor", "unsafe"
}

NEGATORS = {"not", "never", "no"}


# Step 2: Sentiment scoring function
def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()

    total = 0

    for i, word in enumerate(words):
        value = 0

        if word in POSITIVE:
            value = 1
        elif word in NEGATIVE:
            value = -1

        if i > 0 and words[i - 1] in NEGATORS:
            value = -value

        total += value

    return total


# Step 3: Sentiment classification
def label(text):
    result = score(text)

    if result > 0:
        return "Positive"
    elif result < 0:
        return "Negative"
    else:
        return "Neutral"


# Step 4: Simple text summarisation
def summarise(text):
    sentences = text.split(".")

    return ". ".join(
        sentence.strip()
        for sentence in sentences[:2]
        if sentence.strip()
    ) + "."


# Step 5: Sample complaints
complaints = [
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved.",
    "The environment is excellent.",
    "The road is dirty and unsafe.",
    "Transport service is slow.",
    "The area is clean and safe.",
    "The machine is broken.",
    "The service is good."
]

print("AI COMPLAINT ANALYSIS")
print("---------------------")

for complaint in complaints:
    print(
        label(complaint),
        "|",
        complaint,
        "| Score:",
        score(complaint)
    )


# Step 6: Find a possible misclassification
print("\nMISCLASSIFICATION TEST")

test = "The service is not good."

print("Complaint:", test)
print("Predicted sentiment:", label(test))
print("Expected sentiment: Negative")
print("Note: Simple word-based models may misclassify sentences.")


# Step 7: Text summarisation
print("\nTEXT SUMMARISATION")

report = (
    "Air pollution affects public health. "
    "People reported smoke and dirty roads. "
    "Clean transport can improve the environment."
)

print("Original Report:", report)
print("Summary:", summarise(report))


# Step 8: SQLite database
con = sqlite3.connect("task9.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS complaints")

cur.execute("""
CREATE TABLE complaints (
    id INTEGER PRIMARY KEY,
    complaint TEXT,
    sentiment TEXT
)
""")

records = [
    (i + 1, complaint, label(complaint))
    for i, complaint in enumerate(complaints)
]

cur.executemany(
    "INSERT INTO complaints VALUES (?, ?, ?)",
    records
)

con.commit()

# Step 9: Query before indexing
query = """
SELECT * FROM complaints
WHERE sentiment = 'Negative'
"""

start = time.perf_counter()

for i in range(1000):
    cur.execute(query)
    cur.fetchall()

before_index = time.perf_counter() - start

# Step 10: Create database index
cur.execute("""
CREATE INDEX IF NOT EXISTS sentiment_index
ON complaints(sentiment)
""")

con.commit()

# Step 11: Query after indexing
start = time.perf_counter()

for i in range(1000):
    cur.execute(query)
    cur.fetchall()

after_index = time.perf_counter() - start

print("\nDATABASE INDEXING")
print("Time before index:", round(before_index, 6), "seconds")
print("Time after index:", round(after_index, 6), "seconds")

# Step 12: Display complaint summary
print("\nCOMPLAINT SUMMARY")

cur.execute("""
SELECT sentiment, COUNT(*)
FROM complaints
GROUP BY sentiment
""")

for row in cur.fetchall():
    print(row[0], ":", row[1])

con.close()

print("\nTASK 9 COMPLETED")
