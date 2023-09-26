#This will be the code for my calculator app



#so this is where we will make the gui
from tkinter import *
window = Tk()
window.geometry("350x370") #defining the size of the window
window.resizable(0,0) #so that the window is not resizable
window.title("Bodmas Calculator")#the title of the window and the application

#the functions we're using for the program:
#button click
#button clear
#button eval

#this function updates the input field with the new item
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
#this button is essentially the clear option on the calculator
#it will clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set(expression)

#this button will evaluate the expression present in the input field
def button_equal():
    global expression
    result = str(eval(expression)) #eval is what we use to calculate the expression
    input_text.set(result)
    expression = ""

input_text = StringVar() #this is how we get the input field
#this is where we will keep our expression
expression = ""
#this is the representation of the input field 
input_frame = Frame(window, width=350, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#this is where we create the input field within the frame
 
input_field = Entry(input_frame, font=('arial black', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#this is the button frame for the buttons in the calculater
 
button_frame = Frame(window, width=350, height=272.5, bg="light grey")
 
button_frame.pack()
 
# first row of the buttons, contains clear, left and right parenthesis and the divde function
 
clear = Button(button_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_clear()).grid(row = 0, column = 0, padx = 1, pady = 1)

left_paren = Button(button_frame, text = "(", fg ="black",width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("(")).grid(row = 0, column = 1, padx = 1, pady = 1)

right_paren = Button(button_frame, text = ")", fg ="black",width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click(")")).grid(row = 0, column = 2, padx = 1, pady = 1) 

divide = Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 


# second row of the buttons, contains the first layer of a keypad, 7 8 9
 
seven = Button(button_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(button_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(button_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row of the buttons, contains the second layer of a keypad 4 5 6
 
four = Button(button_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(button_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(button_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row of the buttons, contains the third layer of a keypad 1 2 3
 
one = Button(button_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(button_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(button_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row of the buttons, contains 0, decimal/floating point, equals 
 
zero = Button(button_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(button_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(button_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
#and after this the window loop ends
window.mainloop()
