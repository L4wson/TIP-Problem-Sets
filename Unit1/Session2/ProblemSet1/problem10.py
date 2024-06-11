# Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# 
def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(13)
