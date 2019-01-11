

def calculate_determinant(rows):
    if len(rows[0]) == 2:
        print(rows)
        ans = (rows[0][0] * rows[1][1]) - (rows[0][1] * rows[1][0]) #basic determinant calculation = a*d - b*c
        return ans
    else:
        print(rows)
        coefficients = rows[0] #first row is all the coefficients for the determinant
        rows.pop(0) #remove the row of coefficients

        for j in range(len(rows[0])):
            if j % 2 == 0: #the number is even so the coefficient is even
                new_rows = rows
                for i in new_rows:
                    i.pop(j)
                             
                coefficients[j] * calculate_determinant(new_rows)
                print(rows)
            else: #the number is odd so the coefficient is odd
                new_rows = rows
                for i in new_rows:
                    i.pop(j)

                -(coefficients[j]) * calculate_determinant(new_rows)
               

rows = [[1,2,3],[1,2,3],[1,2,3]]
calculate_determinant(rows)
