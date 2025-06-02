from pydantic import BaseModel, ValidationError, validator, EmailStr
from typing import Optional, Dict, Any
from agents.intent_classifier import IntentClassifier
import json

class ProductOrder(BaseModel):
    product_id: str
    price: float
    currency: str
    quantity: int
    buyer_email: EmailStr

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory
        self.intent_classifier = IntentClassifier()

    def process_json(self, text) -> Dict[str, Any]:
        
        try:
            payload = json.loads(text)
            order = ProductOrder(**payload)
            result = order.dict()
            status = "success"
            issues = None
        except ValidationError as e:
            result = None
            status = "error"
            issues = e.errors()

        # Flatten JSON to a string
        if result :
            text = " ".join(f"{k}: {v}" for k, v in result.items())

            # Classify intent
            intent, confidence = self.intent_classifier.predict_intent(text)

            # Validate fields (if needed)
            missing = self.validate_json(result)
        else :
            intent = None
            confidence = None
            missing = None
        
        # Log to shared memory
        self.memory.log_event({
            "source": "JSONAgent",
            "status": status,
            "validated_data": result,
            "issues": issues,
            "intent": intent,
            "confidence": confidence,
            "missing": missing
        })

        return {
            "source": "JSONAgent",
            "status": status,
            "validated_data": result,
            "issues": issues,
            "intent": intent,
            "confidence": confidence,
            "missing": missing
        }
        
    def validate_json(self, data):
        # Example validation logic
        required = ["product_id", "price", "currency", "quantity", "buyer_email"]
        missing = [field for field in required if field not in data]
        if missing:
            return {"missing_fields": missing}
        return None
