import json
from pathlib import Path

from sentence_transformers import SentenceTransformer


class SemanticIntentClassifier:

    def __init__(self):

        # Load the pretrained embedding model
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        # Find our intent dataset
        data_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "intents.json"
        )

        # Load intent examples
        with open(data_path, "r", encoding="utf-8") as file:
            self.intent_examples = json.load(file)

        # Store examples and their intent labels
        self.examples = []
        self.labels = []

        for intent, examples in self.intent_examples.items():

            for example in examples:
                self.examples.append(example)
                self.labels.append(intent)

        # Convert all reference examples into embeddings
        self.example_embeddings = self.model.encode(
            self.examples,
            convert_to_tensor=True
        )

    def classify(self, message: str):

        # Convert the user's message into an embedding
        message_embedding = self.model.encode(
            message,
            convert_to_tensor=True
        )

        # Compare the user's message with all examples
        similarities = self.model.similarity(
            message_embedding,
            self.example_embeddings
        )[0]

        # Get the indices of the 3 most similar examples
        top_indices = similarities.argsort(descending=True)[:3]

        top_matches = []

        for index in top_indices:
            index = index.item()

            top_matches.append({
                "intent": self.labels[index],
                "score": round(similarities[index].item(), 4),
                "example": self.examples[index]
            })

        # Best match
        best_match = top_matches[0]

        return {
            "intent": best_match["intent"],
            "confidence": best_match["score"],
            "matched_example": best_match["example"],
            "top_matches": top_matches
        }