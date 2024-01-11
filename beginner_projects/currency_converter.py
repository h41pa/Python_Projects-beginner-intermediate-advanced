# def currency_convertor():
#     print("This program converts US dollars to Euro ")
#     print()
#
#     dollars = int(input("Enter amount of dollars: "))
#     euro = round(dollars * 0.97, 2)
#     print(f"{dollars} dollars = {euro} EURO")
#
#
# currency_convertor()


def currency_convertor():
    print("This program converts US dollars to EURO, GBP,  ")
    print()
    while True:
        dollars = int(input("Enter amount of dollars: "))
        euro = round(dollars * 0.97, 2)
        gbp = round(dollars * 0.79, 2)
        answer = input("convert to EURO or GBP ?").lower()
        if answer == 'euro':
            print(f"{dollars} dollars = {euro} EURO")
        elif answer == 'gbp':
            print(f"{dollars} dollars = {gbp} EURO")
        else:
            print("Invalid input!")


currency_convertor()
