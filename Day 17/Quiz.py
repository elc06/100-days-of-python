# Creating a question class
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_have_questions_remaining():
    quiz.next_question()

print(f"You've completed the quiz. Your final score was: {quiz.user_score}/{len(question_bank)}")