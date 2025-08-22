import streamlit as st
from utils import save_story, transcribe_audio_with_huggingface
import os
from datetime import datetime

st.set_page_config(page_title="Submit a Story", page_icon="✍️", layout="wide")

st.title("✍️ Submit Your Story")
st.markdown("Share your story by typing it out or uploading an audio file.")


# --- Virtual Keyboard ---
def append_to_story(char):
    st.session_state.story_text += char


def telugu_keyboard():
    st.write("### Telugu Virtual Keyboard")
    vowels = "అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః".split()
    consonants = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ".split()
    common_words = "నమస్కారం ఎలా ఉన్నారు ధన్యవాదాలు దయచేసి అవును కాదు నేను మీరు".split()

    tab1, tab2, tab3 = st.tabs(["Vowels (అచ్చులు)", "Consonants (హల్లులు)", "Common Words (సాధారణ పదాలు)"])

    with tab1:
        cols = st.columns(8)
        for i, vowel in enumerate(vowels):
            cols[i % 8].button(vowel, key=f"vowel_{vowel}", on_click=append_to_story, args=(vowel,))
    with tab2:
        cols = st.columns(10)
        for i, consonant in enumerate(consonants):
            cols[i % 10].button(consonant, key=f"consonant_{consonant}", on_click=append_to_story, args=(consonant,))
    with tab3:
        cols = st.columns(5)
        for i, word in enumerate(common_words):
            cols[i % 5].button(word, key=f"word_{word}", on_click=append_to_story, args=(word + " ",))


# --- Main Submission Logic ---

# Initialize session state
if 'story_text' not in st.session_state:
    st.session_state.story_text = ""

# Part 1: Interactive elements OUTSIDE the form
telugu_keyboard()
st.session_state.story_text = st.text_area(
    "**Your Story** (use the keyboard above or type here)",
    value=st.session_state.story_text,
    height=200,
    key="story_text_input"
)
st.markdown("---")

# Part 2: Clean form for metadata and submission
with st.form("story_form", clear_on_submit=True):
    st.write("### Story Details & Final Submission")
    title = st.text_input("**Title**", placeholder="Enter the title of your story")
    st.markdown("Or, upload an audio story (this will replace any text you have typed above):")
    audio_file = st.file_uploader("Upload an Audio Story (.wav, .mp3)", type=["wav", "mp3"])
    tags = st.multiselect("Select tags", ["Folktale", "Proverb", "Children's Story", "Life Memory", "Mythology"])
    st.markdown("---")
    st.subheader("Data Policy and Consent")
    st.info("By submitting, you agree that your story will become part of an open dataset.")
    consent = st.checkbox("I agree to the terms and consent to my submission.", value=False)

    submitted = st.form_submit_button("Submit Story")

    if submitted:
        final_story_text = st.session_state.story_text
        if not title or not (final_story_text or audio_file) or not consent:
            st.warning("Please provide a title, a story (text or audio), and your consent.")
        else:
            audio_path = None
            if audio_file:
                if not os.path.exists("audio_files"):
                    os.makedirs("audio_files")

                audio_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{audio_file.name}"
                audio_path = os.path.join("audio_files", audio_filename)

                with open(audio_path, "wb") as f:
                    f.write(audio_file.getbuffer())

                with st.spinner("Transcribing audio... Please wait."):
                    transcribed_text = transcribe_audio_with_huggingface(audio_path)
                    if transcribed_text:
                        st.success("Audio transcribed successfully!")
                        final_story_text = transcribed_text
                    else:
                        st.error("Failed to transcribe audio.")

            if final_story_text:
                save_story(title, final_story_text, tags, audio_path, consent)
                st.success("Your story has been submitted successfully! Thank you.")
                st.session_state.story_text = ""  # Clear text area for next submission