from tkinter import *

# Global variables
width = 200
height = 200

# Functions
def fullEyes(int x_dots, int y_dots, int spacing):
	x_eyes = [None]*x_dots
	x_eyes[0] = (width-spacing)/x_dots
	for i in range(x_dots-1):
		if(x_eyes[i]>width-1.5*x_eyes[0])
			break
		x_eyes[i+1] = 1.5*x_eyes[0]+x_eyes[i] 
	return eyes
	
# Program
master = Tk()

c = Canvas(master, bg="black", width=width, height=height)
c.pack()
c.create_rectangle(fullEyes(), fill="red")

mainloop()
