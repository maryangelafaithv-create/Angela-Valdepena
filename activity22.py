drama_type = ["horror", "romance", "thrill", "romcom"]
drama_title = []

while True:
    ans = input("do you know any drama ---> (yes/no)")

    if ans.lower() == "yes":
        print("what type is it? select from the list")
        for x in drama_type:
            print(x) #traversing a list

        a_type = input("type --->")

        title = input("what is the title of the drama---?")
        drama_title.append(title)
        continue
    else:
        print("thank you")
        break
