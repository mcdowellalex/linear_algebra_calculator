'''
This is a linear algebra calculator
author: Alex McDowell
December 2018
Version 1.0
'''


'''
########################################
Version 1.0 contains a working change of
frame
########################################
'''

from tkinter import *
import random


def dot_product():
    frame.destroy()
    
    dp_frame = Frame(master)
    dp_frame.grid()
    
    dp_title = Label(dp_frame, text = 'Dot Product Calculator', font = '16')
    dp_title.grid(row = 0)
    
    
    
    
    
def eigenvalues():
    print('poop')
        
def destroy():
    master.destroy()
    

'''
inititalize the window with the frame
the master is the master/root that always stays
i use frame.destroy to clear everything and update with a new 'page'
'''
master = Tk()
frame = Frame(master)
frame.grid()


welcome = Label(frame, text = 'Welcome to the Linear Algebra Calculator', font = '24')
welcome.grid(row = 0, columnspan = 8)
choice = Label(frame, text = 'Please choose what you would like to calculate')
choice.grid(row = 1, columnspan = 8)

dot_product_button = Button(frame, text = 'Dot Product', command = dot_product)
dot_product_button.grid(row = 2)

eigenvalue_button = Button(frame, text = 'Eigenvalues', command = eigenvalues)
eigenvalue_button.grid(row = 2, column = 1)

destroy = Button(frame, text = 'Exit', command = destroy)
destroy.grid(row = 3)

