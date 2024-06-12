# Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
# Use the function range() to loop through the list indices.

def print_indices(lst):
    for index in range(len(lst)):
        print(index)
print_indices([5,1,3,8,2])

