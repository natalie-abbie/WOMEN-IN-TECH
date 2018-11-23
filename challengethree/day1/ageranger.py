input = input("enter your age.")
age = int(input)
if age < 19:
    print("Your are a minor")
else:
    if age > 19 and age < 37:
        print("you are a youth")
    else:
        print("you are an elder")

