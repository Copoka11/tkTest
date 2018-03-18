from tkinter import *
from tkinter.messagebox import *

def ask_question(event):
    answer = askquestion("Ask Question", "Question one?")
    label1.configure(text=answer)

def ask_ok(event):
    answer = askokcancel("AskOkCancel", "Question two?")
    label2.configure(text=answer)

def ask_yn(event):
    answer = askyesno("AskYesNo", "Question three?")
    label3.configure(text=answer)

def ask_rc(event):
    answer = askretrycancel("AskRetryCancel", "Question four?")
    label4.configure(text=answer)


root = Tk()

btn1 = Button(root, text="askquestion", font=("Tahoma", 20), width=12)
btn1.grid(row=0, column=0, sticky="ew")
label1 = Label(root, font=("Tahoma", 20), width=12)
label1.grid(row=0, column=1)
btn1.bind("<Button-1>", ask_question)

btn2 = Button(root, text="askokcancel", font=("Tahoma", 20), width=12)
btn2.grid(row=1, column=0, sticky="ew")
label2 = Label(root, font=("Tahoma", 20), width=12)
label2.grid(row=1, column=1)
btn2.bind("<Button-1>", ask_ok)

btn3 = Button(root, text="askyesno", font=("Tahoma", 20), width=12)
btn3.grid(row=2, column=0, sticky="ew")
label3 = Label(root, font=("Tahoma", 20), width=12)
label3.grid(row=2, column=1)
btn3.bind("<Button-1>", ask_yn)

btn4 = Button(root, text="retrycancel", font=("Tahoma", 20), width=12)
btn4.grid(row=3, column=0, sticky="ew")
label4 = Label(root, font=("Tahoma", 20), width=12)
label4.grid(row=3, column=1)
btn4.bind("<Button-1>", ask_rc)



root.mainloop()
