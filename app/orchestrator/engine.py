from app.classifier.hybrid import HybridIntentClassifier
from app.extractor.entities import extract_entities
from app.context.manager import ContextManager


class MrShopOrchestrator:

    def __init__(self):

        self.classifier = HybridIntentClassifier()
        self.context_manager = ContextManager()

    def process_message(self, message: str):

        # 1. Detect user intent
        classification = self.classifier.classify(message)

        intent = classification["intent"]

        # 2. Extract entities
        entities = extract_entities(message)

        # 3. Update conversation context
        self.context_manager.update(
            intent=intent,
            entities=entities,
            message=message
        )

        # 4. Retrieve current context
        context = self.context_manager.get_context()

        # 5. Generate a simple prototype response
        response = self.generate_response(
            intent,
            entities,
            context
        )

        return {
            "message": message,
            "intent": intent,
            "classification_method": classification["method"],
            "confidence": classification["confidence"],
            "entities": entities,
            "context": context,
            "response": response
        }

    def generate_response(self, intent, entities, context):

        if intent == "STYLING_ADVICE":

            item = entities.get("item", "item")
            color = entities.get("color")

            if color:
                return (
                    f"I can suggest styling options for your "
                    f"{color} {item}."
                )

            return f"I can suggest outfit ideas for your {item}."

        if intent == "PURCHASE":

            budget = entities.get("budget")

            if budget:
                return (
                    f"I can find products within your "
                    f"₹{budget} budget."
                )

            return "I can help you find products to purchase."

        if intent == "WARDROBE_UPLOAD":

            item = entities.get("item", "item")

            return f"I can add your {item} to the wardrobe."

        if intent == "BOOKING":

            return "I can help you arrange a fashion consultation."

        return "I'm not sure what you'd like to do. Could you clarify?"