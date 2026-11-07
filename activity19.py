isExpensive = False #boolean variable

while isExpensive == False:
    x = bool(input("Is the gas price still expensive? (True/False)"))

    if x == True:
        print("How expensive?")

    else:
        break