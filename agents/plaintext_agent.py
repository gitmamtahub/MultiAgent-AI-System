import spacy
# spacy.cli.download("en_core_web_lg")

class PlainTextAgent:
    def __init__(self,memory):
        self.memory = memory
        self.nlp = spacy.load("en_core_web_sm")
        
    def process(self, text, intent=None):
        doc = self.nlp(text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        
        # Log to shared memory
        self.memory.log_event({
            "source": "PDFAgent",
            "status": "success",
            "intent": intent,
            "entities": entities,
            "summary": text[:200] + "..." if len(text) > 200 else text
        })
        return {
            "source": "PDFAgent",
            "status": "success",
            "intent": intent,
            "entities": entities,
            "summary": text[:200] + "..." if len(text) > 200 else text
        }
