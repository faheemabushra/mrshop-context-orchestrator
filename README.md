# Mr.Shop Context Orchestrator

A prototype conversational AI orchestration system for Mr.Shop.

It identifies user intent, pulls out useful entities, keeps track of conversational context, and handles topic switches mid-conversation.

---

## 1. Objective

This prototype shows how a conversational fashion assistant can coordinate several components instead of leaning on a single intent classifier.

It supports four core intents:

- WARDROBE_UPLOAD
- STYLING_ADVICE
- PURCHASE
- BOOKING

---

## 2. Architecture

```text
                    USER MESSAGE
                         |
                         v
                 +---------------+
                 |    FastAPI    |
                 +-------+-------+
                         |
                         v
              +----------------------+
              | Hybrid Intent        |
              | Classifier           |
              | Rules + Embeddings   |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | Entity Extractor     |
              | Color / Item / Budget|
              +----------+-----------+
                         |
                         v
              +----------------------+
              | Context Manager      |
              | Intent + Entities +  |
              | Conversation History |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | Orchestrator         |
              +----------+-----------+
                         |
                         v
                     RESPONSE
```

---

## 3. Components

### Hybrid Intent Classifier

The classifier combines two approaches:

- Rule-based matching for clear, predictable requests.
- Semantic similarity via Sentence Transformers when the rules can't pin down the intent directly.

This gives a lighter-weight alternative to calling an LLM on every message. The semantic classifier uses the `all-MiniLM-L6-v2` sentence embedding model to compare a user message against a set of predefined examples for each intent.

### Entity Extractor

A rule-based extractor picks out:

- Clothing item
- Color
- Budget

Example:

```
"Find me a red dress below 3000"

Intent: PURCHASE
Entities:
  color = red
  item = dress
  budget = 3000
```

### Context Manager

Keeps track of:

- Current intent
- Previous intent
- Extracted entities
- Conversation history

New entities get merged into the existing context, so information from earlier messages stays available as the conversation continues.

### Orchestrator

Coordinates the full processing pipeline for each turn:

```
User Message
     |
     v
Intent Classification
     |
     v
Entity Extraction
     |
     v
Context Update
     |
     v
Response Generation
```

---

## 4. Topic Switching

The prototype handles moving between intents within the same conversation.

**Message 1**
> "I have a blue blazer. How should I style it?"

Detected: `STYLING_ADVICE`, with `color = blue`, `item = blazer`.

**Message 2**
> "Actually, show me something white under 2000."

Switches to `PURCHASE`, with `color = white`, `budget = 2000`. The context manager keeps the previously detected information while updating the current intent and adding the new entities.

**Message 3**
> "Can I speak with someone who can help me choose colours?"

Switches again, this time to `BOOKING`. This is the point of the design: no message is treated as fully isolated from the ones before it.

---

## 5. Project Structure

```
mrshop-context-orchestrator/
│
├── app/
│   ├── __init__.py
│   │
│   ├── classifier/
│   │   ├── __init__.py
│   │   ├── rules.py
│   │   ├── embeddings.py
│   │   ├── hybrid.py
│   │   ├── test_rules.py
│   │   └── test_hybrid.py
│   │
│   ├── extractor/
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   └── test_entities.py
│   │
│   ├── context/
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   └── test_manager.py
│   │
│   ├── orchestrator/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   └── test_engine.py
│   │
│   └── main.py
│
├── data/
│   └── intents.json
│
├── README.md
└── .venv/
```

---

## 6. Technologies

- Python
- FastAPI
- Pydantic
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Regular expressions

---

## 7. Running the Prototype

**1. Activate the virtual environment**

Windows PowerShell:
```
.venv\Scripts\activate
```

**2. Install dependencies**
```
pip install fastapi uvicorn pydantic sentence-transformers
```

**3. Start the API**
```
uvicorn app.main:app --reload
```

**4. Open the API docs**

Go to `http://127.0.0.1:8000/docs` — the Swagger interface lets you test the `/chat` endpoint directly.

---

## 8. API Usage

**Endpoint:** `POST /chat`

Request:
```json
{
  "message": "Show me something white under 2000"
}
```

Response:
```json
{
  "message": "Show me something white under 2000",
  "intent": "PURCHASE",
  "classification_method": "rules",
  "confidence": 1.0,
  "entities": {
    "color": "white",
    "budget": 2000
  },
  "context": {
    "current_intent": "PURCHASE",
    "previous_intent": "STYLING_ADVICE"
  },
  "response": "I can find products within your ₹2000 budget."
}
```

---

## 9. Example Conversations

**Conversation 1 — Styling**
```
USER: I have a blue blazer. How should I style it?
SYSTEM: I can suggest styling options for your blue blazer.

Intent: STYLING_ADVICE
Entities: color = blue, item = blazer
```

**Conversation 2 — Purchase**
```
USER: Show me something white under 2000.
SYSTEM: I can find products within your ₹2000 budget.

Intent: PURCHASE
Entities: color = white, budget = 2000
```

**Conversation 3 — Booking**
```
USER: Can I speak with someone who can help me choose colours?
SYSTEM: I can help you arrange a fashion consultation.

Intent: BOOKING
```

**Conversation 4 — Topic Switch**
```
USER: I have a blue blazer. How should I style it?
SYSTEM: STYLING_ADVICE

USER: Actually, show me something white under 2000.
SYSTEM: PURCHASE

Previous intent: STYLING_ADVICE
Current intent: PURCHASE
Context retained: item = blazer, color = white, budget = 2000
```

---

## 10. Design Decisions

**Why a hybrid classifier?**
Rules are fast and predictable for explicit requests. Semantic similarity picks up natural language variations that don't contain the exact predefined keywords. Together they give a simple, lightweight classification strategy that's reasonable for a prototype.

**Why semantic embeddings?**
They let messages with similar meaning match even when the wording differs — "How should I style my jacket?" and "What goes well with my jacket?" end up close together even though they don't share much vocabulary.

**Why not an LLM?**
The point of this prototype is to show the orchestration, not large-scale response generation. A local semantic model keeps things simple, avoids an external API dependency, and makes the classification pipeline easy to inspect and explain.

**Why maintain context?**
A conversational system shouldn't treat every message as if it arrived out of nowhere. Tracking previous intent, current intent, entities, and history lets the system follow topic changes without losing information from earlier turns.

---

## 11. Prototype Limitations

This is intentionally a lightweight build, not a production system. Current limitations:

- Limited predefined intent examples
- Lightweight rule-based entity extraction
- No persistent database
- Context only lives within the active orchestrator instance
- No real product, wardrobe, or booking integration
- Template-based response generation
- Limited entity vocabulary

These are deliberate trade-offs — the goal here is the orchestration architecture, not a finished product.

---

## 12. Future Improvements

A production version would need:

- More robust intent classification
- Confidence thresholds and ambiguity handling
- LLM-assisted entity extraction
- Persistent user/session memory
- A vector database for long-term conversational memory
- Real wardrobe and product services
- Booking service integration
- Authentication and user-specific context
- Monitoring and evaluation pipelines
- Better response generation
- API rate limiting and error handling

---

## 13. Summary

The prototype demonstrates a conversational orchestration pipeline: hybrid intent classification feeds entity extraction, which feeds context management, which feeds orchestration and response generation. It supports four core intents and handles topic switching while keeping relevant context from earlier in the conversation.

The architecture is modular by design, so individual components can be swapped for more capable models or external services later without rebuilding the whole system.