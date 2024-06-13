from question_model import Question
from data import get_response
def build_question_data():
    questions = []
    for question in get_response():
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        questions.append(new_question)
    return questions