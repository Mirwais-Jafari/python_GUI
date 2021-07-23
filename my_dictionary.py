from tkinter import *
root=Tk()
root.config(bg='black')
root.title("Dictionary")
def close_root():
    root.destroy()
    exit()

def submit():
    entered_text=entry.get()
    output.delete(0.0,END)
    try:
        difinition=my_dictionary[entered_text]
    except:
        difinition="Sorry the word you entered is not exist in dictionary"
    output.insert('end',difinition)
 
label_text=Label(root,text="Enter the word you would like a difinition for:",bg='white',fg='black',relief=RAISED)
label_text.grid(row=0,column=0,sticky='w')
entry=Entry(root,width=40,bg='white',fg='black')
entry.grid(row=1,column=0,sticky='w')
submit_b=Button(root,text='Submit',bg='white',fg='black',relief=RAISED,command=submit)
submit_b.grid(row=2,column=0)
lablel_difinitaion=Label(root,text='Definition:',bg='white',fg='black',relief=RAISED).grid(row=3,column=0,sticky='w')
output=Text(root,width=30,heigh=5,font="none 12")
output.grid(row=4,column=0)
lable_exit=Label(root,text='Click to exit:',bg='white',fg='black').grid(row=5,column=0,sticky='w')
exit_b=Button(root,text='Exit',command=close_root,bg='white',fg='black').grid(row=6,column=0)
   
my_dictionary={'computer':'is a machine that calculate the data like take the information and does proccess over that and give us the output.','Mother':'is a person who feed the children and take care.'}

root.mainloop()