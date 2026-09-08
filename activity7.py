#assignment operator

x = 2

n1 = eval(input("input a number ---> "))
total = n1 + x
n2 = eval(input("Input number --->"))
total = n1 + n2 + x
n3 = eval(input("Input number --->"))
total = n1 + n2 + x - n3
n4 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4
n5 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5
n6 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5 / n6
n7 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5 / n6 + n7
n8 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5 / n6 + n7 - n8
n9 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5 / n6 + n7 - n8 + n9
n10 = eval(input("Input number --->"))
total = n1 + n2 + x - n3 * n4 * n5 / n6 + n7 - n8 + n9 / n10

print("Total is -->", total)