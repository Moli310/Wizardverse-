import streamlit as st
from pathlib import Path
import base64
import unicodedata

# ---------- Helper: Find Asset ----------
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

# ---------- Helper: Set Background ----------
def set_background(image_path):
    p = Path(image_path)
    if not p.exists():
        found = find_asset(p.name, p.parent)
        if found:
            p = Path(found)
        else:
            st.warning(f"⚠️ Background image not found: {image_path}")
            return
    with open(p, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background:
            linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
            url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------- Page Config ----------
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---------- Global Fonts & Styles ----------
st.markdown("""
<link href="https://fonts.cdnfonts.com/css/harry-p" rel="stylesheet">
<style>
html, body, [class*="css"] {
    font-family: 'Harry P', sans-serif;
}
h1, h2, h3 {
    font-family: 'Harry P', sans-serif;
    letter-spacing: 2px;
}

/* Title Glow */
@keyframes glow {
  0% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
  50% { text-shadow: 0 0 20px #fff, 0 0 30px #ffd700; }
  100% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
}
h1 {
  animation: glow 2s ease-in-out infinite alternate;
  text-align: center;
  color: gold;
}

/* Magical Buttons */
div.stButton > button {
    font-family: 'Harry P', sans-serif;
    border-radius: 12px;
    border: 2px solid transparent;
    color: white !important;
    font-weight: bold;
    padding: 0.6em 1.2em;
    transition: all 0.3s ease-in-out;
    background-color: rgba(0,0,0,0.6);
}

/* House Specific Glows */
div.stButton > button[data-house="Gryffindor"] {
    box-shadow: 0 0 10px #ff4500;
    border-color: #ff0000;
}
div.stButton > button[data-house="Gryffindor"]:hover {
    background-color: #ff0000;
    color: gold !important;
    box-shadow: 0 0 25px #ff4500;
    transform: scale(1.1);
}

div.stButton > button[data-house="Hufflepuff"] {
    box-shadow: 0 0 10px #ffdb00;
    border-color: #ffdb00;
}
div.stButton > button[data-house="Hufflepuff"]:hover {
    background-color: #ffdb00;
    color: black !important;
    box-shadow: 0 0 25px #ffdb00;
    transform: scale(1.1);
}

div.stButton > button[data-house="Ravenclaw"] {
    box-shadow: 0 0 10px #4169e1;
    border-color: #1e90ff;
}
div.stButton > button[data-house="Ravenclaw"]:hover {
    background-color: #1e90ff;
    color: white !important;
    box-shadow: 0 0 25px #87cefa;
    transform: scale(1.1);
}

div.stButton > button[data-house="Slytherin"] {
    box-shadow: 0 0 10px #2a

import streamlit as st
from pathlib import Path
import base64
import unicodedata

# ---------- Helper: Find Asset (handles Unicode filenames) ----------
def find_asset(filename, folder="assets"):
    folder_path = Path(folder)
    if not folder_path.exists():
        return None
    target_norm = unicodedata.normalize("NFC", filename).casefold()
    for f in folder_path.iterdir():
        if unicodedata.normalize("NFC", f.name).casefold() == target_norm:
            return str(f)
    # Try partial match
    for f in folder_path.iterdir():
        if target_norm in unicodedata.normalize("NFC", f.name).casefold():
            return str(f)
    return None

# ---------- Helper: Set Background ----------
def set_background(image_path):
    p = Path(image_path)
    if not p.exists():
        found = find_asset(p.name, p.parent)
        if found:
            p = Path(found)
        else:
            st.warning(f"⚠️ Background image not found: {image_path}")
            return
    with open(p, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background: 
            linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
            url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------- Page Config ----------
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---------- Global Fonts, Effects, and Magic Style ----------
st.markdown("""
<link href="https://fonts.cdnfonts.com/css/harry-p" rel="stylesheet">
<style>
html, body, [class*="css"] {
    font-family: 'Harry P', sans-serif;
}
h1, h2, h3 {
    font-family: 'Harry P', sans-serif;
    letter-spacing: 2px;
}

/* Title Glow */
@keyframes glow {
  0% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
  50% { text-shadow: 0 0 20px #fff, 0 0 30px #ffd700; }
  100% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffa500; }
}
h1 {
  animation: glow 2s ease-in-out infinite alternate;
  text-align: center;
  color: gold;
}

/* Magical Buttons */
div.stButton > button {
    border-radius: 12px;
    border: 2px solid transparent;
    color: white !important;
    font-weight: bold;
    padding: 0.6em 1.2em;
    transition: all 0.3s ease-in-out;
    background-color: rgba(0,0,0,0.6);
}
div.stButton > button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 20px rgba(255,255,255,0.7);
}

/* House Glow */
div.stButton > button:has(span:contains("Gryffindor")) {border-color: #ae0001; box-shadow: 0 0 10px #ae0001;}
div.stButton > button:has(span:contains("Hufflepuff")) {border-color: #ffdb00; box-shadow: 0 0 10px #ffdb00;}
div.stButton > button:has(span:contains("Ravenclaw")) {border-color: #0e1a40; box-shadow: 0 0 10px #0e1a40;}
div.stButton > button:has(span:contains("Slytherin")) {border-color: #2a623d; box-shadow: 0 0 10px #2a623d;}
</style>
""", unsafe_allow_html=True)

# ---------- House Colors ----------
house_colors = {
    "Gryffindor": "#FFDD00",
    "Hufflepuff": "#000000",
    "Ravenclaw": "#FFFFFF",
    "Slytherin": "#FFFFFF"
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
puzzles = quizzes

# ---------- House Page ----------
def house_page(house_name, bg_image):
    set_background(f"assets/{bg_image}")
    st.markdown(f"<h1>{house_name} House</h1>", unsafe_allow_html=True)
    color = house_colors[house_name]
    tabs = st.tabs(["Quizzes", "Puzzles"])

    with tabs[0]:
        for i, q in enumerate(quizzes[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {q['q']}</p>", unsafe_allow_html=True)
            st.radio("", q["options"], key=f"{house_name}_quiz{i}")
    with tabs[1]:
        for i, p in enumerate(puzzles[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {p['q']}</p>", unsafe_allow_html=True)
            st.text_input("", key=f"{house_name}_puzzle{i}")

# ---------- Home Page ----------
def home():
    set_background("assets/𝐇𝐨𝐠𝐰𝐚𝐫𝐭𝐬.jpg")
    st.markdown("""
        <h1>⚡ Welcome to WizardVerse AI ⚡</h1>
        <h3 style='text-align:center; color:#E0E0E0;'>Choose your Hogwarts House to begin your magical journey 🧙‍♂️</h3>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("🦁 Gryffindor"): st.session_state["page"] = "Gryffindor"
    if col2.button("🦡 Hufflepuff"): st.session_state["page"] = "Hufflepuff"
    if col3.button("🦅 Ravenclaw"): st.session_state["page"] = "Ravenclaw"
    if col4.button("🐍 Slytherin"): st.session_state["page"] = "Slytherin"

# ---------- Navigation ----------
if "page" not in st.session_state: st.session_state["page"] = "Home"

if st.session_state["page"] == "Home": home()
elif st.session_state["page"] == "Gryffindor": house_page("Gryffindor", "gryffindor_bg.jpg")
elif st.session_state["page"] == "Hufflepuff": house_page("Hufflepuff", "hufflepuff_bg.jpg")
elif st.session_state["page"] == "Ravenclaw": house_page("Ravenclaw", "ravenclaw_bg.jpg")
elif st.session_state["page"] == "Slytherin": house_page("Slytherin", "serpent_bg.jpg")

# ---------- Back Button ----------
if st.session_state["page"] != "Home":
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"

