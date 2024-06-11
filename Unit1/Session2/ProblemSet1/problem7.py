# Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.
def get_evens(lst):
    evens_lst = []
    for i in lst:
        if i % 2 == 0:
            evens_lst.append(i)
    return evens_lst

print(get_evens([1,2,3,4]))
