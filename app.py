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

# 🧠 Safe data loader
@st.cache_data
def load_data():
    try:
        dialogues_path = os.path.join(BASE_DIR, "movies", "Dialogue.csv")
        spells_path = os.path.join(BASE_DIR, "movies", "Spells.csv")

        # 🧾 Read CSVs
        dialogues = pd.read_csv(dialogues_path, encoding="latin-1")
        spells = pd.read_csv(spells_path, encoding="latin-1")

        return dialogues, spells

    except FileNotFoundError as e:
        st.error("🪶 Oops! A magical scroll (CSV) has gone missing in Hogwarts’ archives.")
        st.info("Make sure your `movies/` folder and CSV files are uploaded to GitHub or present locally.")
        st.code(str(e))
        return None, None


# 🧙 Load data
dialogues, spells = load_data()

# ✅ Continue only if data loaded
if dialogues is not None and spells is not None:
    st.success("✅ Magical datasets loaded successfully!")

    # Show preview
    with st.expander("📜 View a glimpse of the Wizarding dialogues"):
        st.dataframe(dialogues.head(10))

    with st.expander("✨ View spells and charms"):
        st.dataframe(spells.head(10))

    st.markdown("---")
    st.markdown(
        "<h3 style='color:#ffd700;'>🏰 Ready to enter the House Quiz Chamber?</h3>",
        unsafe_allow_html=True
    )

    # 🧩 House Selection Quiz Placeholder
    house = st.radio(
        "Choose your House to start your magical journey:",
        ["Gryffindor 🦁", "Slytherin 🐍", "Ravenclaw 🦅", "Hufflepuff 🦡"]
    )

    st.markdown(
        f"<div style='font-size:20px; color:#e6e6fa;'>Welcome to the {house} challenge! ⚔️</div>",
        unsafe_allow_html=True
    )

    st.write("🧩 The quiz & puzzle section will appear here soon...")
else:
    st.warning("🧹 Waiting for the datasets to be restored before continuing the adventure.")
