#  Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
    for i in range(100+1):
        if i % 5 == 0:
            print(i)

multiples_of_five()