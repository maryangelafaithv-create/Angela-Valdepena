# age (integer)
# is_employed (boolean)
# credit score (integer)
# annual inncome (float)
# has_collateral (boolean)

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you employed? (True/False): "))
credit_score = float(input("Enter credit score ---> "))
annual_income = float(input("What is your annual salary ---> "))
has_collateral = bool(input("Do you have any collateral? (True/False): "))

if age >=21 and is_employed == True:
    print("you are approved for thhe loan")
    if credit_score >= 750:
        print("You have a high credit score")
        if annual_income >= 100000:
            base_rate = 4.5
            print("Your base interest rate is ", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is ", base_rate)
    elif credit_score >=600 and credit_score < 700:
        print("Your credit score is less than 750")
        if has_collateral == True:
            base_rate = 7.0
            print("Your base rate is" , base_rate)
        elif annual_income <=40000:
            print("Low income")
            base_rate = 9.0
            print("Your base rate" , base_rate)
    else:
        base_rate = 8.0
        print("Your base rate is" , base_rate)
elif credit_score < 600:
    print("Rejected: Credit score is to low")
else:
    print("Rejected: Ineligible for loan")