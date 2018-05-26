from tkinter import *
import numpy

# Global variables
width = 800
height = 480
numpy.zeros((8, 8))

# Functions
def fullEyes(color):
        array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
        c.create_rectangle(25,67.5,55,97.5, fill=color)
	
# Program
master = Tk()
# fullEyes(16,8,15)

c = Canvas(master, bg="black", width=width, height=height)
c.pack()
#c.create_rectangle(fullEyes(16,8,15), fill="red")
fullEyes("red")

mainloop()
