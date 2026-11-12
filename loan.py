loan_amnt = float(input("Enter loan amount"))
years = int(input("Enter the numbers of year"))

month = years * 12
principal = loan_amnt / month
remaining_balance = loan_amnt 

#for loop
print("MONTH\tMONTHLY PAYMENT\tINTEREST\tPRINCIPAL\tREMAINING BALANCE")
for count in range (1, month+1):
    remaining_balance -= principal
    loan_int = remaining_balance * 0.00256
    monthly_pay = loan_int + principal
    #print(count, principal)or
    print(count, monthly_pay, loan_int, round(principal, 2), round(remaining_balance,2))
    print(f"|{count}\t|\t{round(monthly_pay,2)}\t\t|\t{round(loan_int,2)}\t\t|\t{round(principal,2)}\t\t|\t{round(remaining_balance)}\t\t|")

    print("total")