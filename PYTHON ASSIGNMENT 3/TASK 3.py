
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]

print("Word frequencies:", frequencies(calls, STOP))
print("Top 3 words:", top(frequencies(calls, STOP), 3))

# Group complaints by district
complaints = [
    ("Madurai", "Seeds not received"),
    ("Chennai", "Fertiliser price high"),
    ("Madurai", "Water supply problem"),
    ("Salem", "Crop damage")
]

district_data = {}

for district, complaint in complaints:
    district_data.setdefault(district, []).append(complaint)

print("\nComplaints by district:")
for district, items in district_data.items():
    print(district, ":", items)

# Test with empty text and punctuation
print("\nEmpty text:", frequencies([""], STOP))
