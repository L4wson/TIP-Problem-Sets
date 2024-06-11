# Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

def doubled(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 2)
    return new_lst
print(doubled([1,2,3]))