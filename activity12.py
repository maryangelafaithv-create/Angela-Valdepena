#import getpass

username = 'angela'

password = 'valdepena123'

u = input("Enter Username --->  ")
p = getpass.getpass("Enter Password --->  ")


if username == u and password == p:
	print("ACCESS GRANTED")

else:
	print("ACCESS DENIED")