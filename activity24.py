flowers = ["rose", "tulips", "gumamela", "yellowbell"]
            #0      #1          #2          #3............


#dictionary
#key, value
flowers_d = {"red":"rose", "purple":"tulips", "pink":"gumamela", "yellow":"yellowbell"}

print(flowers[2])
print(flowers_d["purple"])

#transversing a dictionary

for x, y in flowers_d.items():
    print("key is",x,"-- value is",y)
