from hybrid import HybridIntentClassifier


classifier = HybridIntentClassifier()


messages = [
    "I've got a new denim jacket, what goes well with it?",
    "I need something white for my blazer",
    "Can you find me something nice under 2000?",
    "Can I speak with someone who can help me choose colours?",
    "I want to add my new red dress to my wardrobe",
    "I want to buy a pair of sneakers"
]


for message in messages:

    result = classifier.classify(message)

    print(f"Message: {message}")
    print(f"Intent: {result['intent']}")
    print(f"Method: {result['method']}")
    print(f"Confidence: {result['confidence']}")

    if "matched_example" in result:
        print(f"Matched example: {result['matched_example']}")

    print("-" * 60)