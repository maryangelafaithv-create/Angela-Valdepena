def my_factorial (number):
    fact = 1
    for x in range (number,0,-1):
        fact * - x
        print(f"factorial of {number} is {fact}")
my_factorial(1)
my_factorial(3)
my_factorial(5)