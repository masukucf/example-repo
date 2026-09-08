import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

choice = input('Enter either "investment" or "bond" from the menu above to proceed: ')

if choice.lower() == "investment":


    deposit = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan to invest: "))


    interest = input('Enter "simple" or "compound" interest: ')


    r = rate / 100

    if interest.lower() == "simple":

        A = deposit * (1 + r * years)
        print(f"The total amount after {years} years is R{A:.2f}")

    elif interest.lower() == "compound":
       
        A = deposit * math.pow((1 + r), years)
        print(f"The total amount after {years} years is R{A:.2f}")

    else:
        print('Invalid input. Please enter either "simple" or "compound".')

elif choice.lower() == "bond":

    # Get bond details
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months you plan to repay the bond: "))


    i = (rate / 100) / 12


    repayment = (i * present_value) / (1 - math.pow((1 + i), -months))

    print(f"Your monthly bond repayment will be R{repayment:.2f}")

else:
    print('Invalid input. Please enter either "investment" or "bond".')