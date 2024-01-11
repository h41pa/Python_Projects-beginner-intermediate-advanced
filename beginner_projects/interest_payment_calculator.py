
def loan_calculator():
    print("This is a monthly payment loan calculator ")
    print()

    loan_ammount = float(input("Input the loan amount: "))
    interest_rate = float(input("Input the annual interest rate: "))
    years = int(input("Input ammount of years: "))

    monthly_interest_rate = interest_rate / 1200
    amount_of_months = years * 12
    monthly_payment = loan_ammount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    print(" The monthly payment for this loan is: %.2f " % monthly_payment)

loan_calculator()
