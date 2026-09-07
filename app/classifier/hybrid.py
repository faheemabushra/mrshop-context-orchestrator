from app.classifier.rules import classify_intent as classify_with_rules
from app.classifier.embeddings import SemanticIntentClassifier

class HybridIntentClassifier:

    def __init__(self):

        # Initialize the semantic classifier
        self.semantic_classifier = SemanticIntentClassifier()


    def classify(self, message: str):

        # ---------------------------------------------
        # STEP 1: Try the rule-based classifier
        # ---------------------------------------------

        rule_intent = classify_with_rules(message)

        if rule_intent != "UNKNOWN":

            return {
                "intent": rule_intent,
                "method": "rules",
                "confidence": 1.0
            }


        # ---------------------------------------------
        # STEP 2: If rules fail, use semantic classifier
        # ---------------------------------------------

        semantic_result = self.semantic_classifier.classify(message)

        return {
            "intent": semantic_result["intent"],
            "method": "semantic",
            "confidence": semantic_result["confidence"],
            "matched_example": semantic_result["matched_example"],
            "top_matches": semantic_result["top_matches"]
        }