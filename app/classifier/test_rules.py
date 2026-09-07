from rules import classify_intent


messages = [
    "I've got a new denim jacket, what goes well with it?",
    "I need something white for my blazer",
    "Can you find me something nice under 2000?",
    "Can I speak with someone who can help me choose colours?"
]


for message in messages:
    intent = classify_intent(message)

    print(f"Message: {message}")
    print(f"Intent:  {intent}")
    print("-" * 50)