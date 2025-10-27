# app.py
import streamlit as st
import pandas as pd
import os
import random

# ----------------------------
# SETUP
# ----------------------------
st.set_page_config(page_title="WizardVerse AI: House Quiz", page_icon="🧙‍♂️", layout="wide")

BASE_DIR = os.path.dirname(__file__)  # automatically detects current folder

# Load CSVs safely
@st.cache_data
def load_data():
    dialogues = pd.read_csv(os.path.join(BASE_DIR, "movies", "Dialogue.csv"), encoding="latin-1")
    spells = pd.read_csv(os.path.join(BASE_DIR, "movies", "Spells.csv"), encoding="latin-1")
    return dialogues, spells

dialogues, spells = load_data()

# ----------------------------
# HOUSE THEMES
# ----------------------------
house_themes = {
    "Gryffindor": {"color": "#740001", "bg": "https://i.imgur.com/Ns6h2CJ.jpg"},
    "Slytherin": {"color": "#1A472A", "bg": "https://i.imgur.com/dgZsfxL.jpg"},
    "Ravenclaw": {"color": "#222F5B", "bg": "https://i.imgur.com/wWVuJZX.jpg"},
    "Hufflepuff": {"color": "#EEE117", "bg": "https://i.imgur.com/G0b6v3B.jpg"},
}

# ----------------------------
# MAIN PAGE
# ----------------------------
st.title("🏰 Welcome to WizardVerse AI: The House Challenge")
house = st.selectbox("Choose your Hogwarts House:", list(house_themes.keys()))
theme = house_themes[house]

# Background
st.markdown(
    f"""
    <style>
        body {{
            background-color: {theme['color']};
            background-image: url({theme['bg']});
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f"### 🪄 Welcome, {house} Wizard! Your magical challenge begins now...")

# ----------------------------
# HOUSE QUIZZES
# ----------------------------
if house == "Gryffindor":
    st.header("🦁 Battle of Wits")
    row = dialogues.sample(1).iloc[0]
    quote = row['dialogue']
    ans = row['character']
    guess = st.text_input(f"Who said this quote? 💬 '{quote}'")
    if st.button("Check Answer"):
        if guess.lower().strip() == str(ans).lower().strip():
            st.success("✨ Correct! You’re a true Gryffindor hero!")
        else:
            st.error(f"Incorrect! It was {ans}.")

elif house == "Slytherin":
    st.header("🐍 Riddle of the Serpent")
    riddle = "I can make you invisible, but I’m not a spell. I’m a thing you wear, but not on your feet. What am I?"
    answer = "cloak"
    guess = st.text_input("Decode the Riddle:")
    if st.button("Reveal"):
        if "cloak" in guess.lower():
            st.success("Clever as always — Invisibility Cloak!")
        else:
            st.error("Think deeper, Slytherin. The answer was: *Invisibility Cloak*.")

elif house == "Ravenclaw":
    st.header("🦅 Raven’s Riddle")
    st.write("What magical object shows your deepest desire?")
    guess = st.text_input("Your Answer:")
    if st.button("Submit"):
        if "mirror of erised" in guess.lower():
            st.success("Brilliant! The *Mirror of Erised* — wisdom shines within you 🦅")
        else:
            st.error("Incorrect — the answer was *Mirror of Erised*.")

elif house == "Hufflepuff":
    st.header("🦡 Magical Memory Match")
    row = spells.sample(1).iloc[0]
    effect = row['effect']
    spell = row['spell']
    guess = st.text_input(f"What spell causes this effect? '{effect}'")
    if st.button("Reveal Spell"):
        if guess.lower().strip() == str(spell).lower().strip():
            st.success(f"Well done! It’s {spell}. True Hufflepuff spirit 💛")
        else:
            st.error(f"Almost! The correct spell was {spell}.")
