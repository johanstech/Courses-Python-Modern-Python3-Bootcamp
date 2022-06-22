nums = [1, 2, 3]

# append() adds an element to the end of the list
nums.append(4)  # nums[3]
nums.append([5, 6])  # nums[4] = nested list

# extend() extends the list with more elements from another list
nums.extend([5, 6, 7, 8])  # [..., 5, 6, 7, 8]

# insert() inserts an element at a specified index of a list
nums.insert(nums[7], 10)

for n in nums:
    print(n)
