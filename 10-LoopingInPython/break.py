while True:
    command = input("Type 'exit' to exit: ")
    if command.lower() == "exit":
        break

for x in range(1, 101):
    print(x)
    if x == 3:
        break

times = int(input("How many times do I need to tell you? "))

for time in range(times):
    print("DO THE THING!")
    if time >= 3:
        print("Are you even listening?")
        break
