# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-07-24

This marks the first stable, deployable release of the Telugu Story and Folklore Collector. This version includes all core functionalities and has been successfully deployed to Hugging Face Spaces.

### Added

-   **Core Application Functionality:**
    -   Implemented story submission via text input with a Unicode Telugu virtual keyboard.
    -   Added audio story submission (`.wav`, `.mp3`) with AI-powered transcription.
    -   Created a "Browse Stories" page with search and tag-based filtering.
    -   Established the SQLite database schema for storing stories and metadata.
-   **AI Integration:**
    -   Integrated with the Hugging Face Inference API to use the `vasista22/whisper-telugu-base` model for accurate Telugu speech-to-text.
-   **Multi-Page Structure:**
    -   Organized the application into a clean multi-page layout with dedicated pages for "Submit a Story", "Browse Stories", and "About".
-   **Project Documentation:**
    -   Created `README.md` with project overview, setup instructions, and deployment guide.
    -   Added an `Apache-2.0` `LICENSE` file.
    -   Created this `CHANGELOG.md` file.
-   **Deployment Configuration:**
    -   Added `requirements.txt` for Python dependencies.
    -   Added `packages.txt` to install `ffmpeg` on the deployment server, enabling audio processing.

### Changed

-   **Major Project Restructuring:**
    -   Refactored the initial project structure by moving all Python source files from a nested `src/` directory to the repository's root directory. This critical change was made to ensure compatibility with Streamlit's multi-page app discovery mechanism on Hugging Face Spaces.
-   **Database Path for Deployment:**
    -   Modified `utils.py` to create and access the SQLite database in the writable `/tmp/` directory. This was a crucial change to enable the application to run on Hugging Face's read-only filesystem.
-   **API Key Management:**
    -   Enhanced security by configuring the application to read the `HUGGINGFACE_API_KEY` from environment variables, using Hugging Face's built-in repository secrets instead of local files for deployment.

### Fixed

-   **Multi-Page Navigation:** Resolved a critical deployment issue where the sidebar navigation links would not appear. This was fixed by the project restructuring described above.
-   **Database Errors on Startup:** Fixed the `unable to open database file` error that occurred during deployment by changing the database path to a writable location.

---