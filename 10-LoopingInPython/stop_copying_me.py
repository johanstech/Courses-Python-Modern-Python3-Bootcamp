stop = "stop copying me"

msg = input("Hey, how's it going?\n")
while msg.lower() != stop:
    msg = input(f"{msg}\n")

print("UGH FINE, you win...")
