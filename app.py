import streamlit as st
from utils import init_db

# Set the page configuration. This should be the first Streamlit command.
st.set_page_config(
    page_title="Telugu Story Collector",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This is a community-driven app to collect and share Telugu stories and folklore."
    }
)

# Initialize the database when the app starts.
try:
    init_db()
except Exception as e:
    st.error(f"An error occurred during database initialization: {e}")
    st.warning("The app may not be able to save or load stories.")

# --- Main Homepage Content ---
# This section does NOT contain any page-switching logic or selectbox.

st.title("Welcome to the Telugu Story and Folklore Collector! 📖")

st.markdown("""
This is a community-driven platform dedicated to preserving the rich narrative traditions of the Telugu people. Whether it's a folktale your grandmother told you, a life memory, or a classic proverb, your contribution helps keep our culture alive.

### What can you do here?

*   **✍️ Submit a Story:** Share your stories by typing or uploading an audio recording.
*   **📚 Browse Stories:** Explore the collection of stories shared by our community.
*   **ℹ️ About:** Learn more about the mission and technology behind this project.

**Select a page from the sidebar on the left to get started!**
""")

# Add a simple, non-interactive message in the sidebar.
st.sidebar.success("Select a page above to begin.")