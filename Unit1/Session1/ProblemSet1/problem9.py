#  Write a function get_first() that takes in a list as a parameter and returns the first item in the list. Return None if the list is empty.
def get_first(lst):
    if lst:
        return lst[0]
    else:
        return None

print(get_first([3,1,6,7,5]))