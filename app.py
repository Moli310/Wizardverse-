import streamlit as st
import base64
from pathlib import Path

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Helper function to set background ----
def set_background(image_path: str):
    """Encodes and sets a local image as Streamlit background."""
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

# ---- Home Page ----
def home():
    st.title("⚡ Welcome to WizardVerse AI ⚡")
    st.subheader("Choose your Hogwarts House to begin your magical journey 🧙‍♂️")
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

# ---- House Pages ----
def gryffindor_page():
    set_background("assets/gryffindor_bg.jpg")
    st.title("🦁 Gryffindor House")
    st.write("Bravery, daring, nerve, and chivalry define a Gryffindor!")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")
    st.write("🚧 Coming soon... magical features await!")

def hufflepuff_page():
    set_background("assets/hufflepuff_bg.jpg")
    st.title("🦡 Hufflepuff House")
    st.write("Loyalty, patience, and hard work make you shine!")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")
    st.write("🚧 Coming soon... magical features await!")

def ravenclaw_page():
    set_background("assets/ravenclaw_bg.jpg")
    st.title("🦅 Ravenclaw House")
    st.write("Wit, wisdom, and learning light your way.")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")
    st.write("🚧 Coming soon... magical features await!")

def slytherin_page():
    set_background("assets/serpent_bg.jpg")
    st.title("🐍 Slytherin House")
    st.write("Ambition, cunning, and resourcefulness guide you.")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")
    st.write("🚧 Coming soon... magical features await!")

# ---- Navigation Logic ----
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if st.session_state["page"] == "Home":
    home()
elif st.session_state["page"] == "Gryffindor":
    gryffindor_page()
elif st.session_state["page"] == "Hufflepuff":
    hufflepuff_page()
elif st.session_state["page"] == "Ravenclaw":
    ravenclaw_page()
elif st.session_state["page"] == "Slytherin":
    slytherin_page()

# ---- Back button ----
if st.session_state["page"] != "Home":
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"


