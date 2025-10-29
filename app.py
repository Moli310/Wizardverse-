import streamlit as st
from pathlib import Path
import base64

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Google Font for Harry Potter style 
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

# ---- Background Function with Overlay ----
def set_background(image_path: str):
    file_path = Path(image_path)
    if not file_path.exists():
        st.warning(f"⚠️ Background image not found: {file_path}")
        return
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: relative;
        }}
        .overlay {{
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: rgba(0,0,0,0.5); /* semi-transparent black overlay */
            z-index: 0;
        }}
        .stApp > .main {{
            position: relative;
            z-index: 1;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

# ---- Quiz & Puzzle Data (9 each) ----
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
    "Hufflepuff": [
        {"q": "Who founded Hufflepuff?", "a": "Helga", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Hufflepuff emblem?", "a": "Badger", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Hufflepuff ghost?", "a": "Fat Friar", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Hufflepuff values?", "a": "Loyalty", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Hufflepuff colors?", "a": "Yellow and Black", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Hufflepuff?", "a": "Cedric Diggory", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Hufflepuff common room location?", "a": "Near kitchens", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for hard work?", "a": "Hufflepuff", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Hufflepuff founder valued?", "a": "Fairness", "options": ["Courage", "Fairness", "Wisdom", "Ambition"]}
    ],
    "Ravenclaw": [
        {"q": "Who founded Ravenclaw?", "a": "Rowena", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Ravenclaw emblem?", "a": "Eagle", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Ravenclaw ghost?", "a": "Grey Lady", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Ravenclaw values?", "a": "Wisdom", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Ravenclaw colors?", "a": "Blue and Silver", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Ravenclaw?", "a": "Luna Lovegood", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Ravenclaw common room?", "a": "Tower", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for intelligence?", "a": "Ravenclaw", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Ravenclaw founder valued?", "a": "Learning", "options": ["Courage", "Fairness", "Learning", "Ambition"]}
    ],
    "Slytherin": [
        {"q": "Who founded Slytherin?", "a": "Salazar", "options": ["Godric", "Helga", "Rowena", "Salazar"]},
        {"q": "Slytherin emblem?", "a": "Snake", "options": ["Lion", "Badger", "Eagle", "Snake"]},
        {"q": "Slytherin ghost?", "a": "Bloody Baron", "options": ["Nearly Headless Nick", "Fat Friar", "Grey Lady", "Bloody Baron"]},
        {"q": "Slytherin values?", "a": "Ambition", "options": ["Courage", "Loyalty", "Wisdom", "Ambition"]},
        {"q": "Slytherin colors?", "a": "Green and Silver", "options": ["Red and Gold", "Yellow and Black", "Blue and Silver", "Green and Silver"]},
        {"q": "Famous Slytherin?", "a": "Draco Malfoy", "options": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"]},
        {"q": "Slytherin common room?", "a": "Dungeon", "options": ["Tower", "Near kitchens", "Library", "Dungeon"]},
        {"q": "House known for cunning?", "a": "Slytherin", "options": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]},
        {"q": "Slytherin founder valued?", "a": "Resourcefulness", "options": ["Courage", "Fairness", "Learning", "Resourcefulness"]}
    ]
}

# ---- Puzzle Data (9 each) ----
puzzles = {
    "Gryffindor": [
        {"p": "Unscramble: DRCIGO", "a": "Godric"},
        {"p": "Unscramble: NOIL", "a": "Lion"},
        {"p": "Unscramble: YRAEGFHCIDRNO", "a": "Gryffindor"},
        {"p": "Unscramble: KNHECYCEEEDHL", "a": "Nearly Headless Nick"},
        {"p": "Unscramble: EVRCOAUG", "a": "Courage"},
        {"p": "Unscramble: HPRTA YTOPTER", "a": "Harry Potter"},
        {"p": "Unscramble: RSDOW", "a": "Sword"},
        {"p": "Unscramble: LDERA", "a": "Dare"},
        {"p": "Unscramble: CLBRAG", "a": "Garlic"}
    ],
    "Hufflepuff": [
        {"p": "Unscramble: HELGA", "a": "Helga"},
        {"p": "Unscramble: DABGER", "a": "Badger"},
        {"p": "Unscramble: LUFHPUFCF", "a": "Hufflepuff"},
        {"p": "Unscramble: TYLOAL", "a": "Loyalty"},
        {"p": "Unscramble: KCEEDRVCI", "a": "Cedric"},
        {"p": "Unscramble: SKCIREH", "a": "Kitchens"},
        {"p": "Unscramble: ARFNEIS", "a": "Fairness"},
        {"p": "Unscramble: DHPFCLFU", "a": "Hufflepuff"},
        {"p": "Unscramble: WORKHD", "a": "Hardwork"}
    ],
    "Ravenclaw": [
        {"p": "Unscramble: ROWENA", "a": "Rowena"},
        {"p": "Unscramble: EAGLE", "a": "Eagle"},
        {"p": "Unscramble: RAVNCLAW", "a": "Ravenclaw"},
        {"p": "Unscramble: YSIDOMW", "a": "Wisdom"},
        {"p": "Unscramble: LNAUERIG", "a": "Learning"},
        {"p": "Unscramble: LUNA LOVEGOOD", "a": "Luna Lovegood"},
        {"p": "Unscramble: TOWER", "a": "Tower"},
        {"p": "Unscramble: NIBRAE", "a": "Brain"},
        {"p": "Unscramble: LEARN", "a": "Learn"}
    ],
    "Slytherin": [
        {"p": "Unscramble: SALAZAR", "a": "Salazar"},
        {"p": "Unscramble: SNAKE", "a": "Snake"},
        {"p": "Unscramble: BLOODY BARON", "a": "Bloody Baron"},
        {"p": "Unscramble: BMCNUI", "a": "Cunning"},
        {"p": "Unscramble: RESROUCE", "a": "Resource"},
        {"p": "Unscramble: MALFOY", "a": "Malfoy"},
        {"p": "Unscramble: DUNGEON", "a": "Dungeon"},
        {"p": "Unscramble: GREEN", "a": "Green"},
        {"p": "Unscramble: SILVER", "a": "Silver"}
    ]
}

# ---- House Page Function ----
def house_page(house_name, bg_image):
    set_background(f"assets/{bg_image}")
    st.markdown(f"<h1 class='hp-font'>{house_name} House</h1>", unsafe_allow_html=True)
    color = house_colors[house_name]
    
    tabs = st.tabs(["Quizzes", "Puzzles"])
    
    # Quizzes
    with tabs[0]:
        for i, q in enumerate(quizzes[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {q['q']}</p>", unsafe_allow_html=True)
            st.radio("", q["options"], key=f"{house_name}_quiz{i}")
    
    # Puzzles
    with tabs[1]:
        for i, p in enumerate(puzzles[house_name]):
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{i+1}. {p['p']}</p>", unsafe_allow_html=True)
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

