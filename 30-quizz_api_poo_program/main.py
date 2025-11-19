from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

# Create a list to store all Question objects
question_bank = []
for question in question_data:
    # Extract question text and correct answer from the data
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Create a new Question object and add it to the list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create the quiz logic controller
quiz = QuizBrain(question_bank)

# Start the user interface and pass the QuizBrain instance
quizz_interface = QuizzInterface(quiz)

# This part only runs after the UI mainloop finishes
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
