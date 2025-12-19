from question_model import Question
from data import question_data
from quiz_brain import Quizbrain



question_bank=[]
for i in question_data[0]["results"]:
    question_text = i["question"]
    question_ans = i["correct_answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)


quiz=Quizbrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    
print(f'You completed the quiz')
print(f" Your final score was: {quiz.score}/{quiz.question_number}")