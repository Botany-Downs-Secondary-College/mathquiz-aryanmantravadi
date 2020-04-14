#Sprint6.py
#A.Mantravadi, March 2020

from tkinter import * #imports all modules of tool kit interface, * is called wildcard
from random import *
from tkinter import ttk

class MathQuiz: #OOP will have classews and functions will be part of classes
    #Keep your widgets in instantiate (__init__) method, each instance (object) must have self. as prefix
    def __init__(self, parent):

        """Widgets for frame 1"""
        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                text = "Welcome to Math Quiz", font=("times", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 3)
        self.name_label = Label(self.frame1, text="Name: ")
        self.name_label.grid(row = 2, column = 1)
        self.name = StringVar()
        self.name.set("")
        self.NameEntry = ttk.Entry(self.frame1, textvariable= self.name)
        self.NameEntry.grid(row = 3, column = 1)
        self.age_label = Label(self.frame1, text="Age: ")
        self.age_label.grid(row = 4, column = 1)
        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = ttk.Entry(self.frame1, textvariable= self.age)
        self.AgeEntry.grid(row = 5, column = 1)
        level_label = Label(self.frame1, text="Choose your difficulty: ")
        level_label.grid(row = 7, column = 1)
        
        self.warning = Label(self.frame1, text = "")
        self.warning.grid(row = 6, column = 1, columnspan = 3)
        
        self.radio_var = StringVar()
        self.radio_var.set(1)
        
        #Radio buttons with for loop for efficiency
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.difficulty_level = StringVar()
        self.difficulty_level.set(0)
        self.difficulty_buttons =[]

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.frame1, variable = self.difficulty_level, value = i, text = self.difficulty[i], anchor = W, padx =50, width = "10", height = "2")
            self.difficulty_buttons.append(rb)
            rb.grid(row = i+9, column = 1, sticky = W)

        #Button that calls frame2
        self.submit = Button(self.frame1, text = "Next", command = self.show_frame2)
        self.submit.grid(row = 14, column = 1)
        

        """Widgets for frame 2"""
        self.frame2 = Frame(parent) #notice grid() method is missing here

        self.questions = Label(self.frame2, bg= "black", fg = "white", width = 40, padx = 30, pady = 10,
                               text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(columnspan = 3)

        self.QuizLabel = Label(self.frame2, text="")
        self.QuizLabel.grid(row = 1, columnspan = 3, sticky = W)

        self.QuestionLabel = Label(self.frame2, text ="", width = 15, height = 3)#empty label to print questions
        self.QuestionLabel.grid(row = 2,column = 0, sticky = W)
        
        self.useranswer = IntVar()
        self.useranswer.set("")
        self.QuestionEntry = ttk.Entry(self.frame2, textvariable=self.useranswer)
        self.QuestionEntry.grid(row = 2, column = 1, sticky = W)

        self.feedback = Label(self.frame2, text = "Click Check answer button")
        self.feedback.grid(row = 3, column = 0, columnspan = 3)
        
        self.home = Button(self.frame2, text = "Home", anchor =W, command = self.show_frame1)
        self.home.grid(row = 4, column = 0)

        self.check = Button(self.frame2, text = "Check answer", anchor = W, command = self.check_answer)
        self.check.grid(row = 4, column = 1)

        self.next_btn = Button(self.frame2, text = "Next", width = 5, command = self.next_problem, relief = RIDGE)
        self.next_btn.grid(row = 4, column = 2)

     

        """Widgets for Report frame"""
        self.index = 0
        self.score = 0
        self.report_frame = Frame(parent, height = "450", width = "400")
        self.report_frame.grid_propagate(0)
        #creating labels for Report headings using 'for' loop
        report_page = ["Name", "Age", "Score"]
        self.report_labels = []
        

        for i in range(len(report_page)):
            lb = Label(self.report_frame, bg = "black", fg = "white", padx = 30, pady = 3, text = report_page[i], anchor = W, width = "7", height = "2", font = ("Times", "22", "bold"))
            self.report_labels.append(lb)
            lb.grid(row = 1, column = i+1, sticky = "EW")

        self.report_name = Label(self.report_frame, textvariable = self.name)
        self.report_name.grid(row = 3, column = 1, sticky = "EW")

        self.report_age = Label(self.report_frame, textvariable = self.age)
        self.report_age.grid(row = 3, column = 2, sticky = "EW")
        
        self.report_score = Label(self.report_frame, text = "")
        self.report_score.grid(row = 3, column = 3)


    def show_frame2(self):
        #User inputs    
        try:
            #instance created to check if input data is correct for the variables
            if self.name.get() == "":
                self.warning.configure(text = "Please enter text")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text = "Please enter your name")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()

            elif self.age.get() == "":
                self.warning.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 12:
                self.warning.configure(text = "You're too old to play this game")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <= 0:
                self.warning.configure(text = "Please enter a number greater than 0")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <=7:
                self.warning.configure(text = "Oh no! You're too young to play this game")

            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.next_problem()

        except ValueError:
            self.warning.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

    def show_frame1(self):
        self.frame2.grid_remove() #removes frame 2
        self.frame1.grid()

    def next_problem(self):
        """ Creates a problem, stores the correct answer """
        x = randrange(10)
        y = randrange(10)
        self.select = self.difficulty_level.get()

        if self.select == "0":
            easy_text = str(x) + " + " + str(y) + " = "

            self.answer = x + y
            self.index += 1

            self.QuestionLabel.configure(text = easy_text)
            self.QuizLabel.configure(text = "Question" + str(self.index)+ "/5")

        elif self.select == "1":
            medium_text = str(x) + " - " + str(y) + " = "

            self.answer = x - y
            self.index += 1

            self.QuestionLabel.configure(text = medium_text)
            self.QuizLabel.configure(text = "Question" + str(self.index)+ "/5")

        else:
        
            hard_text = str(x) + " x " + str(y) + " = "

            self.answer = x * y
            self.index += 1

            self.QuestionLabel.configure(text = hard_text)
            self.QuizLabel.configure(text = "Question" + str(self.index)+ "/5")

        

        if self.index >= 6:
            self.frame2.grid_remove()
            self.report_frame.grid(row = 1, columnspan = 4)

    def check_answer(self):
        try:
            ans = int(self.QuestionEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct!")
                self.score += 1
                self.QuestionEntry.delete(0, END)
                self.QuestionEntry.focus()
                self.next_problem()
                
            else:
                self.feedback.configure(text = "Unlucky! Try again next time!")
                self.QuestionEntry.delete(0, END)
                self.QuestionEntry.focus()
                self.next_problem()

        except ValueError:
            self.feedback.configure(text = "This is not a number")
            self.QuestionEntry.delete(0, END)
            self.QuestionEntry.focus()

        if self.score <= 5:
            self.report_score.configure(text = str(self.score))
            
        

#code in the main routine
if __name__ == "__main__": #checking to see class name is the main module
    root = Tk() #root is a variable that calls the module to create GUI
    frames = MathQuiz(root)
    root.title("OOP") #Window title appears on top left
    root.mainloop()

    
