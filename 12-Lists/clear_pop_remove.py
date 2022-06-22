nums = [1, 2, 3]

# clear() clears the entire list
nums.clear()  # nums = []

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop() removes and returns the last item in the list, or by index if provided
nums.pop()  # removes and returns 9
nums.pop(1)  # removes and return 2

# remove(x) removes first instance of list with value x
nums.remove(5)  # removes 5 from list

for n in nums:
    print(n)
