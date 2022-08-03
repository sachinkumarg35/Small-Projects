#GUI Calculator using tkinter Python.

#Import the libraries.
import tkinter as tk
from tkinter import*
#imported* from tkinter means imported everything from tkinter.

#Now we need to call TK()in-app variable, now we will use app instead of Tk()
app = tk.Tk()

#Tk() to set the window size to be 200*270.
app.geometry("250x280")
app.title("Calculator")
app.maxsize(250, 220)
app.minsize(250, 250)

"Then using the title class we have named it as python calculator. Then using max size and a midsize class of window which is the maximum and minimum size of the window to be 200×270. Now what is done here is when a user tries to minimize or maximize the window he will not be able to do it, as we don’t want to adjust the buttons which we will create some after"

ent = Entry(app, width=16, borderwidth = 3, relief=RIDGE)
ent.grid(pady = 10, row= 0, sticky='w', padx=15)

"Now we have used the Entry widget of tkinter library to create an input box for our calculator which is invariable “ent” and Entry takes arguments as parent container which id “app” here and other options like width which is 20px and border-width which is equal to 5px and to make it look like input box we have used style as RIDGE which creates the box-shadow."

"In the next line, we have used grid geometry to create a 2-d table on the window and can be accessed as rows and columns and added arguments like pady which is basically padding in y to 12px and sticky equals to w which means its direction will be west and padx which is padding in x to 17px and added all this configuration to “ent” object."

def delete():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")
def fresult():
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                c_res = ent.get()
                c_res = eval(c_res)
                clearf()
                ent.insert("end",c_res)
def clearf():
        ent.delete(0,"end")
                   
"Now we have defined a function delete which will be the last character of the input using delete method like ent.delete(first=len(a)-1, last=”end”) where len() is a built-in python function and a is used to get the value of the input. Now we will define fresult() which is the final result and which will be called when the user asks for it and in the next line we have used is get method to get the value of what is in the “ent” input box and check it as if ent.get() == “” means if it is blank then do nothing as “pass”. In next line elif ent.get()[0] == “0” means else if “ent” first index value is “0” then delete the “ent” input from 0 to end as ent.delete(0,”end”). And in the next line, else we have created “c_res” variable which contains the value of input as ent.get() then updated “c_res” variable to contain eval(c_res) which is the brain of this calculator which is eval() built-in function in python which needs a separate article and it converts python input from string to integer completes all the mathematical operations by itself and then we have called clearf() function which we create jus after and at the end of this function we insert “c_res” value to end in the input box using ent.insert(“end”,c_res)."

"In the next line, we have defined a function clearf()  which is used when a user calls a clear function to clean the input box and in the next line is to delete all the characters from start to end in the input box as ent.delete(0,”end”)"
                  
#Now we are going to add GUI widgets of numbers and other operators like:
clean = Button(app, text="C", width = 8, command=clearf, bg="green", fg="pink", relief = RIDGE)
clean.grid(row =0, sticky="w", padx =125)

char_nine = Button(text = "9", width = 2, command=lambda: ent.insert("end", "9" ), borderwidth = 3, relief=RIDGE)
char_nine.grid(row=1, sticky="w", padx=15)
char_eight = Button(text = "8", width = 2, command=lambda: ent.insert("end", "8"), borderwidth = 3, relief=RIDGE)
char_eight.grid(row=1, sticky="w", padx=45)
char_seven = Button(text = "7", width = 2, command=lambda: ent.insert("end", "7"), borderwidth = 3, relief=RIDGE)
char_seven.grid(row=1, sticky="w", padx=75)

char_plus = Button(app, text="+", width=5, command=lambda: ent.insert("end", "+"), borderwidth = 3, relief=RIDGE)
char_plus.grid(row =1, sticky="e", padx=125)

char_six = Button(text = "6", width = 2, command=lambda: ent.insert("end", "6"), borderwidth = 3, relief=RIDGE)
char_six.grid(row=2, sticky="w", padx = 15, pady=5)
char_five = Button(text = "5", width = 2, command=lambda: ent.insert("end", "5"), borderwidth = 3, relief=RIDGE)
char_five.grid(row=2, sticky="w", padx = 45, pady = 5)
char_four = Button(text = "4", width = 2, command=lambda: ent.insert("end", "4"), borderwidth = 3, relief=RIDGE)
char_four.grid(row =2, sticky="w", padx = 75, pady = 5)

char_minus = Button(app, text="-", width = 5, command=lambda: ent.insert("end", "-"), borderwidth = 3, relief = RIDGE)
char_minus.grid(row=2, sticky="e", padx=125, pady = 5)

char_three = Button(text = "3", width = 2, command=lambda: ent.insert("end", "3"), borderwidth = 3, relief = RIDGE)
char_three.grid(row=3, sticky="w", padx = 15, pady = 5)
char_two = Button(text="2", width = 2, command=lambda: ent.insert("end", "2"), borderwidth = 3, relief=RIDGE)
char_two.grid(row=3, sticky = "w", padx = 45, pady = 5)
char_one = Button(text = "1", width = 2, command=lambda: ent.insert("end", "1"), borderwidth = 3, relief = RIDGE)
char_one.grid(row=3, sticky="w", padx=75, pady=5)

char_multiply = Button(app, text="*", width = 5, command=lambda: ent.insert("end", "*"), borderwidth = 3, relief = RIDGE)
char_multiply.grid(row=3, sticky="e", padx = 125, pady = 5)

char_zero = Button(text = "0", width = 2, command=lambda: ent.insert("end", "0"), borderwidth = 3, relief = RIDGE)
char_zero.grid(row=4, sticky="w", padx=15, pady=5)
char_double_zero = Button(text = "00", width = 2, command=lambda: ent.insert("end", "00"), borderwidth = 3, relief = RIDGE)
char_double_zero.grid(row = 4, sticky="w", padx = 45, pady = 5)
char_dot = Button(app, text=".", width = 2, command=lambda: ent.insert("end", "."), borderwidth = 3, relief = RIDGE)
char_dot.grid(row = 4, sticky="w", padx= 75, pady = 5)

char_divide = Button(app, text="/", width = 5, command=lambda: ent.insert("end", "/"), borderwidth = 3, relief = RIDGE)
char_divide.grid(row = 4, sticky = "e", padx= 125, pady = 5)

result = Button(app, text = "=", width = "10", command=fresult, bg="blue", fg="white", borderwidth = 3, relief = RIDGE)
result.grid(row = 5, sticky = "w", padx = 15, pady = 5)

char_modulus = Button(app, text="%", width = 5, command=lambda: ent.insert("end", "%"), borderwidth = 3, relief = RIDGE)
char_modulus.grid(row = 5, sticky = "e", padx = 125, pady = 5)

delete = Button(app, text = "del", width = 5, command = delete, borderwidth = 3, relief = RIDGE)
delete.grid(row = 5, sticky = "w", padx = 80, pady=5)

"Now the main GUI starts as we will create buttons for the calculator. So the first Button is a clean variable that has a parent container app and its text is “c” with a background colour green, and foreground colour to white and relief style as RIDGE and command argument is clearf function that is when user clicks “C” on the calculator it triggers clearf() function."

"In the next line, we have used grid geometry of clean button to have row=0 , sticky which is the direction to west or “w” padx or padding in x to 125"

"Now we have to create all the buttons are 0-9 number and “+,-,*,/,%, =, del”"

"As all are going to be buttons so many of its arguments are going to be just the same like width=2, borderwidth=3 and relief=RIDGE. Things that will be changed are text as it is new in every button command which will be a new lambda function everywhere."

"NOTE: LAMBDA OR ANONYMOUS FUNCTION IS A FUNCTION THAT CAN BE MADE WITHOUT NAMES AND UNLIKE REGULAR PYTHON FUNCTION IT CANNOT BE USED MORE THAN ONCE."

app.mainloop()
#Above is the last line of code which is mainloop() class of tkinter library which will handle all the user clicks and background threads.