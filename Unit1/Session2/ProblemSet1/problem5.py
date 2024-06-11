# Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.
def max_difference(lst):
    max_val = lst[0]
    min_val = lst[0] 

    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
            
    return max_val - min_val
numbers = [5,22,8,10,2]
print(max_difference(numbers))