class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns a boolean if there are still more questions in the question bank left to answer or not"""
        question_size = len(self.question_list) - 1
        return self.question_number <= question_size
    def check_answer(self, user_answer, correct_answer):
        """Checks if the user's response is the same as the answer"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        """Retrieve the item at the current question_number from the question_list."""
        # use input function to show the user the question text and ask for the user's answer
        question_text = self.question_list[self.question_number]
        if self.question_number < len(self.question_list):
            self.question_number += 1
            user_answer = input(f"Q{self.question_number}: {question_text.text} (True/False): ")
            self.check_answer(user_answer, question_text.answer)

# TODO 1: asking the questions
# TODO2: checking if the answer was correct
# TODO3: checking if we are at the end of the quiz
