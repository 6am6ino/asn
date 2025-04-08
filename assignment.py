
my_list = []
print(f"Step 1: Empty list created: {my_list}")

# Step 2: Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"Step 2: After appending elements: {my_list}")

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print(f"Step 3: After inserting 15 at position 1: {my_list}")

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"Step 4: After extending with [50, 60, 70]: {my_list}")

# Step 5: Remove the last element from my_list
my_list.pop()
print(f"Step 5: After removing the last element: {my_list}")

# Step 6: Sort my_list in ascending order
my_list.sort()
print(f"Step 6: After sorting in ascending order: {my_list}")

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"Step 7: Index of value 30 in my_list: {index_of_30}")