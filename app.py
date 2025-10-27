import os
import pandas as pd
import streamlit as st
import time

# 🎩 Basic page setup
st.set_page_config(
    page_title="WizardVerse AI 🧙‍♂️",
    page_icon="🪄",
    layout="wide"
)

# ✨ Hogwarts header
st.markdown(
    """
    <div style="text-align:center; font-family: 'Garamond'; font-size:40px; color:#d4af37;">
        <b>⚡ WizardVerse AI ⚡</b><br>
        <span style="font-size:20px; color:#e6e6fa;">
        Explore the magic of Harry Potter — books, movies & fandom!
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# 🗂️ Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🧠 Safe data loader
@st.cache_data
def load_data():
    try:
        dialogues_path = os.path.join(BASE_DIR, "movies", "Dialogue.csv")
        spells_path = os.path.join(BASE_DIR, "movies", "Spells.csv")

        dialogues = pd.read_csv(dialogues_path, encoding="latin-1")
        spells = pd.read_csv(spells_path, encoding="latin-1")

        return dialogues, spells

    except FileNotFoundError as e:
        st.error("🪶 Oops! A magical scroll (CSV) has gone missing in Hogwarts’ archives.")
        st.info("Make sure your `movies/` folder and CSV files are uploaded to GitHub or present locally.")
        st.code(str(e))
        return None, None

# 🖼️ Background function
def set_background(image_file):
    if os.path.exists(image_file):
        import base64
        with open(image_file, "rb") as img:
            b64 = base64.b64encode(img.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{b64}");
                background-size: cover;
                background-attachment: fixed;
                color: #fff;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# 🧙 Load data
dialogues, spells = load_data()

# ✅ Continue only if data loaded
if dialogues is not None and spells is not None:
    st.success("✅ Magical datasets loaded successfully!")

    # Show preview
    with st.expander("📜 View a glimpse of the Wizarding dialogues"):
        st.dataframe(dialogues.head(10))

    with st.expander("✨ View spells and charms"):
        st.dataframe(spells.head(10))

    st.markdown("---")
    st.markdown(
        "<h3 style='color:#ffd700;'>🏰 Ready to enter the House Quiz Chamber?</h3>",
        unsafe_allow_html=True
    )

    # ---------------- House Quiz Section ----------------
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.score = 0
        st.session_state.q_index = 0

    # Select House
    house = st.radio(
        "Choose your House to start your magical journey:",
        ["Gryffindor 🦁", "Slytherin 🐍", "Ravenclaw 🦅", "Hufflepuff 🦡"]
    )

    # Set background for house
    bg_map = {
        "Gryffindor 🦁": "assets/gryffindor_bg.jpg",
        "Slytherin 🐍": "assets/slytherin_bg.jpg",
        "Ravenclaw 🦅": "assets/ravenclaw_bg.jpg",
        "Hufflepuff 🦡": "assets/hufflepuff_bg.jpg"
    }
    set_background(bg_map.get(house, ""))

    st.markdown(
        f"<div style='font-size:20px; color:#e6e6fa;'>Welcome to the {house} challenge! ⚔️</div>",
        unsafe_allow_html=True
    )

    # House quizzes
    house_quizzes = {
        "Gryffindor 🦁": [
            {"q": "What object must be caught to end a Quidditch match?", "a": "Golden Snitch"},
            {"q": "Who destroyed the last Horcrux?", "a": "Neville Longbottom"},
            {"q": "Which spell disarms an opponent?", "a": "Expelliarmus"},
        ],
        "Slytherin 🐍": [
            {"q": "What is the emblematic animal of Slytherin?", "a": "Serpent"},
            {"q": "Who was the true heir of Slytherin?", "a": "Tom Riddle"},
            {"q": "What potion allows you to change appearance?", "a": "Polyjuice Potion"},
        ],
        "Ravenclaw 🦅": [
            {"q": "What is Ravenclaw’s prized trait?", "a": "Intelligence"},
            {"q": "Who is the founder of Ravenclaw?", "a": "Rowena Ravenclaw"},
            {"q": "What is the color of Ravenclaw’s emblem?", "a": "Blue"},
        ],
        "Hufflepuff 🦡": [
            {"q": "What is Hufflepuff’s defining quality?", "a": "Loyalty"},
            {"q": "Who founded Hufflepuff House?", "a": "Helga Hufflepuff"},
            {"q": "Which magical creature is featured on the Hufflepuff crest?", "a": "Badger"},
        ]
    }

    # Quiz Logic
    if not st.session_state.quiz_started:
        if st.button("✨ Begin Quiz"):
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.experimental_rerun()
    else:
        questions = house_quizzes[house]
        idx = st.session_state.q_index
        score = st.session_state.score

        if idx < len(questions):
            q = questions[idx]
            st.markdown(f"<b>Q{idx+1}: {q['q']}</b>", unsafe_allow_html=True)
            answer = st.text_input("💬 Your answer:", key=f"ans_{idx}")

            if st.button("🪶 Submit Answer"):
                if answer.strip().lower() == q['a'].lower():
                    st.success("✨ Correct! Ten points to your House!")
                    st.session_state.score += 10
                else:
                    st.error(f"❌ Incorrect! Correct answer: {q['a']}")
                st.session_state.q_index += 1
                time.sleep(1)
                st.experimental_rerun()
        else:
            st.balloons()
            st.markdown(f"<h4>🏆 Quiz complete! Your score: {score}/{len(questions)*10}</h4>", unsafe_allow_html=True)
            if st.button("🔁 Try Another House"):
                st.session_state.quiz_started = False
                st.session_state.score = 0
                st.session_state.q_index = 0
                st.experimental_rerun()

else:
    st.warning("🧹 Waiting for the datasets to be restored before continuing the adventure.")
