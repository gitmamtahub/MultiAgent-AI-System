import streamlit as st
from agents.classifier_agent import ClassifierAgent
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent
from agents.plaintext_agent import PlainTextAgent
from memory.shared_memory import SharedMemory

st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
st.title("📦 Multi-Agent AI System")
st.markdown("Enter text (JSON, Email, or Plaintext(PDF text)) to process.")

# Input section
input_text = st.text_area("Enter Input Text", height=200)

if st.button("Run Classification"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Initialize agents
        memory = SharedMemory()
        classifier_agent = ClassifierAgent(memory)
        email_agent = EmailAgent(memory)
        json_agent = JSONAgent(memory)
        pdf_agent = PlainTextAgent(memory)
        

        # Detect format and intent
        data_format, intent , result= classifier_agent.classify_and_route(input_text)

        st.success(f"**Detected Format:** {data_format}")
        st.info(f"**Detected Intent:** {intent}")

        if result:
            st.subheader("🧠 Agent Result")
            st.json(result)

        # Show memory log
        st.subheader("📜 Shared Memory Log")
        memory_log = memory.get_logs()
        st.json(memory_log)
