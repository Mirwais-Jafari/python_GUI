import tkinter
from functions import *
import time

def main():
    root = tkinter.Tk()
    root.geometry('20x10')
    root.title('Best todo list')

    # Making widgets
    topFrame = tkinter.Frame(root)
    bottomFrame = tkinter.Frame(root)

    # scrollBars
    scrollBar1 = tkinter.Scrollbar(bottomFrame)
    scrollBar2 = tkinter.Scrollbar(bottomFrame)

    # label topFrame.grid(pady=5)
    percentageV = tkinter.StringVar()
    percentageL = tkinter.Label(topFrame, textvariable=percentageV, font=('impact', 10))

    # Label bottomfram
    finishedlab = tkinter.LabelFrame(bottomFrame, text="You Did It ", font=('impact', 8),
                                     bd=6)
    unfinishedlab = tkinter.LabelFrame(bottomFrame, text="You Must Do ", font=('impact', 8),
                                       bd=6)

    # listboxes
    finishedLb = tkinter.Listbox(bottomFrame, yscrollcommand=scrollBar2.set,
                                 bd=4, font=('courier', 10))

    unfinishedLb = tkinter.Listbox(bottomFrame, yscrollcommand=scrollBar1.set,
                                   bd=4, font=('courier', 10))

    theEntry = tkinter.Entry(topFrame, bd=3)
    theEntry.config(font=('courier', 10))
    theEntry.focus()

    # Buttons
    addBtn = tkinter.Button(topFrame, text='Add', font=('impact', 8),
                            command=lambda: addText(theEntry.get(),
                                                    unfinishedLb,
                                                    finishedLb, percentageV, theEntry),
                            bd=5, )
    clearBtn = tkinter.Button(topFrame, text='Clear', bd=5, font=('impact', 8),
                              command=lambda: clearEntry(theEntry))
    finishedBtn = tkinter.Button(topFrame, text='Finished', bd=5, font=('impact', 8),
                                 command=lambda: finishTask(unfinishedLb, finishedLb, percentageV))
    unfinishedBtn = tkinter.Button(topFrame, text='Unfinished', bd=5, font=('impact', 6),
                                   command=lambda: unfinishTask(unfinishedLb, finishedLb, percentageV))
    newToDoBtn = tkinter.Button(topFrame, text='NewToDo', bd=5, font=('impact', 6),
                                command=lambda: makingNewTodo(unfinishedLb, finishedLb, percentageV))
    removeBtn = tkinter.Button(topFrame, text='Remove', bd=5, font=('impact', 8),
                               command=lambda: removeText(unfinishedLb, finishedLb, percentageV))

    scrollBar1.configure(command=unfinishedLb.yview)
    scrollBar2.configure(command=finishedLb.yview)

    # gridding or placing
    # row 1
    addBtn.place(relx=0.03, relwidth=0.1, rely=0.1, relheight=0.4)
    theEntry.place(relx=0.15, relwidth=0.7, rely=0.1, relheight=0.4)
    clearBtn.place(relx=0.87, relwidth=0.1, rely=0.1, relheight=0.4)
    # row2
    finishedBtn.place(relx=0.03, relwidth=0.1, rely=0.55, relheight=0.4)
    unfinishedBtn.place(relx=0.15, relwidth=0.1, rely=0.55, relheight=0.4)
    newToDoBtn.place(relx=0.27, relwidth=0.1, rely=0.55, relheight=0.4)
    removeBtn.place(relx=0.39, relwidth=0.1, rely=0.55, relheight=0.4)
    percentageL.place(relx=0.51, relwidth=0.45, rely=0.45, relheight=0.6)
    # row3
    unfinishedlab.place(relx=0.031, relwidth=0.45, rely=0, relheight=0.1)
    finishedlab.place(relx=0.501, relwidth=0.45, rely=0, relheight=0.1)
    # row4
    unfinishedLb.place(relx=0.03, relwidth=0.45, rely=0.1, relheight=0.88)
    scrollBar1.place(relx=0.48, relwidth=0.02, rely=0.1, relheight=0.88)
    finishedLb.place(relx=0.5, relwidth=0.45, rely=0.1, relheight=0.88)
    scrollBar2.place(relx=0.95, relwidth=0.02, rely=0.1, relheight=0.88)

    topFrame.place(relx=0, relwidth=1, rely=0, relheight=0.2)
    bottomFrame.place(relx=0, relwidth=1, rely=0.2, relheight=0.8)

    insertFileText(unfinishedLb, finishedLb)
    percentage(unfinishedLb, finishedLb, percentageV)
    root.mainloop()


main()