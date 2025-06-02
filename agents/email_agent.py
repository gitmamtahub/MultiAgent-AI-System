import re
from datetime import datetime
from email.utils import parsedate_to_datetime
import spacy
# spacy.cli.download("en_core_web_lg")

class EmailAgent:
    def __init__(self,memory):
        self.memory = memory
        self.nlp = spacy.load("en_core_web_sm")

    def process_email(self, email_text, intent):
        sender = self.extract_sender(email_text)
        subject = self.extract_subject(email_text)
        timestamp = self.extract_timestamp(email_text)
        urgency = self.detect_urgency(email_text)
        entities = self.extract_entities(email_text)

        email_data = {
            "sender": sender,
            "subject": subject,
            "intent": intent,
            "urgency": urgency,
            "timestamp": timestamp,
            "entities": entities
        }

        # Log to shared memory
        self.memory.log_event({
            "source": "EmailAgent",
            "data": email_data
        })

        return {
            "source": "EmailAgent",
            "data": email_data
        }   

    def extract_sender(self, text):
        match = re.search(r"From:\s*(\S+@\S+)", text)
        return match.group(1) if match else "unknown"

    def extract_subject(self, text):
        match = re.search(r"Subject:\s*(.*)", text)
        return match.group(1).strip() if match else "No Subject"
    
    def extract_timestamp(self, text):
        match = re.search(r"Date:\s*(.*)", text)
        if match:
            try:
                return parsedate_to_datetime(match.group(1)).isoformat()
            except Exception:
                return datetime.now().isoformat()
         # fallback if no Date header
        return datetime.now().isoformat()

    def detect_urgency(self, text):
        urgent_keywords = ["urgent", "asap", "immediately", "priority", "as soon as possible"]
        text_lower = text.lower()
        for word in urgent_keywords:
            if word in text_lower:
                return "High"
        return "Normal"
    
    def extract_entities(self, text):
        doc = self.nlp(text)
        return [{"text": ent.text, "label": ent.label_} for ent in doc.ents if ent.label_ in ["DATE", "GPE", "CARDINAL", "PRODUCT","ORG"]]
