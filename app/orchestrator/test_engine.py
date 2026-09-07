from app.orchestrator.engine import MrShopOrchestrator


orchestrator = MrShopOrchestrator()


messages = [
    "I have a blue blazer. How should I style it?",
    "Actually, show me something white under 2000.",
    "Can I speak with someone who can help me choose colours?"
]


for message in messages:

    result = orchestrator.process_message(message)

    print("\nUSER:")
    print(message)

    print("\nSYSTEM:")
    print(result["response"])

    print("\nIntent:", result["intent"])
    print("Method:", result["classification_method"])
    print("Confidence:", result["confidence"])
    print("Entities:", result["entities"])

    print("\nContext:")
    print(result["context"])

    print("=" * 70)