'''
This is a linear algebra calculator
author: Alex McDowell
December 2018
Version 2.0
'''


'''
########################################
Version 2.1 is the first working version
with classes and updating the frame by
destroying it
########################################
'''
from tkinter import *
import random

class App:
    def __init__(self):
        self.master = Tk()
        self.master.title('Linear Algebra Calculator')
        
        self.frame = Frame(self.master)
        self.frame.grid()
        
        self.welcome = Label(self.frame, text = 'Welcome to the Linear Algebra Calculator', font = '24')
        self.welcome.grid(row = 0, columnspan = 8)
        self.choice = Label(self.frame, text = 'Please choose what you would like to calculate')
        self.choice.grid(row = 1, columnspan = 8)

        self.dot_product_button = Button(self.frame, text = 'Dot Product', command = self.dot_product)
        self.dot_product_button.grid(row = 2)

        self.eigenvalue_button = Button(self.frame, text = 'Eigenvalues', command = self.eigenvalues)
        self.eigenvalue_button.grid(row = 2, column = 1)

        self.destroy = Button(self.frame, text = 'Exit', command = self.destroy)
        self.destroy.grid(row = 3)

    def destroy(self):
        self.master.destroy()
    
    def dot_product(self):
        self.frame.destroy()
        
        self.dp_frame = Frame(self.master)
        self.dp_frame.grid()
        
        self.dp_title = Label(self.dp_frame, text = 'Dot Product Calculator', font = '16')
        self.dp_title.grid(row = 0, columnspan = 2)
        
        self.dp_instruction = Label(self.dp_frame, text = 'Please enter two vectors of equal length with entries separated by commas')
        self.dp_instruction.grid(row = 1, columnspan = 7)
        self.dp_instruction_2 = Label(self.dp_frame, text = 'For example: (4, 5, 46, 0)')
        self.dp_instruction_2.grid(row = 2, columnspan = 2, sticky = W)
        
        self.v1_label = Label(self.dp_frame, text = 'Vector 1:')
        self.v1_label.grid(row = 3)
        self.v1_entry = Entry(self.dp_frame, width = 20)
        self.v1_entry.grid(row = 3, column = 1)
        
        self.dp_answer = Label(self.dp_frame, text = '', font = ('Helvetica', 24, 'bold'))
        self.dp_answer.grid(row = 3, column = 2, rowspan = 2)
        
        self.v2_label = Label(self.dp_frame, text = 'Vector 2:')
        self.v2_label.grid(row = 4)
        self.v2_entry = Entry(self.dp_frame, width = 20)
        self.v2_entry.grid(row = 4, column  = 1)
        
        self.calculate_dp_button = Button(self.dp_frame, text = 'Calculate', command = self.calculate_dot_product)
        self.calculate_dp_button.grid(row = 5, column = 1)
        
    def calculate_dot_product(self):
        None
        
    def eigenvalues(self):
       None
            
    

'''
inititalize the window with the frame
the master is the master/root that always stays
i use frame.destroy to clear everything and update with a new 'page'
'''

if __name__ == '__main__':
    app = App()
    

