#Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.
def print_negatives(lst):
    for i in lst:
        if i < 0:
            print(i)

print_negatives([3,-2,2,1,-5])

