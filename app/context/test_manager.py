from manager import ContextManager


context_manager = ContextManager()


# First user message
context_manager.update(
    intent="STYLING_ADVICE",
    entities={
        "color": "blue",
        "item": "blazer"
    },
    message="I have a blue blazer. How should I style it?"
)

print("After first message:")
print(context_manager.get_context())


print("\n" + "=" * 60 + "\n")


# Topic switch
context_manager.update(
    intent="PURCHASE",
    entities={
        "budget": 2000
    },
    message="Actually, show me something under 2000."
)

print("After topic switch:")
print(context_manager.get_context())