'''
###################################
trying to make a copy of the list
rows without having it point to the
same memory location
so I can make alterations to the
copy without changing the original
###################################
'''

def calculate_determinant(rows):
    ans = 0
    if len(rows[0]) == 2:
        print('p')
        ans = (rows[0][0] * rows[1][1]) - (rows[0][1] * rows[1][0]) #basic determinant calculation = a*d - b*c
        
    else:
        coefficients = rows[0] #first row is all the coefficients for the determinant
        rows.pop(0) #remove the row of coefficients
        
        
        for j in range(len(rows[0])):
            if j % 2 == 0: #the number is even so the coefficient is even      
                new_rows = rows[:]
                
                print('new',new_rows)
                print('rows',rows)
                
                for i in range(len(rows)):
                    new_rows[i].pop(j)
                    print('new',new_rows)
                    print('rows',rows)
                    
                ans = ans + (coefficients[j] * calculate_determinant(new_rows))
                print('even',ans)
                print('new',new_rows)
                print('rows',rows)
            else: #the number is odd so the coefficient is odd
                new_rows = rows.copy()

                for i in range(len(rows)):
                    new_rows[i].pop(j)
                                            
                ans = ans + (-(coefficients[j]) * calculate_determinant(new_rows))
                
                      
    return ans                
        
               

rows = [[1,2,4],[2,1,3], [4,4,5]]
answer = calculate_determinant(rows)
print('answer is:' , answer)
