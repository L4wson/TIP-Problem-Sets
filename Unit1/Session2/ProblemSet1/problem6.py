# Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.
def count_less_than(numbers, threshold):
    counter = 0
    for i in numbers:
        if i > threshold:
            counter += 1
    print(counter)

count_less_than([12,8,2,4,4,10],5)
