# Inputs
name = input("Enter sender name: ")
type = input("Enter type of item: ")

isFragile = input("Is the item fragile? (True/False): ").lower() == "true"
weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
is_express = input("Is it express? (True/False): ").lower() == "true"
is_international = input("Is it international? (True/False): ").lower() == "true"


# 1. Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)


# 2. Evaluate Pricing Tiers
# First matching condition only
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


# Output
print("Sender Name:", name)
print("Type of Item:", type)
print("Fragile:", isFragile)
print("Weight:", weight, "kg")
print("Distance:", distance, "km")
print("Express:", is_express)
print("International:", is_international)
print("Base Cost: ${:.2f}".format(base_cost))
print("Total Shipping Charge: ${:.2f}".format(total))