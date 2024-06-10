# Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive). 

def sum_positive_range(stop):
    sum = 0
    for i in range(stop+1):
        sum += i
    return sum

print(sum_positive_range(6))