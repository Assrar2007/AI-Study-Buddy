import streamlit as st
# NEW CODE (flat structure)
from summarizer import summarize
from explainer import explain
from flashcards import generate_flashcards
from quiz_generator import generate_mcq
from chatbot import chat
from pdf_reader import extract_text_from_pdf
from voice_to_text import transcribe_audio
from exporters import export_to_pdf

st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide")

st.sidebar.title("📚 AI Study Buddy")
menu = st.sidebar.radio("Navigation", ["Home", "Text Input", "PDF Upload", "Audio Input", "Chatbot", "Export"])

st.sidebar.markdown("---")
st.sidebar.write("Built using FLAN-T5 + Whisper")


# -------------------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------------------
if menu == "Home":
    st.title("📚 AI Study Buddy")
    st.write("Welcome! This intelligent assistant helps you study better by generating summaries, explanations, flashcards, quizzes and more.")

    st.markdown("""
        ### ✨ Features:
        - 📑 Summarization
        - ✍🏼 Simplified Explanation
        - 🎴 Flashcards
        - 📝 MCQ Quiz Generation
        - 🤖 Chatbot Assistance
        - 📄 PDF Input Support
        - 🎧 Audio Input (Whisper)
        - 🖨 Export as PDF
    """)


# -------------------------------------------------------------------
# TEXT INPUT
# -------------------------------------------------------------------
elif menu == "Text Input":
    st.title("✍🏼 Text Input")
    text_input = st.text_area("Paste your study material here:", height=250)

    if st.button("Generate Study Material"):
        if text_input:
            summary = summarize(text_input)
            explanation = explain(text_input)
            flashcards = generate_flashcards(text_input)
            mcq = generate_mcq(text_input)

            st.subheader("📑 Summary")
            st.write(summary)

            st.subheader("✍🏼 Explanation")
            st.write(explanation)

            st.subheader("🎴 Flashcards")
            st.write(flashcards)

            st.subheader("📝 MCQs")
            st.write(mcq)

            st.session_state['summary'] = summary
            st.session_state['explanation'] = explanation
            st.session_state['flashcards'] = flashcards
            st.session_state['mcq'] = mcq


# -------------------------------------------------------------------
# PDF INPUT
# -------------------------------------------------------------------
elif menu == "PDF Upload":
    st.title("📄 PDF Upload")
    pdf_file = st.file_uploader("Upload your PDF file", type=["pdf"])

    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        st.success("PDF extracted successfully!")
        st.write(text[:1000] + " ...")

        if st.button("Generate Study Material from PDF"):
            summary = summarize(text)
            explanation = explain(text)
            flashcards = generate_flashcards(text)
            mcq = generate_mcq(text)

            st.session_state['summary'] = summary
            st.session_state['explanation'] = explanation
            st.session_state['flashcards'] = flashcards
            st.session_state['mcq'] = mcq

            st.success("Material generated successfully! Go to Export tab to save!")


# -------------------------------------------------------------------
# AUDIO INPUT
# -------------------------------------------------------------------
elif menu == "Audio Input":
    st.title("🎧 Audio Input")
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

    if audio_file:
        st.info("Transcribing audio ...")
        text = transcribe_audio(audio_file)
        st.write("### Extracted Text:")
        st.write(text)

        if st.button("Generate Study Material from Audio"):
            summary = summarize(text)
            explanation = explain(text)
            flashcards = generate_flashcards(text)
            mcq = generate_mcq(text)

            st.session_state['summary'] = summary
            st.session_state['explanation'] = explanation
            st.session_state['flashcards'] = flashcards
            st.session_state['mcq'] = mcq

            st.success("Material generated successfully! Go to Export tab to save!")


# -------------------------------------------------------------------
# CHATBOT
# -------------------------------------------------------------------
elif menu == "Chatbot":
    st.title("🤖 Study Assistant Chatbot")
    user_query = st.text_input("Ask me anything:")

    if st.button("Ask"):
        answer = chat(user_query)
        st.subheader("Answer:")
        st.write(answer)


# -------------------------------------------------------------------
# EXPORT
# -------------------------------------------------------------------
elif menu == "Export":
    st.title("🖨 Export Study Material")

    if all(k in st.session_state for k in ['summary', 'explanation', 'flashcards', 'mcq']):
        if st.button("Export to PDF"):
            path = export_to_pdf(
                st.session_state['summary'],
                st.session_state['explanation'],
                st.session_state['flashcards'],
                st.session_state['mcq'],
                "chatbot unused"
            )
            st.success(f"File exported: {path}")
            with open(path, "rb") as f:
                st.download_button("Download PDF", f, file_name=path)
    else:
        st.warning("No content to export yet! Generate material first.")