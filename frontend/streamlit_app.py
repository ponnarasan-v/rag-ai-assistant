import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="RAG Assistant", layout="centered")

# Simple styling
st.markdown("""
<style>
.answer-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #e8f5e9;
    color: #1b5e20;
    font-size: 16px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 AI Document Assistant (RAG + Ollama)")

query = st.text_input("Ask a question from your document:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, json={"question": query})

            if response.status_code != 200:
                st.error(f"Backend Error:\n{response.text}")
            else:
                data = response.json()

                st.subheader("✅ Answer")

                st.markdown(f"""
                <div class="answer-box">
                {data["answer"]}
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")