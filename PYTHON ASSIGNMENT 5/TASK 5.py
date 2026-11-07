
def summarise(text):
    sentences = text.split(".")
    summary = sentences[:2]
    return ". ".join(s.strip() for s in summary if s.strip()) + "."

positive_words = ["good", "happy", "excellent", "clean", "helpful"]
negative_words = ["bad", "sad", "dirty", "poor", "slow"]

def sentiment_analysis(text):
    words = text.lower().split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"
def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to AI Assistant."

    elif "air quality" in message:
        return "Air quality monitoring helps us understand pollution."

    elif "thank" in message:
        return "You are welcome!"

    elif "bye" in message:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I do not understand your message."
print("TEXT SUMMARISATION")

text = (
    "Air pollution affects human health. "
    "Clean air is important for everyone. "
    "Trees help improve the environment."
)

print("Original Text:", text)
print("Summary:", summarise(text))
print("\nSENTIMENT ANALYSIS")

reviews = [
    "The environment is clean and good",
    "The area is dirty and bad",
    "The weather is normal"
]

for review in reviews:
    print(review, ":", sentiment_analysis(review))

print("\nAI CHATBOT")

messages = ["Hello", "Tell me about air quality", "Thank you"]

for message in messages:
    print("User:", message)
    print("Bot:", chatbot(message))

print("\nTASK 5 COMPLETED")
