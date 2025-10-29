import streamlit as st
from pathlib import Path
import base64

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Helper Functions ----
def set_background(image_path):
    """Set a full-page background image."""
    if not Path(image_path).exists():
        st.warning(f"⚠ Image {image_path} not found!")
        return
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            filter: brightness(0.8);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---- Front Page ----
def front_page():
    set_background("assets/Hogwarts.jpg")
    st.markdown("<h1 style='text-align:center;color:white;'>🏰 Welcome to WizardVerse AI 🪄</h1>", unsafe_allow_html=True)

    # House selection
    col1, col2, col3, col4 = st.columns(4)
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    for col, house in zip([col1, col2, col3, col4], houses):
        with col:
            if st.button(house):
                st.session_state['house'] = house
            # House icons
            icon_path = f"assets/{house.lower()}.png"
            if Path(icon_path).exists():
                st.image(icon_path, use_container_width=True)
            else:
                st.write(f"Icon missing: {house}")

# ---- House Page ----
def house_page(house):
    set_background(f"assets/{house.lower()}_bg.jpg")
    st.markdown(f"<h1 style='text-align:center;color:white;'>{house} House 🏰</h1>", unsafe_allow_html=True)

    if st.button("⬅ Back to Hogwarts"):
        st.session_state['house'] = None

    # Simple Quiz
    st.subheader("📝 Quiz")
    question = f"Who founded {house}?"
    answers = {
        "Gryffindor": "Godric",
        "Hufflepuff": "Helga",
        "Ravenclaw": "Rowena",
        "Slytherin": "Salazar"
    }
    choice = st.radio(question, list(answers.values()))
    if st.button("Submit Answer"):
        if choice == answers[house]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! Correct answer: {answers[house]}")

    # Simple Puzzle
    st.subheader("🧩 Puzzle")
    scrambled = "".join(reversed(house))
    st.write(f"Unscramble the house name: {scrambled}")
    answer = st.text_input("Your Answer")
    if st.button("Check Puzzle"):
        if answer.strip().lower() == house.lower():
            st.success("🎉 Correct!")
        else:
            st.error("❌ Try Again!")

# ---- Main ----
if 'house' not in st.session_state:
    st.session_state['house'] = None

if st.session_state['house'] is None:
    front_page()
else:
    house_page(st.session_state['house'])


