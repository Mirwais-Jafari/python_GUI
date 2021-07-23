import tkinter
import os

def percentage(unfinishedLb, finishedLb, percentageV):

    unfinishSize = unfinishedLb.size()
    finishSize = finishedLb.size()

    try:
        total = unfinishSize+finishSize
        percentage = (100/total)*finishSize
    except ZeroDivisionError:
        percentage = 0
    percentage = int(percentage)
    percentageV.set('%i%% tasks are completed.'%percentage)

def makingNewTodo(unfinishedLb, finishedLb, percentageV):
    unfinishedLb.delete(0,tkinter.END)
    finishedLb.delete(0,tkinter.END)

    os.remove('toDo.txt')
    os.remove('finishedTodo.txt')
    percentage(unfinishedLb, finishedLb, percentageV)

def removeTextFromFile(fileName, text):
    with open(fileName, 'r') as file:
        with open('default', 'w') as newFile:
            lines = file.readlines()
            for line in lines:
                if line.strip('\n') != text:
                    newFile.write(line)
    os.remove(fileName)
    os.rename('default', fileName)

def removeText(unfinishedLb, finishedLb, percentageV):
    if unfinishedLb.curselection():
        index = unfinishedLb.curselection()
        removeTextFromFile('toDo.txt', unfinishedLb.get(index))
        unfinishedLb.delete(index)
    elif finishedLb.curselection():
        index = finishedLb.curselection()
        removeTextFromFile('finishedTodo.txt', finishedLb.get(index))
        finishedLb.delete(index)
    percentage(unfinishedLb, finishedLb, percentageV)



def unfinishTask(unfinishedLb, finishedLb, percentageV):
    index = finishedLb.curselection()
    text = finishedLb.get(index)
    finishedLb.delete(index)
    unfinishedLb.insert(tkinter.END, text)
    removeTextFromFile('finishedTodo.txt', text)
    with open('toDo.txt', 'a') as file:
        file.write(text+'\n')
    percentage(unfinishedLb, finishedLb, percentageV)


def finishTask(unfinishedLb, finishedLb, percentageV):
    index = unfinishedLb.curselection()
    text = unfinishedLb.get(index)
    unfinishedLb.delete(index)

    finishedLb.insert(tkinter.END, text)
    removeTextFromFile('toDo.txt', text)
    with open('finishedTodo.txt', 'a') as file:
        file.write(text+'\n')
    percentage(unfinishedLb, finishedLb, percentageV)


def clearEntry(theEntry):
    theEntry.delete(0,tkinter.END)

def insertFileText(listBox, listBox2):
    if os.path.exists('toDo.txt'):
        with open('toDo.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            listBox.insert(tkinter.END, line.strip('\n'))
    if os.path.exists('finishedTodo.txt'):
        with open('finishedTodo.txt')as file:
            lines = file.readlines()
        for line in lines:
            listBox2.insert(tkinter.END, line.strip('\n'))

def isNotInFile(lines, text):
    for line in lines:
        if line.strip('\n') == text:
            return False
    return True
def addText(text, unfinishedLb, finishedLb, percentageV,theEntry):
    with open('toDo.txt', 'a+') as file:
        lines = file.readlines()
        if isNotInFile(lines, text) and text!='':
            file.write(text+'\n')
            unfinishedLb.insert(tkinter.END, text)
    percentage(unfinishedLb, finishedLb, percentageV)
    theEntry.delete(0,tkinter.END)