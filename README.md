
# Telugu Story and Folklore Collector 📖

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/rohitc1612/Telugu-Story-Collector)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A collaborative web application built with Streamlit to preserve, explore, and share the rich heritage of Telugu stories, folklore, and culture.
---

### ► [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/rohitc1612/Telugu-Story-Collector)

---

## 🎯 Mission

The Telugu language has a rich and diverse history of storytelling. This project aims to create a digital sanctuary for these narratives, providing a platform where anyone can contribute stories, proverbs, and memories. By collecting these tales in an open and accessible way, we hope to create a valuable resource for cultural enthusiasts, researchers, artists, and future generations.

## ❗ Important Note on Data Persistence

The free tier of Hugging Face Spaces provides a **temporary (ephemeral) filesystem**.

**This means that all submitted stories are DELETED whenever the Space restarts or goes to sleep.**

This deployment serves as a fully functional demo. For a production application with permanent data storage, the app would need to be upgraded to use a dedicated cloud database or a Hugging Face Space with a **Persistent Storage** tier.

## ✨ Features

*   **✍️ Unicode Text Submission:** Type stories directly in Telugu.
*   **⌨️ Telugu Virtual Keyboard:** An intuitive on-screen keyboard makes typing easy for everyone.
*   **🔊 AI-Powered Audio Transcription:** Upload an audio story (`.wav`, `.mp3`) and have it automatically transcribed into Telugu text using a fine-tuned Whisper model.
*   **📚 Live Story Browser:** Explore, search, and filter all stories submitted during the current live session.
*   **🔐 Secure & Scalable:** API keys are kept safe using Hugging Face's built-in secrets management.

## 🛠️ Technology Stack

*   **Framework:** Streamlit
*   **Language:** Python
*   **Database:** SQLite (in temporary storage on the server)
*   **AI Model:** `vasista22/whisper-telugu-base` via Hugging Face Inference API
*   **Deployment:** Hugging Face Spaces

## 🚀 Getting Started: Setup and Installation

### Step 1: Get the Code

Clone the repository to your local machine:
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
```

### Step 2: Install Prerequisites

1.  **Python 3.8+:** It's highly recommended to use a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate    # On Windows
    ```

2.  **FFmpeg:** This system-level package is required for audio processing.
    *   **On Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
    *   **On macOS (with Homebrew):** `brew install ffmpeg`
    *   **On Windows:** Download from the [official site](https://ffmpeg.org/download.html) and add to your system's PATH.

3.  **Python Libraries:** Install all required packages from `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Configure the Application

The app needs a Hugging Face API token and a path for its database. The configuration depends on your environment.

#### For Deployment on Hugging Face Spaces (Recommended)

1.  **Set the Secret:** In your Space **Settings > Repository secrets**, create a new secret named `HUGGINGFACE_API_KEY` and paste your Hugging Face token as the value.
2.  **Verify Code:** Ensure your `utils.py` file is configured to read from the server environment:
    *   `DB_PATH` must be `"/tmp/telugu_stories.db"`
    *   The API key must be loaded with `os.getenv("HUGGINGFACE_API_KEY")`

#### For Local Development

1.  **Set the Secret:** Create a file named `.streamlit/secrets.toml` and add your key:
    ```toml
    HUGGINGFACE_API_KEY = "hf_xxxxxxxxxxxxxxxxxxxxxx"
    ```
2.  **Update Code:** In `utils.py`, modify the following lines to use a persistent local database and read from the local secrets file:
    *   Change `DB_PATH` to `"telugu_stories.db"`
    *   Change the API key line to `api_key = st.secrets["HUGGINGFACE_API_KEY"]`

### Step 4: Run the App

Once configured, run the application from your terminal:
```bash
streamlit run app.py
```

## 📂 Project Structure

```
.
├── pages/              # Contains individual app pages
│   ├── 1_✍️_Submit_a_Story.py
│   ├── 2_📚_Browse_Stories.py
│   └── 3_ℹ️_About.py
├── app.py              # Main entry point and homepage
├── utils.py            # Shared functions (DB connection, API calls)
├── requirements.txt    # Python dependencies
├── packages.txt        # System-level dependencies for Hugging Face Spaces (e.g., ffmpeg)
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, please feel free to:
1.  **Fork** the project.
2.  Create a **new branch** for your feature (`git checkout -b feature/NewStoryTheme`).
3.  **Commit** your changes (`git commit -m 'Add new story theme'`).
4.  **Push** to the branch (`git push origin feature/NewStoryTheme`).
5.  Open a **Pull Request**.

## 📄 License

This project is licensed under the Apache 2.0 License.

---
```
