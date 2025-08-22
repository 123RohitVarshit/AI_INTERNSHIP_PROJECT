# Project Report: Telugu Story and Folklore Collector

**Author:** [Rohit Chiluka]
**Date:** July 24, 2025
**Version:** 1.0.0
**Status:** Live Demonstration Deployed

---

## 1. Project Summary

The Telugu Story and Folklore Collector is a full-featured, collaborative web application designed to preserve, explore, and share the rich cultural heritage of Telugu stories. Developed using Python and the Streamlit framework, the platform enables users to submit stories as text or audio recordings. A key feature is its AI-powered speech-to-text transcription, which leverages a fine-tuned Whisper model via the Hugging Face API to convert spoken Telugu into Unicode text.

The application is deployed as a live demo on Hugging Face Spaces, demonstrating a modern, scalable approach to building and sharing AI-powered applications. It addresses significant usability and technical challenges, including providing an intuitive Telugu virtual keyboard and navigating the constraints of a serverless, read-only deployment environment.

---

## 2. Introduction and Motivation

### 2.1. The Problem
Oral traditions, folktales, and personal histories are vital components of any culture. In the digital age, these narratives are at risk of being lost as they are not always documented. The Telugu language, with its rich history of literature and storytelling, faces this challenge. There is a need for an accessible, community-driven platform where anyone—from elders recounting memories to parents sharing children's stories—can easily contribute and preserve these invaluable cultural assets.

### 2.2. The Solution
This project directly addresses this need by creating a centralized, digital sanctuary for Telugu stories. The core objectives were to:
1.  **Lower the Barrier to Entry:** Allow submissions via both simple text input and more natural audio recordings.
2.  **Ensure Accessibility:** Implement a virtual Telugu keyboard for users without specialized hardware.
3.  **Leverage Modern AI:** Use state-of-the-art speech recognition to make audio content searchable and readable.
4.  **Foster a Community:** Create a browseable, filterable gallery of stories for all users to enjoy.
5.  **Build a Scalable Prototype:** Develop a secure, easily deployable application that serves as a robust proof-of-concept.

---

## 3. Core Functionalities

The application is structured as a multi-page Streamlit app with the following key features:

### 3.1. Story Submission
*   **Multi-modal Input:** Users can either type their story directly into a text area or upload an audio file (`.wav`, `.mp3`).
*   **Telugu Virtual Keyboard:** A custom, tabbed on-screen keyboard allows users to easily input Telugu vowels (అచ్చులు), consonants (హల్లులు), and common words with simple clicks. This is critical for users on devices without native Telugu keyboard support.
*   **Metadata Collection:** Each story is accompanied by a title and can be categorized with multiple tags (e.g., Folktale, Proverb, Life Memory) for better organization.
*   **Informed Consent:** A mandatory consent checkbox ensures that users agree to have their submission become part of the open dataset, promoting ethical data collection.

### 3.2. AI-Powered Audio Transcription
When a user uploads an audio file, it is sent to the Hugging Face Inference API. The backend uses the `vasista22/whisper-telugu-base` model, a version of OpenAI's Whisper fine-tuned specifically for the Telugu language. This provides highly accurate, automated transcription, converting spoken stories into searchable Unicode text.

### 3.3. Story Browsing and Exploration
*   **Centralized Story Feed:** A dedicated page displays all consented stories in a clean, reverse-chronological feed.
*   **Search and Filter:** Users can perform a full-text search on story titles or apply one or more tags to filter the collection, making it easy to discover tales of interest.
*   **Integrated Playback:** For stories submitted with audio, an embedded player appears directly below the transcribed text, allowing users to listen to the original recording.

### 3.4. User Interface and Experience (UI/UX)
*   **Multi-Page Architecture:** The application is split into logical sections (Homepage, Submit, Browse, About) using Streamlit's native multi-page functionality, providing clear and intuitive navigation.
*   **Responsive Design:** The UI is designed to be functional and aesthetically pleasing across various screen sizes, from mobile phones to desktops.
*   **Anonymity and Privacy:** The platform does not require user logins or collect any personal data, ensuring contributor privacy.

---

## 4. System Architecture and Technology Stack

### 4.1. Architecture
The application follows a simple but powerful client-server architecture:
1.  **Frontend:** Built entirely with **Streamlit**. It handles user interaction, renders the UI, and manages application state.
2.  **Backend Logic (`utils.py`):** A separate utility module encapsulates core logic for database interactions and external API calls. This separation of concerns makes the code cleaner and more maintainable.
3.  **Database:** A **SQLite** database is used for its simplicity and serverless nature. On deployment, it operates in a temporary, in-memory mode.
4.  **External AI Service:** The **Hugging Face Inference API** acts as the AI backend, handling the computationally intensive task of speech recognition.

### 4.2. Technology Stack

| Component                | Technology                                   | Justification                                                                                             |
| ------------------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Web Framework**        | Streamlit                                    | Chosen for its speed in developing data-centric, interactive web applications directly in Python.           |
| **Programming Language** | Python                                       | The de facto language for data science and AI, with extensive libraries for every required task.          |
| **Database**             | SQLite                                       | Lightweight, file-based, and requires no separate server, making it ideal for a self-contained application. |
| **Speech-to-Text AI**    | Hugging Face Inference API (`whisper-telugu`) | Provides free, scalable access to a high-quality, specialized AI model without needing to host it ourselves.  |
| **Deployment Platform**  | Hugging Face Spaces                          | Offers a seamless, Git-based deployment workflow for Streamlit apps, with integrated secret management.      |
| **Audio Processing**     | Pydub                                        | A robust library for handling various audio file formats, used as a dependency for audio processing.        |
| **Data Handling**        | Pandas                                       | Used for efficiently loading and filtering story data from the database for the "Browse" page.              |

---

## 5. Challenges and Solutions

Several technical challenges were encountered and successfully resolved during development:

1.  **Challenge:** Streamlit's `st.form` component does not allow interactive widgets like `st.button` inside it, which conflicted with the virtual keyboard design.
    *   **Solution:** The application architecture was refactored to separate the interactive elements (keyboard, text area) from the final submission form. The keyboard and text area now modify `st.session_state` directly, while the form only collects metadata and a final "Submit" click.

2.  **Challenge:** The initial user interface had two competing navigation systems, causing confusion.
    *   **Solution:** The redundant `st.selectbox` menu was removed, and the project was fully converted to use Streamlit's native, file-based multi-page app structure for clear, unambiguous navigation.

3.  **Challenge:** During deployment to Hugging Face Spaces, the application crashed with an `unable to open database file` error.
    *   **Solution:** The root cause was identified as the **read-only filesystem** of the deployment environment. The code was modified to create and access the SQLite database file in the writable `/tmp/` directory, a standard practice for such platforms.

4.  **Challenge:** Securing the Hugging Face API key without exposing it in the public code repository.
    *   **Solution:** The application was configured to read the API key from an environment variable (`os.getenv`). This key is stored securely using **Repository secrets** in the Hugging Face Space settings, which injects it into the environment at runtime.

---

## 6. Future Work and Potential Enhancements

This project serves as a strong foundation. Future development could include:
*   **Persistent Storage:** Integrate a cloud-based database service (e.g., Neon, Supabase, Firebase) to ensure that submitted stories are stored permanently.
*   **User Accounts:** Allow users to create accounts to track their submissions and edit them later.
*   **Community Engagement Features:** Implement features like "likes," comments, and social sharing to foster a more interactive community.
*   **Content Moderation:** Develop a system for users to flag inappropriate content and for administrators to review submissions.
*   **Data Analytics Dashboard:** Create a page that visualizes metadata, such as the geographic origin of stories (if collected), the most popular tags, or submission trends over time.
*   **Text-to-Speech (TTS):** Add a feature to read typed stories aloud using a Telugu TTS engine, enhancing accessibility.

## 7. Conclusion

The Telugu Story and Folklore Collector successfully achieves its goal of creating a functional, user-friendly platform for cultural preservation. It demonstrates the power of combining modern tools like Streamlit and Hugging Face to build and deploy meaningful, AI-enhanced applications rapidly. While the current deployment has limitations regarding data persistence, it stands as a robust proof-of-concept and a valuable template for future community-driven archival projects.