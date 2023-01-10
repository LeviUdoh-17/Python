from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
answer = ""
for lists in question_data:
    for text, answers in lists.items():
        if text == "question":
            question = answers
        elif text == "correct_answer":
            answer = answers
            question_bank.append(Question(question, answer))
        else:
            pass
quiz = QuizBrain(question_bank)
still_questions = quiz.still_has_questions()

while still_questions:
    quiz.next_question()
    still_questions = quiz.still_has_questions()
else:
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")