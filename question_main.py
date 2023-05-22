from tkinter import messagebox

class question_main:
    
    def __init__(self,questions):
        self.current_question=0
        self.score=0
        self.question_text=None
        self.questions=questions
        self.radio_option()
       
    def radio_option(self):
        return self.questions[self.current_question][2]
    def question_txt(self):
        if self.current_question<10:
         q_text=self.questions[self.current_question][0]
         return q_text
       


    def check_answer(self,answer):
      
        self.correct=self.questions[self.current_question][1]
      
        self.current_question+=1
        if self.correct==answer:
            self.score+=1
            
            return True
      
         

    def showscore(self):
        loss=self.current_question-self.score
       
        messagebox.showinfo("Result", f"correct:{self.score}\nwrong:\n{loss}")
        
        
            

    
        