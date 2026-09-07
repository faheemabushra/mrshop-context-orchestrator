def classify_intent(message: str):
    """
    Rule-based intent classifier.

    Returns:
        One of the supported intents, or UNKNOWN.
    """

    message = message.lower().strip()

    # --------------------------------------------------
    # WARDROBE UPLOAD
    # --------------------------------------------------

    wardrobe_keywords = [
        "add to my wardrobe",
        "add to wardrobe",
        "add to my closet",
        "add to closet",
        "upload to my wardrobe",
        "upload to wardrobe",
        "save to my wardrobe",
        "save to wardrobe",
        "save this item",
        "store this item"
    ]

    if any(keyword in message for keyword in wardrobe_keywords):
        return "WARDROBE_UPLOAD"


    # --------------------------------------------------
    # BOOKING
    # --------------------------------------------------

    booking_keywords = [
        "book a stylist",
        "book stylist",
        "book a consultation",
        "book consultation",
        "schedule a stylist",
        "schedule consultation",
        "stylist appointment",
        "fashion consultation",
        "colour consultation",
        "color consultation",
        "speak with a stylist",
        "talk to a stylist",
        "fashion expert"
    ]

    if any(keyword in message for keyword in booking_keywords):
        return "BOOKING"


    # --------------------------------------------------
    # PURCHASE
    # --------------------------------------------------

    purchase_keywords = [
        "buy",
        "purchase",
        "shop for",
        "find me",
        "show me",
        "looking for",
        "under 2000",
        "under 3000",
        "under 5000"
    ]

    if any(keyword in message for keyword in purchase_keywords):
        return "PURCHASE"


    # --------------------------------------------------
    # STYLING ADVICE
    # --------------------------------------------------

    styling_keywords = [
        "what should i wear",
        "what can i wear",
        "how should i style",
        "how can i style",
        "what goes well with",
        "what goes with",
        "what can i pair with",
        "how do i pair",
        "suggest an outfit",
        "help me choose an outfit",
        "what would look good"
    ]

    if any(keyword in message for keyword in styling_keywords):
        return "STYLING_ADVICE"


    # --------------------------------------------------
    # No confident rule match
    # --------------------------------------------------

    return "UNKNOWN"