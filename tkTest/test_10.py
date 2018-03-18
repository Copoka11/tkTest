from tkinter import *

def new_win():
    win = Toplevel(root)
    label1 = Label(win, text="Top level window text", font=20)
    label1.pack()

def exit_app():
    root.destroy()



root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="File", menu=first_item)
first_item.add_command(label="New", command=new_win)
first_item.add_command(label="Exit", command=exit_app)

second_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=second_item)
second_item.add_command(label="Item1")
second_item.add_command(label="Item2")
second_item.add_command(label="Item3")
second_item.add_command(label="Item4")
second_item.add_separator()
second_item.add_command(label="Item5")

tool_bar = Frame(root, bg="#a1a1a1")
tool_bar.pack(side=TOP, fill=X)

btn1 = Button(tool_bar, text="Cut")
btn1.grid(row=0, column=0, padx=2, pady=2)

btn2 = Button(tool_bar, text="Copy")
btn2.grid(row=0, column=1, padx=2, pady=2)

btn3 = Button(tool_bar, text="Paste")
btn3.grid(row=0, column=2, padx=2, pady=2)

status_bar = Label(root, relief=SUNKEN, anchor=W, text="mission complete")
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
