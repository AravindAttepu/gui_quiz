from quiz_data import question_bank
from question_main import question_main
from quiz_ui import gui_interface
from random import shuffle
import html

all_questions=[]


for questions in question_bank:
    choices=[]
    new_question=[]
    
    question =html.unescape(questions["question"])
    answer = html.unescape(questions["correct_answer"])
    incorrect_answers = questions["incorrect_answers"]
    new_question.append(question)
    new_question.append(answer)
  
    for incorrect in incorrect_answers:
        choices.append(incorrect)
    choices.append(answer)    
    shuffle(choices)
    new_question.append(choices)
    
   
    #all_questions.append(new_question)
    all_questions.append(new_question)
    
quiz=question_main(all_questions)  
quiz1=gui_interface(quiz)  





