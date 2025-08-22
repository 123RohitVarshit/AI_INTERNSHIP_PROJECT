# utils.py

import streamlit as st
import sqlite3
import pandas as pd
import requests
import time
import os # Make sure os is imported
from datetime import datetime

# --- CORRECTED CODE: Define a writable path for the database ---
# Use the /tmp/ directory which is guaranteed to be writable on Hugging Face Spaces
DB_PATH = "/tmp/telugu_stories.db"

# --- Database Functions ---

def init_db():
    """Initializes the SQLite database and the stories table if it doesn't exist."""
    try:
        # Use the constant DB_PATH
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS stories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    story_text TEXT NOT NULL,
                    tags TEXT,
                    audio_path TEXT,
                    consent INTEGER NOT NULL,
                    submission_timestamp DATETIME NOT NULL
                )
            ''')
            conn.commit()
    except Exception as e:
        # This will now provide a more specific error if it still fails
        st.error(f"Failed to initialize database at {DB_PATH}: {e}")


def save_story(title, story_text, tags, audio_path, consent):
    """Saves a single story submission to the database."""
    try:
        # Use the constant DB_PATH
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO stories (title, story_text, tags, audio_path, consent, submission_timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                (title, story_text, ','.join(tags), audio_path, 1 if consent else 0, datetime.now())
            )
            conn.commit()
    except Exception as e:
        st.error(f"Failed to save story to database: {e}")


def load_all_stories():
    """Loads all consented stories from the database into a DataFrame."""
    # Check if the database file exists before trying to connect
    if not os.path.exists(DB_PATH):
        # If it doesn't exist, return an empty DataFrame to avoid errors
        return pd.DataFrame()
        
    try:
        # Use the constant DB_PATH
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query("SELECT * FROM stories WHERE consent=1 ORDER BY submission_timestamp DESC", conn)
        return df
    except Exception as e:
        st.error(f"Failed to load stories from database: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

# --- Hugging Face API Function (No changes needed here) ---

def transcribe_audio_with_huggingface(audio_path):
    """Sends an audio file to the Hugging Face Inference API for transcription."""
    API_URL = "https://api-inference.huggingface.co/models/vasista22/whisper-telugu-base"
    try:
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key:
            st.error("Hugging Face API key is not set. Please configure it in the Space secrets.")
            return None
        headers = {"Authorization": f"Bearer {api_key}"}

        with open(audio_path, "rb") as f:
            data = f.read()

        response = requests.post(API_URL, headers=headers, data=data)

        if response.status_code == 503:
            st.info("Model is currently loading on the server. Please wait...")
            time.sleep(15)
            response = requests.post(API_URL, headers=headers, data=data)

        response.raise_for_status()
        result = response.json()
        return result.get("text")

    except requests.exceptions.RequestException as e:
        st.error(f"Network or API error: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error during transcription: {e}")
        return None