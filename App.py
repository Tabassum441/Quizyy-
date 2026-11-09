import streamlit as st

st.set_page_config(page_title="Quizyy", page_icon="🎀")

st.title("🎀 Welcome to Quizyy!")
st.subheader("Test Your Brain, Have Fun!")

name = st.text_input("Enter your name:")

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Who created Python?",
        "options": [
            "James Gosling",
            "Guido van Rossum",
            "Dennis Ritchie",
            "Mark Zuckerberg"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is 5 + 5?",
        "options": ["8", "9", "10", "11"],
        "answer": "10"
    }
]

with st.form("quiz_form"):
    answers = []

    for i, q in enumerate(questions):
        st.write(f"Q{i+1}. {q['question']}")
        choice = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"q{i}"
        )
        answers.append(choice)

    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    if not name.strip():
        st.warning("Please enter your name!")
    else:
        score = sum(
            answers[i] == questions[i]["answer"]
            for i in range(len(questions))
        )

        st.success(f"Well done, {name}!")
        st.write(f"Your score: {score}/3")

        if score == 3:
            st.balloons()
            st.write("Excellent! 🌟")
        elif score == 2:
            st.write("Great job! 💗")
        else:
            st.write("Keep practising! 🌸")
