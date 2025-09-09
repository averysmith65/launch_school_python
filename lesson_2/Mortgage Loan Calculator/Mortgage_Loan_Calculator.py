# loan formulla m = p * (j / (1 - (1 + j) ** (-n)))
# import json

# def prompt(message):
#     print(f"==> {message}")

print("Welcome to mortgage loan calulator!")

def invalid_number(number_str):
    '''
    Determines if number is invalid by converting to a float
    
    Args:
        number_str (str): 

    Returns:
        bool: if string number can be converted to int
    '''
    try:
        float(number_str)
    except ValueError:
        return True
    return False

while True:
    while True:
        print("What is your loan amount?")
        loan_amount = input()
        
        if not invalid_number(loan_amount):
            break

        print("invalid number")
    
    while True:
        print("What is your APR? (for example 5% type 0.05)")
        apr = input()

        if not invalid_number(apr):
            break

        print("invalid number")

    while True:
        print("what is the loan duration? (please type in years)")
        loan_duration = input()

        if not invalid_number(loan_duration):
            break

        print("invalid number")

    
    monthly_interest = float(apr) / 12
    loan_months = float(loan_duration) * 12
    mortgage = (float(loan_amount) * (monthly_interest / (1 - (1 + monthly_interest) ** (-loan_months))))

    print(f"your mortgage is {mortgage}")
    break