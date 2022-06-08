# ask for age
print("How old are you?")
age = input()

if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink!")
    elif age >= 18:
        print("You can enter but not drink.")
    else:
        print("You're too young to enter.")
else:
    print("Please enter your age.")
