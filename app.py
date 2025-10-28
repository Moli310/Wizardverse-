import streamlit as st

st.set_page_config(page_title="WizardVerse: Hogwarts Adventure", layout="centered")

st.title("🏰 Welcome to Hogwarts!")
st.markdown("Choose your house to begin your magical journey ⚡")

# Initialize session state
if 'house' not in st.session_state:
    st.session_state['house'] = None

houses = {
    "🦁 Gryffindor": "Bravery, courage, and chivalry.",
    "🐍 Slytherin": "Cunning, ambition, and resourcefulness.",
    "🦅 Ravenclaw": "Wisdom, wit, and learning.",
    "🦡 Hufflepuff": "Loyalty, patience, and dedication."
}

# ---- HOME PAGE ----
if st.session_state['house'] is None:
    st.subheader("✨ Select your Hogwarts House ✨")

    col1, col2 = st.columns(2)
    for i, (house, desc) in enumerate(houses.items()):
        col = col1 if i % 2 == 0 else col2
        if col.button(house):
            st.session_state['house'] = house

# ---- HOUSE PAGE ----
else:
    house = st.session_state['house']
    st.success(f"You are now in {house}!")
    st.button("🏠 Go Back to Houses", on_click=lambda: st.session_state.update({'house': None}))

    tab1, tab2, tab3 = st.tabs(["🧠 Quiz", "🧩 Puzzle", "✨ Spells"])

    with tab1:
        st.header("House Quiz")
        q1 = st.radio("1️⃣ What spell is used to disarm an opponent?",
                      ["Expelliarmus", "Avada Kedavra", "Lumos"])
        q2 = st.radio("2️⃣ What platform do students use to board the Hogwarts Express?",
                      ["9¾", "7½", "10½"])
        if st.button("Submit Quiz"):
            score = 0
            if q1 == "Expelliarmus":
                score += 1
            if q2 == "9¾":
                score += 1
            st.success(f"Your score: {score}/2")

    with tab2:
        st.header("House Puzzle 🧩")
        st.write("Riddle: What has to be broken before you can use it?")
        answer = st.text_input("Your answer:")
        if st.button("Check Answer"):
            if answer.lower().strip() == "egg":
                st.success("Correct! 🥚")
            else:
                st.error("Try again!")

    with tab3:
        st.header("✨ Spell Book")
        st.write("- **Alohomora** – Unlocks doors.")
        st.write("- **Wingardium Leviosa** – Makes things levitate.")
        st.write("- **Expecto Patronum** – Summons a Patronus.")
        st.write("- **Lumos** – Lights up your wand tip.")

st.markdown("---")
st.caption("Made with 🪄 magic and Streamlit.")
