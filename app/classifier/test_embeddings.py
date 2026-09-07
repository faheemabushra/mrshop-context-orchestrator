from embeddings import SemanticIntentClassifier


classifier = SemanticIntentClassifier()


messages = [
    "I've got a new denim jacket, what goes well with it?",
    "I need something white for my blazer",
    "Can you find me something nice under 2000?",
    "Can I speak with someone who can help me choose colours?",
    "I want to add my new red dress to my wardrobe"
]


for message in messages:

    result = classifier.classify(message)

    print(f"Message: {message}")
    print(f"Intent: {result['intent']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Matched example: {result['matched_example']}")

    print("Top matches:")

    for match in result["top_matches"]:
        print(
        f"  {match['intent']} "
        f"-> {match['score']} "
        f"-> {match['example']}"
    )

    print("-" * 60)