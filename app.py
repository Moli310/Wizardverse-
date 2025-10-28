import os
import pandas as pd
import streamlit as st

# 🎩 Basic page setup
st.set_page_config(
    page_title="WizardVerse AI 🧙‍♂️",
    page_icon="🪄",
    layout="wide"
)

# ✨ Hogwarts header
st.markdown(
    """
    <div style="text-align:center; font-family: 'Garamond'; font-size:40px; color:#d4af37;">
        <b>⚡ WizardVerse AI ⚡</b><br>
        <span style="font-size:20px; color:#e6e6fa;">
        Explore the magic of Harry Potter — books, movies & fandom!
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# 🗂️ Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIES_DIR = os.path.join(BASE_DIR, "movies")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 🧠 Safe CSV loader
@st.cache_data
def safe_load_csv(filename):
    filepath = os.path.join(MOVIES_DIR, filename)
    if not os.path.exists(filepath):
        st.error(f"🪶 Missing file: {filename} — please check if it's uploaded to the `movies/` folder.")
        return None
    return pd.read_csv(filepath, encoding="latin-1")

# 🧙 Load all datasets
with st.spinner("Summoning Hogwarts datasets... 🧙‍♀️"):
    dialogues = safe_load_csv("Dialogue.csv")
    spells = safe_load_csv("Spells.csv")
    characters = safe_load_csv("Characters.csv")
    places = safe_load_csv("Places.csv")
    movies = safe_load_csv("Movies.csv")
    chapters = safe_load_csv("Chapters.csv")

# ✅ Continue only if data loaded
if dialogues is not None and spells is not None:
    st.success("✅ Magical datasets loaded successfully!")

    # 🧾 Show previews
    with st.expander("📜 View Wizarding Dialogues"):
        st.dataframe(dialogues.head(10))

    with st.expander("✨ View Spells and Charms"):
        st.dataframe(spells.head(10))

    st.markdown("---")
    st.markdown(
        "<h3 style='color:#ffd700;'>🏰 Ready to enter the House Quiz Chamber?</h3>",
        unsafe_allow_html=True
    )

    # 🧩 House Selection Quiz
    house = st.radio(
        "Choose your House to start your magical journey:",
        ["Gryffindor 🦁", "Slytherin 🐍", "Ravenclaw 🦅", "Hufflepuff 🦡"]
    )

    # 🖼️ Change background based on selection
    if "Gryffindor" in house:
        bg_path = os.path.join(ASSETS_DIR, "gryffindor_bg.jpg")
    elif "Slytherin" in house:
        bg_path = os.path.join(ASSETS_DIR, "serpent_bg.jpg")
    elif "Ravenclaw" in house:
        bg_path = os.path.join(ASSETS_DIR, "ravenclaw_bg.jpg")
    else:
        bg_path = os.path.join(ASSETS_DIR, "hufflepuff_bg.jpg")

    if os.path.exists(bg_path):
        st.markdown(
            f"""
            <style>
                .stApp {{
                    background-image: url("file://{bg_path}");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"<div style='font-size:20px; color:#e6e6fa;'>Welcome to the {house} challenge! ⚔️</div>",
        unsafe_allow_html=True
    )

    # 🧩 Placeholder for quiz/puzzles
    st.info("🧩 The quiz & puzzle section will appear here soon... Stay tuned for magical riddles and challenges!")
else:
    st.warning("🧹 Waiting for the datasets to be restored before continuing the adventure.")
    st.info("Make sure your `movies/` folder and CSV files are uploaded to GitHub or present locally.")
