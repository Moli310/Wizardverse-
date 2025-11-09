import streamlit as st
from pathlib import Path
import base64
import unicodedata

# -------- Helper: Find Asset --------
def find_asset(filename, folder="assets"):
    folder_path = Path(folder)
    if not folder_path.exists():
        return None
    target_norm = unicodedata.normalize("NFC", filename).casefold()
    for f in folder_path.iterdir():
        if unicodedata.normalize("NFC", f.name).casefold() == target_norm:
            return str(f)
    for f in folder_path.iterdir():
        if target_norm in unicodedata.normalize("NFC", f.name).casefold():
            return str(f)
    return None

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="WizardVerse AI — Hogwarts Edition",
    layout="wide",
    page_icon="🪄",
)

# ---------- Helper: Set Magical Background ----------
def set_background(image_path):
    p = Path(image_path)
    if not p.exists():
        st.warning(f"⚠️ Background image not found: {image_path}")
        return

    with open(p, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: scale(1.05); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}

    .stApp {{
        background:
            linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
            url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        animation: fadeIn 3s ease-in-out;
        transition: background 1s ease-in-out;
    }}

    </style>
    """, unsafe_allow_html=True)

set_background("assets/Hogwarts.jpg")

# ---------- Page Config ----------
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---------- Global Fonts ----------
st.markdown("""
<link href="https://fonts.cdnfonts.com/css/harry-p" rel="stylesheet">
<style>
html, body, [class*="css"] { font-family: 'Harry P', sans-serif; }
h1, h2, h3 { font-family: 'Harry P', sans-serif; letter-spacing: 2px; }
@keyframes glow {
  0% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
  50% { text-shadow: 0 0 20px #fff, 0 0 30px #ffd700; }
  100% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
}
h1 { animation: glow 2s ease-in-out infinite alternate; text-align:center; color:gold; }
</style>
""", unsafe_allow_html=True)

# ---------- House Colors ----------
house_colors = {
    "Gryffindor": "#FFD700",
    "Hufflepuff": "#000000",
    "Ravenclaw": "#C0C0FF",
    "Slytherin": "#C8E6C9"
}

# ---------- Quiz & Puzzle Data ----------
quizzes = {
    "Gryffindor": [
        {"q": "Who founded Gryffindor?", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "What is the Gryffindor emblem?", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Gryffindor common room is in?", "options": ["Tower", "Basement", "Library", "Dungeon"]},
        {"q": "Gryffindor ghost is?", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Gryffindor colors?", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "What is Gryffindor's sword made of?", "options": ["Silver", "Gold", "Bronze", "Iron"]},
        {"q": "Famous Gryffindor student?", "options": ["Harry Potter", "Draco Malfoy", "Luna Lovegood", "Cedric Diggory"]},
        {"q": "House known for bravery?", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Gryffindor founder valued?", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]}
    ],
    "Hufflepuff": [
        {"q": "Who founded Hufflepuff?", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Hufflepuff emblem?", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Hufflepuff ghost?", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Hufflepuff values?", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Hufflepuff colors?", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Hufflepuff?", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Hufflepuff common room location?", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for hard work?", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Hufflepuff founder valued?", "options": ["Courage", "Fairness", "Wisdom", "Ambition"]}
    ],
    "Ravenclaw": [
        {"q": "Who founded Ravenclaw?", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Ravenclaw emblem?", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Ravenclaw ghost?", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Ravenclaw values?", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Ravenclaw colors?", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Ravenclaw?", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Ravenclaw common room?", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for intelligence?", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Ravenclaw founder valued?", "options": ["Courage", "Fairness", "Learning", "Ambition"]}
    ],
    "Slytherin": [
        {"q": "Who founded Slytherin?", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Slytherin emblem?", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Slytherin ghost?", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Slytherin values?", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Slytherin colors?", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Slytherin?", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Slytherin common room?", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for cunning?", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Slytherin founder valued?", "options": ["Courage", "Fairness", "Learning", "Resourcefulness"]}
    ]
}

# ---------- Home Page ----------
def home():
    set_background("assets/𝐇𝐨𝐠𝐰𝐚𝐫𝐭𝐬.jpg")
    # Home page button style
    st.markdown("""
    <style>
    div.stButton > button {
        border-radius: 12px; border:2px solid transparent; color:white !important;
        font-weight:bold; padding:0.6em 1.2em; transition: all 0.3s ease-in-out;
        background-color: rgba(0,0,0,0.6);
    }
    div.stButton > button:hover { transform:scale(1.1); box-shadow:0 0 20px rgba(255,255,255,0.7); }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>⚡ Welcome to WizardVerse AI ⚡</h1>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    if col1.button(" Gryffindor"): st.session_state["page"] = "Gryffindor"
    if col2.button(" Hufflepuff"): st.session_state["page"] = "Hufflepuff"
    if col3.button(" Ravenclaw"): st.session_state["page"] = "Ravenclaw"
    if col4.button("Slytherin"): st.session_state["page"] = "Slytherin"

# ---------- House Page ----------
def house_page(house_name, bg_image):
    set_background(f"assets/{bg_image}")

    # House-specific button style
    color = house_colors.get(house_name, "white")
    st.markdown(f"""
    <style>
    div.stButton > button {{
        border-radius:12px; border:2px solid {color}; font-weight:bold;
        padding:0.6em 1.2em; background-color: rgba(0,0,0,0.6); color:white !important;
        box-shadow:0 0 10px {color};
        transition: all 0.3s ease-in-out;
    }}
    div.stButton > button:hover {{
        transform: scale(1.1); box-shadow: 0 0 25px {color}; color: {color} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<h1>{house_name} House</h1>", unsafe_allow_html=True)
    tabs = st.tabs(["Quizzes", "Puzzles"])

    with tabs[0]:
        for i, q in enumerate(quizzes[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {q['q']}</p>", unsafe_allow_html=True)
            st.radio("", q["options"], key=f"{house_name}_quiz{i}")

    with tabs[1]:
        for i, q in enumerate(quizzes[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {q['q']}</p>", unsafe_allow_html=True)
            st.text_input("", key=f"{house_name}_puzzle{i}")

# ---------- Navigation ----------
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if st.session_state["page"] == "Home":
    home()
elif st.session_state["page"] == "Gryffindor":
    house_page("Gryffindor", "gryffindor_bg.jpg")
elif st.session_state["page"] == "Hufflepuff":
    house_page("Hufflepuff", "hufflepuff_bg.jpg")
elif st.session_state["page"] == "Ravenclaw":
    house_page("Ravenclaw", "ravenclaw_bg.jpg")
elif st.session_state["page"] == "Slytherin":
    house_page("Slytherin", "serpent_bg.jpg")


# ---------- Back Button ----------
if st.session_state["page"] != "Home":
    if st.button("Back to Houses"):
        st.session_state["page"] = "Home"



