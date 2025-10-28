import streamlit as st
import base64
from pathlib import Path

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Helper: Background with overlay and smaller image scaling ----
def set_background(image_path: str):
    """Encodes and sets a local image as Streamlit background with subtle dark overlay."""
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
            background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                              url("data:image/jpeg;base64,{encoded}");
            background-size: contain;  /* 👈 makes image smaller */
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
    st.title("⚡ WizardVerse AI ⚡")
    st.subheader("Explore the magic of Harry Potter — choose your House to begin your adventure!")

    # Show front image (your uploaded one)
    front_img = "assets/Hogwarts"  # rename the uploaded image to this
    if Path(front_img).exists():
        st.image(front_img, use_container_width=True)

    st.write("---")
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

    if st.button("✨ Enter Quiz"):
        st.session_state["page"] = "Quiz"

    st.write("🚧 Coming soon... magical features await!")
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"

def hufflepuff_page():
    set_background("assets/hufflepuff_bg.jpg")
    st.title("🦡 Hufflepuff House")
    st.write("Loyalty, patience, and hard work make you shine!")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")

    if st.button("✨ Enter Quiz"):
        st.session_state["page"] = "Quiz"

    st.write("🚧 Coming soon... magical features await!")
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"

def ravenclaw_page():
    set_background("assets/ravenclaw_bg.jpg")
    st.title("🦅 Ravenclaw House")
    st.write("Wit, wisdom, and learning light your way.")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")

    if st.button("✨ Enter Quiz"):
        st.session_state["page"] = "Quiz"

    st.write("🚧 Coming soon... magical features await!")
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"

def slytherin_page():
    set_background("assets/serpent_bg.jpg")
    st.title("🐍 Slytherin House")
    st.write("Ambition, cunning, and resourcefulness guide you.")
    st.subheader("✨ Quizzes | 🧩 Puzzles | 🪄 Spells")

    if st.button("✨ Enter Quiz"):
        st.session_state["page"] = "Quiz"

    st.write("🚧 Coming soon... magical features await!")
    if st.button("⬅️ Back to Houses"):
        st.session_state["page"] = "Home"

# ---- Quiz Placeholder ----
def quiz_page():
    st.title("🪄 Wizarding Quiz Chamber")
    st.write("Answer a few questions to test your magical knowledge!")
    st.markdown("🚧 *Quiz content coming soon...*")

    if st.button("⬅️ Back to House"):
        st.session_state["page"] = "Home"

# ---- Page Routing ----
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

pages = {
    "Home": home,
    "Gryffindor": gryffindor_page,
    "Hufflepuff": hufflepuff_page,
    "Ravenclaw": ravenclaw_page,
    "Slytherin": slytherin_page,
    "Quiz": quiz_page,
}

pages[st.session_state["page"]]()


