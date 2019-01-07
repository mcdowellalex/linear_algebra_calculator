'''
This is a linear algebra calculator
author: Alex McDowell
December 2018
Version 2.2
'''


'''
########################################

########################################
'''

from tkinter import *
import random

class App:
    def __init__(self):
        self.master = Tk()
        self.master.title('Linear Algebra Calculator')
        self.location = ''
        self.home_page()
        
    def home_page(self):
        self.update_frame()
        
        self.location = 'home page'
            
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

        self.det_button = Button(self.frame, text = 'Determinant', command = self.determinant)
        self.det_button.grid(row = 2, column = 2)

        self.destroy_button = Button(self.frame, text = 'Exit', command = self.destroy)
        self.destroy_button.grid(row = 3)

    def update_frame(self):
        if self.location == '':
            None
        elif self.location == 'home page':
            self.frame.destroy()
        elif self.location == 'dot product page':
            self.dp_frame.destroy()
        elif self.location == 'eigenvalue page':
            self.ev_frame.destroy()
        elif self.location == 'determinant page':
            self.det_frame.destroy()
    
    def destroy(self):
        self.master.destroy()
    
    def dot_product(self):
        self.update_frame()
        
        self.location = 'dot product page'
        
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
        
        self.dp_answer_label = Label(self.dp_frame, text = '', font = ('Helvetica', 24, 'bold'))
        self.dp_answer_label.grid(row = 3, column = 2, rowspan = 2)
        
        self.v2_label = Label(self.dp_frame, text = 'Vector 2:')
        self.v2_label.grid(row = 4)
        self.v2_entry = Entry(self.dp_frame, width = 20)
        self.v2_entry.grid(row = 4, column  = 1)
        
        
        self.destroy_button = Button(self.dp_frame, text = 'Exit', command = self.destroy)
        self.destroy_button.grid(row = 7, column = 0)
        
        self.calculate_dp_button = Button(self.dp_frame, text = 'Calculate', command = self.calculate_dot_product)
        self.calculate_dp_button.grid(row = 5, column = 1)    
        
        self.back_button = Button(self.dp_frame, text = 'Home', command = self.home_page)
        self.back_button.grid(row = 5, column = 0)
        
        self.error_label = Label(self.dp_frame, text = '')
        self.error_label.grid(row = 6, columnspan = 5)
        
        
    def calculate_dot_product(self):
        self.v1 = self.v1_entry.get()
        self.v2 = self.v2_entry.get()
        
        self.v1 = self.v1.split(',')
        self.v1 = [int(i) for i in self.v1]
        
        self.v2 = self.v2.split(',')
        self.v2 = [int(i) for i in self.v2]
        
        if len(self.v1) == len(self.v2):
            #calculate the dot product here
            self.dp_answer = 0
            for i in range(len(self.v1)):
                product = self.v1[i] * self.v2[i]
                self.dp_answer = self.dp_answer + product
                
            str(self.dp_answer)
            self.dp_answer_label.config(text = self.dp_answer) 
            self.error_label.config(text = '')
        else:
            self.error_label.config(text = 'Please enter two vectors of equal length')
        
    def eigenvalues(self):
        self.update_frame()
        
        self.location = 'eigenvalue page'
        
        self.ev_frame = Frame(self.master)
        self.ev_frame.grid()
        
        self.ev_title = Label(self.ev_frame, text = 'Eigenvalue Calculator', font = '16')
        self.ev_title.grid(row = 0, columnspan = 2)

        

    def determinant(self):
        self.update_frame()

        self.location = 'determinant page'

        self.det_frame = Frame(self.master)
        self.det_frame.grid()

        self.det_label = Label(self.det_frame, text = 'Determinant Calculator', font = '16')
        self.det_label.grid(row = 0, columnspan = 2)

        self.det_num_rows_entry = Entry(self.det_frame)
        self.det_num_rows_entry.grid(row = 1)
        self.det_num_columns_entry = Entry(self.det_frame)
        self.det_num_columns_entry.grid(row = 2)

        self.det_calc_button = Button(self.det_frame, text = 'Calculate', command = self.calculate_determinant)
        self.det_calc_button.grid(row = 2, column = 1)

        self.det_to_home_button = Button(self.det_frame, text = 'Home', command = self.home_page)
        self.det_to_home_button.grid(row = 3)
        
    def calculate_determinant(self):
        None
        
        
        
            
    

'''
inititalize the window with the frame
the master is the master/root that always stays
i use frame.destroy to clear everything and update with a new 'page'
'''

if __name__ == '__main__':
    app = App()
