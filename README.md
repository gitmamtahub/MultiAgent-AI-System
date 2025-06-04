# 🧠 Multi-Agent AI System for Input Classification and Routing

This project is a multi-agent AI system that processes **JSON**, **Email**, and **Plaintext/PDF Text** inputs. It detects the format and intent, routes the data to specialized agents, extracts structured information, and logs the results in a shared memory module. The system is extensible, interpretable, and includes a Streamlit-based UI for interaction.

---

## 🚀 Features

- 📂 **Format Detection**: Automatically identifies if input is JSON, Email, or Plaintext/PDF.
- 🎯 **Intent Classification**: Uses a fine-tuned BERT model to classify intents (e.g., RFQ, Complaint, Invoice).
- 🧠 **Shared Memory**: Logs metadata and extracted information across agents for traceability.
- 📨 **Email Agent**: Extracts sender, subject, urgency, timestamp, and named entities.
- 🧾 **JSON Agent**: Validates and reformats structured product order data.
- 📜 **Plaintext Handler**: Parses unstructured text, detects intent, and logs relevant info.
- 🎛️ **Streamlit UI**: Simple web interface to interact with the system and view results.

---

## 🏗️ System Architecture
                      **User Input (UI)** 
                      **Classifier Agent**        
          **Email Agent    JSON Agent     Plaintext/PDF Agent**   
                        **Shared Memoey**

User Input → Detected as Email + Intent: RFQ → Routed to Email Agent
→ Extracted entities + sender + urgency → Logged in Shared Memory

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-agent-intent-system.git
cd multi-agent-intent-system

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install Dependencies

pip install -r requirements.txt

4. Download the trained BERT model (fine-tuned):

Place it under ./model/

5. Running the App
streamlit run app.py

Use the Streamlit interface to:
Paste email, JSON, or plaintext
View detected format and intent
See results from the appropriate agent
Access memory log

## Intent Labels
Trained intents (editable in intent_classifier.py):

1) Complaint
2) Invoice
3) RFQ (Request for Quotation)
4) Regulation
5) Review

## Project Structure
.
├── app.py                  # Streamlit UI
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   ├── json_agent.py
│   ├── plaintext_agent.py
│   └── intent_classifier.py
├── memory/
│   └── shared_memory.py
├── model/                  # Trained BERT model
│   ├── config.json
│   ├── model.safetensors   # very large size imp file cannot be push to github
│   ├── special_tokens_map.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   └── vocab.txt
├── train/                  # not included as we need only inferences for this application
│   ├── train.py            # BERT trained for this purpose
│   └── data.csv            # Training data for intent classification
├── utils/
│   └── file_utils.py       # Format detection
├── label_encoder.pkl       # can't be used with Auttokenizer and AutoModels so not on github
├── requirements.txt
└── README.md

🛠️ Tech Stack
Python 🐍
Hugging Face Transformers 🤗
PyTorch 🔥
spaCy (NER) 🔍
Streamlit 🌐
In-Memory Store 📦

📚 Future Work
Extend to handle CSV, DOCX, or image (OCR) inputs
Add User Authentication
Store logs in Redis or a persistent DB
Export memory logs as downloadable reports

📃 License
This is open-source project

🙋‍♂️ Author
Made with ❤️ by [Mamta Khatri]
