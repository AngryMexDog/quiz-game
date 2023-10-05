#class Question:
#    def __init__(self, q_text, q_answer):
#        self.text = q_text
#        self.answer = q_answer

#new_q = Question("algo", "False")
#print(new_q.text)


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()