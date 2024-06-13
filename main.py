from quiz_brain import QuizBrain
from ui import QuizInterface
from data_builder import build_question_data

question_bank = build_question_data()
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
