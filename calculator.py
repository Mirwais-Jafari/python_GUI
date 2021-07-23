from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.title('Simple Calculator')
e=Entry(root,width=35,borderwidth=2)
e.grid(row=0,column=0,columnspan=3,padx=10)
def button_insert(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def addition_button():
	first_number=e.get()
	global f_number
	global math
	math='addition'
	f_number=float(first_number)
	e.delete(0,END)

def subtraction_button():
	first_number=e.get()
	global f_number
	global math
	math='subtraction'
	f_number=float(first_number)
	e.delete(0,END)

def multiplication_button():
	first_number=e.get()
	global f_number
	global math
	math='multiplication'
	f_number=float(first_number)
	e.delete(0,END)

def division():
	first_number = e.get()
	global f_number
	global math
	math = 'division'
	f_number = float(first_number)
	e.delete(0, END)

def Equal_button():
	second_number=e.get()
	e.insert(0,second_number)
	e.delete(0,END)
	if math=='addition':
		e.insert(0,f_number + float(second_number))
	if math=='subtraction':
		e.insert(0,f_number - float(second_number))
	if math=='multiplication':
		e.insert(0,f_number * float(second_number))
	if math=='division':
		e.insert(0,f_number / float(second_number))

def clear_button():
	e.delete(0,END)

def exit_button():
	root.destroy()
def About_button():
	msg.showerror("App Details","info\nCreated by Mirwais Kavosh\nf:Mir Wais\ncall number: 0785544760")


# define the buttons
button_1=Button(root,text='1',padx=40,pady=20,command=lambda:button_insert(1))
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_insert(2))
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_insert(3))
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_insert(4))
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_insert(5))
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_insert(6))
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_insert(7))
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_insert(8))
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_insert(9))
button_0=Button(root,text='0',padx=40,pady=20,command=lambda:button_insert(0))

add_button=Button(root,text='+',padx=40,pady=20,command=addition_button)
equal_button=Button(root,text='=',padx=40,pady=20,command=Equal_button)
clear_button=Button(root,text='C',padx=36,pady=20,command=clear_button)

sub_button=Button(root,text='-',padx=40,pady=20,command=subtraction_button)
multiply_button=Button(root,text='x',padx=42,pady=20,command=multiplication_button)
divide_button=Button(root,text='/',padx=40,pady=20,command=division)
exit_button=Button(root,text='exit',padx=34,pady=20,command=exit_button)
about_button=Button(root,text='about',padx=30,pady=20,command=About_button)

# grid the buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
add_button.grid(row=4,column=1)
equal_button.grid(row=4,column=2)

sub_button.grid(row=5,column=0)
divide_button.grid(row=5,column=1)
multiply_button.grid(row=5,column=2)
clear_button.grid(row=6,column=0,ipadx=2)
exit_button.grid(row=6,column=1)
about_button.grid(row=6,column=2)
root.mainloop()
