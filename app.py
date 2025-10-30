import streamlit as st
from pathlib import Path
import base64

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Google Font for Harry Potter style ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
<style>
.hp-font { font-family: 'Creepster', cursive; color: gold; text-shadow: 2px 2px 5px black; }
.sub-font { font-family: 'Creepster', cursive; color: white; }
</style>
""", unsafe_allow_html=True)

# ---- House Colors (adjusted for readability) ----
house_colors = {
    "Gryffindor": "#FFDD00",  # bright gold
    "Hufflepuff": "#000000",  # black
    "Ravenclaw": "#FFFFFF",   # white
    "Slytherin": "#FFFFFF"    # white
}

# ---- Background Function with overlay ----
def set_background(image_path):
    file_path = Path(image_path)
    if not file_path.exists():
        st.warning(f"⚠️ Background image not found: {file_path}")
        return
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                    url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# ---- Quiz & Puzzle Data (9 each) ----
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

puzzles = quizzes  # for simplicity, using same structure; you can replace with your puzzles

# ---- House Page Function ----
def house_page(house_name, bg_image):
    set_background(f"assets/{bg_image}")
    st.markdown(f"<h1 class='hp-font'>{house_name} House</h1>", unsafe_allow_html=True)
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

# ---- Home Page ----
def home():
    set_background("assets/Hogwarts.jpg")
    st.markdown("<h1 class='hp-font'>⚡ Welcome to WizardVerse AI ⚡</h1>", unsafe_allow_html=True)
    st.subheader("Choose your Hogwarts House to begin your magical journey 🧙‍♂️")
    
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("🦁 Gryffindor"): st.session_state["page"] = "Gryffindor"
    if col2.button("🦡 Hufflepuff"): st.session_state["page"] = "Hufflepuff"
    if col3.button("🦅 Ravenclaw"): st.session_state["page"] = "Ravenclaw"
    if col4.button("🐍 Slytherin"): st.session_state["page"] = "Slytherin"

# ---- Navigation ----
if "page" not in st.session_state: st.session_state["page"] = "Home"

if st.session_state["page"] == "Home": home()
elif st.session_state["page"] == "Gryffindor": house_page("Gryffindor", "gryffindor_bg.jpg")
elif st.session_state["page"] == "Hufflepuff": house_page("Hufflepuff", "hufflepuff_bg.jpg")
elif st.session_state["page"] == "Ravenclaw": house_page("Ravenclaw", "ravenclaw_bg.jpg")
elif st.session_state["page"] == "Slytherin": house_page("Slytherin", "serpent_bg.jpg")

# ---- Back Button ----
if st.session_state["page"] != "Home":
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"


