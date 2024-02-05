# Calculating Principle Amount

def calculate_principle(borrowedamount,rate,duriation):
    pr_amount = borrowedamount / (1+(rate * duriation))
    intrest_amount = pr_amount - borrowedamount
    return pr_amount, intrest_amount


borrowedamount = 200000
rate = 0.05
duriation = 2

pr_amt = calculate_principle(borrowedamount,rate,duriation)
print(pr_amt)
print("Principle: ", borrowedamount)
print("Loan Duriation: ", duriation)
print("Rate of intrest: ", rate)
print("Total Amount Pending: ", pr_amt)