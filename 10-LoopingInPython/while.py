password = "purple"

msg = input("What's the best colour? ").lower()
while msg != password:
    msg = input("Uh nooo. What's the best colour? ").lower()
print("Correct!")

num = 1
while num < 11:
    print(num)
    num += 1
