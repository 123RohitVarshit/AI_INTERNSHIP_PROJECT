import streamlit as st
import pandas as pd
from utils import load_all_stories
import os

st.set_page_config(page_title="Browse Stories", page_icon="📚", layout="wide")

st.title("📚 Explore the Story Collection")

df = load_all_stories()

if df.empty:
    st.info("No stories have been submitted yet. Be the first to contribute!")
else:
    # --- Filtering and Search ---
    col1, col2 = st.columns([2, 1])
    with col1:
        search_query = st.text_input("Search stories by title")
    with col2:
        all_tags = sorted(list(set(','.join(df['tags'].dropna()).split(','))))
        if '' in all_tags: all_tags.remove('')
        filter_tags = st.multiselect("Filter by tags", all_tags)

    # Apply filters
    if search_query:
        df = df[df['title'].str.contains(search_query, case=False, na=False)]
    if filter_tags:
        df = df[df['tags'].apply(lambda x: all(tag in x for tag in filter_tags))]

    if df.empty:
        st.warning("No stories match your search criteria.")
    else:
        # --- Display Stories ---
        st.write(f"Found {len(df)} stories.")
        st.markdown("---")
        for index, row in df.iterrows():
            with st.container():
                st.subheader(row['title'])
                st.caption(f"Tags: `{row['tags']}` | Submitted on: {pd.to_datetime(row['submission_timestamp']).strftime('%Y-%m-%d')}")
                st.write(row['story_text'])
                if row['audio_path'] and os.path.exists(row['audio_path']):
                    st.audio(row['audio_path'])
                st.markdown("---")