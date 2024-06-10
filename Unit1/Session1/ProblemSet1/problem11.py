# Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).

def counter(stop):
    for i in range(stop+1):
        print(i)

counter(7)