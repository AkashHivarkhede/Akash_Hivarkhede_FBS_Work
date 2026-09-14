# Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.


import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["int", "string", "bool", "float"],
        "answer": "bool"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["get()", "input()", "read()", "scan()"],
        "answer": "input()"
    }
]


current_question = 0
score = 0


def show_question():

    question_label.config(
        text=questions[current_question]["question"]
    )

    for i in range(4):
        option_buttons[i].config(
            text=questions[current_question]["options"][i],
            state="normal"
        )

    feedback_label.config(text="")

def check_answer(selected_answer):

    global current_question
    global score

    correct_answer = questions[current_question]["answer"]

    if selected_answer == correct_answer:
        score += 1
        feedback_label.config(
            text="Correct Answer!"
        )
    else:
        feedback_label.config(
            text="Incorrect Answer!"
        )

    for button in option_buttons:
        button.config(state="disabled")

    next_button.config(state="normal")


# Next question
def next_question():

    global current_question

    current_question += 1

    if current_question < len(questions):
        show_question()
        next_button.config(state="disabled")

    else:
        messagebox.showinfo(
            "Quiz Completed",
            f"Quiz Completed!\nYour Score: {score}/{len(questions)}"
        )

        root.destroy()


root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x450")


# Title
title_label = tk.Label(
    root,
    text="Python Quiz",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)


# Question
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=450
)
question_label.pack(pady=20)


option_buttons = []

for i in range(4):

    button = tk.Button(
        root,
        text="",
        width=30,
        command=lambda i=i: check_answer(
            questions[current_question]["options"][i]
        )
    )

    button.pack(pady=5)

    option_buttons.append(button)


feedback_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold")
)
feedback_label.pack(pady=15)


next_button = tk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_button.pack(pady=10)


show_question()


root.mainloop()