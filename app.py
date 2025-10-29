import streamlit as st
from pathlib import Path
import base64

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Helper function to set background ----
def set_background(image_path: str):
    file_path = Path(image_path)
    if not file_path.exists():
        st.warning(f"⚠️ Background image not found: {file_path}")
        return
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- Sample Quizzes and Puzzles ----
quizzes = {
    "Gryffindor": [
        {"q": "Who founded Gryffindor?", "a": "Godric", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "What is the Gryffindor emblem?", "a": "Lion", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Gryffindor common room is in?", "a": "Tower", "options": ["Tower", "Basement", "Library", "Dungeon"]},
        {"q": "Gryffindor ghost is?", "a": "Nearly Headless Nick", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Gryffindor colors?", "a": "Red and Gold", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "What is Gryffindor's sword made of?", "a": "Silver", "options": ["Silver", "Gold", "Bronze", "Iron"]},
        {"q": "Famous Gryffindor student?", "a": "Harry Potter", "options": ["Harry Potter", "Draco Malfoy", "Luna Lovegood", "Cedric Diggory"]},
        {"q": "House known for bravery?", "a": "Gryffindor", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Gryffindor founder valued?", "a": "Courage", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]}
    ],
    # Repeat similar 9 quizzes for other houses
}

puzzles = {
    "Gryffindor": [
        {"p": "Unscramble: DRCIGO", "a": "Godric"},
        {"p": "Unscramble: NOIL", "a": "Lion"},
        {"p": "Unscramble: YRAEGFHCIDRNO", "a": "Gryffindor"},
        {"p": "Unscramble: KNHECYCEEEDHL", "a": "Nearly Headless Nick"},
        {"p": "Unscramble: VGEANR", "a": "Graven"},
        {"p": "Unscramble: EVRCOAUG", "a": "Courage"},
        {"p": "Unscramble: PTHRAY POTTER", "a": "Harry Potter"},
        {"p": "Unscramble: TSAAEHSVLR", "a": "Salazar"},
        {"p": "Unscramble: EGONRD", "a": "Donger"}
    ],
    # Repeat similar 9 puzzles for other houses
}

# ---- House Pages ----
def house_page(house, bg_image):
    set_background(bg_image)
    st.title(f"🏰 {house} House")
    
    # Tabs for Quizzes, Puzzles
    tabs = st.tabs(["📝 Quizzes", "🧩 Puzzles"])
    
    # ---- Quizzes Tab ----
    with tabs[0]:
        st.subheader("Quizzes")
        for idx, q in enumerate(quizzes.get(house, [])):
            st.write(f"**Q{idx+1}: {q['q']}**")
            choice = st.radio(f"Select answer for Q{idx}", q['options'], key=f"{house}_quiz{idx}")
            if st.button(f"Submit Q{idx+1}", key=f"{house}_submit{idx}"):
                if choice == q['a']:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! Correct answer: {q['a']}")
    
    # ---- Puzzles Tab ----
    with tabs[1]:
        st.subheader("Puzzles")
        for idx, p in enumerate(puzzles.get(house, [])):
            st.write(f"Puzzle {idx+1}: {p['p']}")
            ans = st.text_input("Your Answer", key=f"{house}_puzzle{idx}")
            if st.button(f"Check Puzzle {idx+1}", key=f"{house}_check{idx}"):
                if ans.strip().lower() == p['a'].lower():
                    st.success("🎉 Correct!")
                else:
                    st.error(f"❌ Try Again! Answer: {p['a']}")

# ---- Home Page ----
def home():
    st.title("⚡ Welcome to WizardVerse AI ⚡")
    st.subheader("Choose your Hogwarts House 🧙‍♂️")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🦁 Gryffindor"):
            st.session_state["page"] = "Gryffindor"
    with col2:
        if st.button("🦡 Hufflepuff"):
            st.session_state["page"] = "Hufflepuff"
    with col3:
        if st.button("🦅 Ravenclaw"):
            st.session_state["page"] = "Ravenclaw"
    with col4:
        if st.button("🐍 Slytherin"):
            st.session_state["page"] = "Slytherin"

# ---- Navigation ----
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Background images mapping
bg_images = {
    "Gryffindor": "assets/gryffindor_bg.jpg",
    "Hufflepuff": "assets/hufflepuff_bg.jpg",
    "Ravenclaw": "assets/ravenclaw_bg.jpg",
    "Slytherin": "assets/slytherin_bg.jpg"
}

if st.session_state["page"] == "Home":
    set_background("assets/Hogwarts.jpg")
    home()
else:
    house_page(st.session_state["page"], bg_images[st.session_state["page"]])
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"


