import streamlit as st
from src.helper import llm_model, text_to_speech, voice_input
from pathlib import Path   # handy for reading the mp3

def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me anything"):
        with st.spinner("Listening…"):
            text = voice_input()          # grab speech
            response = llm_model(text)    # talk to the LLM
            text_to_speech(response)      # synthesize answer

        audio_bytes = Path("speech.mp3").read_bytes()

        st.text_area("Response:", response, height=350)
        st.audio(audio_bytes)
        st.download_button(
            "Download Speech",
            data=audio_bytes,
            file_name="speech.mp3",
            mime="audio/mp3"
        )

# 🚀 This is now at top-level, not indented.
if __name__ == "__main__":
    main()
