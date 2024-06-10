#  Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).
def sum_range(start,stop):
    sum = 0
    for i in range(start,stop+1):
        sum += i
    return sum

print(sum_range(3,9))
