'''
Homemade Calculator by Isaiah Romero
'''

from tkinter import *

root = Tk()

#Create buttons for numbers and operations
buttonVariable = Button()
label1 = Label(root, text = "I. Romero - Calculator")
Button1 = Button(root, text = '1', width = 10)
Button2 = Button(root, text = '2', width = 10)
Button3 = Button(root, text = '3', width = 10)
Button4 = Button(root, text = '4', width = 10)
Button5 = Button(root, text = '5', width = 10)
Button6 = Button(root, text = '6', width = 10)
Button7 = Button(root, text = '7', width = 10)
Button8 = Button(root, text = '8', width = 10)
Button9 = Button(root, text = '9', width = 10)
Button10 = Button(root, text = '+', width = 10)
Button11 = Button(root, text = '0', width = 10)
Button12 = Button(root, text = '-', width = 10)
Button13 = Button(root, text = '/', width = 10)
Button14 = Button(root, text = '=', width = 10)
Button15 = Button(root, text = 'X', width = 10)

#Make the grid
label1.grid(row = 0, columnspan = 30)
Button1.grid(row=1,column=0)
Button2.grid(row=1,column=1)
Button3.grid(row=1,column=2)
Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)
Button7.grid(row=3,column=0)
Button8.grid(row=3,column=1)
Button9.grid(row=3,column=2)
Button10.grid(row=4,column=0)
Button11.grid(row=4,column=1)
Button12.grid(row=4,column=2)
Button13.grid(row=5,column=0)
Button14.grid(row=5,column=1)
Button15.grid(row=5,column=2)
root.mainloop()