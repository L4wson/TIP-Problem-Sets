# Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.

def get_last(lst):
    if lst:
        return lst[-1]
    return None
print(get_last([3,1,6,7,5]))