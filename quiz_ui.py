from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from question_main import *

class gui_interface:
    def __init__(self,quiz123:question_main):
        self.quiz = quiz123
        self.window=Tk()
        self.window.title("QUIZ APPLICATION")
        self.window.geometry("850x350")
        self.show_title()

        
        

        self.canvas=Canvas(width=800,height=300)
        self.question_text = self.canvas.create_text(400, 50,
                                                     text="Question here",
                                                     width=680,
                                                     fill="orange",
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.userdata=StringVar( )

        
       # next button
        self.nextbtn=Button(text="NEXT", width=10, bg="green",fg="white", command=self.next_btn)
        self.nextbtn.place(x=700,y=250)

        # quit button
        self.nextbtn=Button(text="QUIT",width=10, bg="red", fg="white",command=self.window.destroy, )
        self.nextbtn.place(x=100,y=250)

        #answer label
        self.templabel=Label(self.window,text="", pady=10, font=("ariel", 15, "bold"))
        self.templabel.place(x=350,y=250)
        self.options=None

        #q_no indication
        self.q_label=Label(self.window, text="1/10" ,font=('ariel',10,"bold"))
        self.q_label.place(x=700,y=50)
                                                   
        self.options=self.radio_btn()
        self.question_write()
        
        self.window.mainloop()

    def question_write(self)    :
       

        self.canvas.itemconfig(self.question_text, text=self.quiz.question_txt())
       
        self.show_choices()

       

    def next_btn(self):
        self.q_label["text"] = self.quiz.current_question+2 
        if self.quiz.check_answer(self.userdata.get()):
            self.templabel["fg"] = "green"
            self.templabel["text"] = 'Correct answer! \U0001F44D'
            self.question_write()
            self.show_choices()
            
        elif self.quiz.current_question<10:
            self.templabel["fg"] ="red"
            self.templabel["text"]= 'Ans:'+self.quiz.correct+'\n\u274E wrong answer '
            self.question_write()
            self.show_choices()
        else:
        
         self.quiz.showscore()
         self.window.destroy()
       

    def show_title(self):
        title=Label(self.window, text="QUIZ APP",fg="white",bg="black",width=50, font=("ariel", 20, "bold"))    
        title.place(x=0,y=2)

    def radio_btn(self):
       
        choice_list=[]
        pos=160
       
        while len(choice_list)<4 :
            radio_b=Radiobutton(self.window,text='', variable=self.userdata , value='',font=("ariel", 10, "bold"))
            radio_b.place( x=300, y=pos)
            choice_list.append(radio_b)
            pos+=20
        self.userdata.set(None)
        return choice_list
    

    def show_choices(self):
               self.userdata.set(None)
               val=0
               for option in self.quiz.radio_option():
                self.options[val]["text"]=option 
                self.options[val]["value"]=option
                val+=1
               


     
       
