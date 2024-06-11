# Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    print(lst)

find_divisors(6)

