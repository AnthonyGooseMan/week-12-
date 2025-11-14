# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list1 = [1,2,3,4,5]
print(my_list1)
print(type(my_list1))
# instead of typing a bunch  of variables we can put them in this list
# Makes our job easier
# Performance task answer:
print(my_list1[0])
print(my_list1[1:4])
print(my_list1[0:])
my_list1.append(6)
my_list1.append(7)
my_list1.append(8)
my_list1.extend([10,11,12,13,14])
print(my_list1)
# 500 more numbers
my_list1.extend(list(range(15, 515)))
print(my_list1)
my_list1.extend(list(range(516, 1116)))
print(my_list1)


new_list = ['a','b','c']
print(new_list)
new_list.append('d')
print(new_list)
removed_item = new_list.pop(1)
print(removed_item)
print(new_list)
removed_second_item = new_list.pop(1)
print(removed_second_item)
print(new_list)

numbers = [4,2,5,1, 3]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(2,10)
print(numbers)


my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.