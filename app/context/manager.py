class ContextManager:

    def __init__(self):
        self.context = {
            "current_intent": None,
            "previous_intent": None,
            "entities": {},
            "conversation_history": []
        }

    def update(self, intent, entities, message):

        # Store previous intent
        self.context["previous_intent"] = (
            self.context["current_intent"]
        )

        # Update current intent
        self.context["current_intent"] = intent

        # Merge new entities with existing context
        self.context["entities"].update(entities)

        # Store conversation
        self.context["conversation_history"].append({
            "message": message,
            "intent": intent,
            "entities": entities
        })

    def get_context(self):
        return self.context