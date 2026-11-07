from  getpass import getpass

isLogin = False

while isLogin == False:
    username = input("INPUT USERNAME")
    password = getpass("INPUT PASSWORD")

    if username == "AngelaFaith" and password == "angelabsit1a":
        print("ACCESS GRANTED")
        isLogin = True
    else:
        print("ACCESS DENIED")