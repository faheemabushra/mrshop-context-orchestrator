import re


def extract_entities(message: str):
    """
    Extract lightweight entities from a user message.

    Returns:
        Dictionary containing detected entities.
    """

    message_lower = message.lower()

    entities = {}

    # -------------------------
    # COLOR
    # -------------------------

    colors = [
        "black",
        "white",
        "red",
        "blue",
        "green",
        "yellow",
        "pink",
        "purple",
        "brown",
        "beige",
        "grey",
        "gray"
    ]

    for color in colors:
        if color in message_lower:
            entities["color"] = color
            break

    # -------------------------
    # BUDGET
    # -------------------------

    budget_patterns = [
        r"under\s*[₹rs.]?\s*(\d+)",
        r"below\s*[₹rs.]?\s*(\d+)",
        r"within\s*[₹rs.]?\s*(\d+)",
        r"budget\s*(?:of|is)?\s*[₹rs.]?\s*(\d+)"
    ]

    for pattern in budget_patterns:

        match = re.search(pattern, message_lower)

        if match:
            entities["budget"] = int(match.group(1))
            break

    # -------------------------
    # CLOTHING ITEM
    # -------------------------

    items = [
        "shirt",
        "t-shirt",
        "tshirt",
        "dress",
        "jeans",
        "jacket",
        "blazer",
        "skirt",
        "trousers",
        "pants",
        "shoes",
        "sneakers",
        "heels",
        "top",
        "sweater",
        "hoodie"
    ]

    for item in items:

        if item in message_lower:
            entities["item"] = item
            break

    return entities