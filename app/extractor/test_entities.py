from entities import extract_entities


messages = [
    "Show me something white under 2000",
    "I have a blue blazer",
    "Find me a red dress below 3000",
    "I want some black sneakers",
    "How should I style my denim jacket?"
]


for message in messages:

    entities = extract_entities(message)

    print(f"Message: {message}")
    print(f"Entities: {entities}")
    print("-" * 60)