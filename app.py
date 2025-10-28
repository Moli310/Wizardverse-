import streamlit as st
from pathlib import Path
import base64
import pandas as pd

# ---- Page Config ----
st.set_page_config(page_title="WizardVerse AI", layout="wide")

# ---- Helper Functions ----
def set_background(image_path):
    file_path = Path(image_path)
    if not file_path.exists():
        st.warning(f"⚠ Image {image_path} not found!")
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
            filter: brightness(0.8);
        }}
        </style>
        """, unsafe_allow_html=True
    )

def front_page():
    set_background("assets/hogwarts.jpg")
    st.markdown("<h1 style='text-align:center;color:white;'>🏰 Welcome to WizardVerse AI 🪄</h1>", unsafe_allow_html=True)

    # House selection with images
    col1, col2, col3, col4 = st.columns(4)
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    for col, house in zip([col1, col2, col3, col4], houses):
        with col:
            if st.button(f"{house}"):
                st.session_state['house'] = house
            st.image(f"assets/{house.lower()}.png", use_column_width=True)

def house_page(house):
    set_background(f"assets/{house.lower()}.jpg")
    st.markdown(f"<h1 style='text-align:center;color:white;'>{house} House 🏰</h1>", unsafe_allow_html=True)

    # Navigation
    if st.button("⬅ Back to Hogwarts"):
        st.session_state['house'] = None

    # --- Dataset-driven Quizzes ---
    st.subheader("📝 Quizzes")
    quiz_df = pd.read_csv(f"datasets/{house.lower()}_quiz.csv")  # Example CSV: columns = question, option1..4, answer
    for idx, row in quiz_df.iterrows():
        st.write(f"**Q{idx+1}: {row['question']}**")
        options = [row['option1'], row['option2'], row['option3'], row['option4']]
        ans = st.radio(f"Select answer for Q{idx+1}", options, key=f"quiz{idx}")
        if st.button(f"Submit Q{idx+1}", key=f"submit{idx}"):
            if ans == row['answer']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct answer: {row['answer']}")

    # --- Dataset-driven Puzzles ---
    st.subheader("🧩 Puzzles")
    puzzle_df = pd.read_csv(f"datasets/{house.lower()}_puzzles.csv")  # Example: columns = puzzle, answer
    for idx, row in puzzle_df.iterrows():
        st.write(f"Puzzle {idx+1}: {row['puzzle']}")
        user_ans = st.text_input("Your Answer", key=f"puzzle{idx}")
        if st.button(f"Check Puzzle {idx+1}", key=f"check{idx}"):
            if user_ans.strip().lower() == row['answer'].lower():
                st.success("🎉 Correct!")
            else:
                st.error(f"❌ Try Again! Answer: {row['answer']}")

    # --- Spells ---
    st.subheader("🪄 Spells")
    spells_df = pd.read_csv("datasets/spells.csv")  # columns = spell, effect
    spell_choice = st.selectbox("Choose a spell", spells_df['spell'])
    if st.button("Cast Spell"):
        effect = spells_df[spells_df['spell'] == spell_choice]['effect'].values[0]
        st.info(f"{spell_choice} spell casted! ✨ Effect: {effect}")

# ---- Main App Logic ----
if 'house' not in st.session_state:
    st.session_state['house'] = None

if st.session_state['house'] is None:
    front_page()
else:
    house_page(st.session_state['house'])


