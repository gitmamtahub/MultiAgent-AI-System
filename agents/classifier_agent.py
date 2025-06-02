from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent
from utils.file_utils import detect_format
from agents.intent_classifier import IntentClassifier
from agents.plaintext_agent import PlainTextAgent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.intent_classifier = IntentClassifier()
        self.email_agent = EmailAgent(self.memory)
        self.json_agent = JSONAgent(self.memory)
        self.plaintext_agent = PlainTextAgent(self.memory)

    def classify_and_route(self, input_data):
        # 1. Detect format
        data_format = detect_format(input_data)

        # 2. Predict intent
        if data_format == 'JSON' :
            intent = "check-Log/Result"
            confidence = "check-Log/Result"
        else :
            intent, confidence = self.intent_classifier.predict_intent(input_data)

        # 3. Log in memory
        self.memory.log_event({
            "source": "ClassifierAgent",
            "format": data_format,
            "intent": intent,
            "confidence": confidence
        })

        # 4. Route to appropriate agent
        if data_format == "Email":
            result = self.email_agent.process_email(input_data, intent)
        elif data_format == "JSON":
            result = self.json_agent.process_json(input_data)
        elif data_format == "PlainText-PDF":
            result = self.plaintext_agent.process(input_data, intent)
        else:
            result = {"error": "Unsupported format"}

        return data_format,intent,result