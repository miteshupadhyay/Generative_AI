# Simple Q&A Chatbot

This is the simple Q&A Chatbot System using Google Gemini for LLM and LlamaIndex as framework.

Experiments.ipyb file has the entire chatbot functionality in it.
you need to pass GOOGLE_API_KEY inside .env file.

# 1. create the virtual enviroment

conda create -p qa_sys python=3.11 -y

# 2. Activate the virtual environment

conda activate qa_sys

# 3. Install requirements

pip install -r requirements.txt

# 4. run the Streamlit
streamlit run StreamlitApp.py

