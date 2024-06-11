def flip_sign(lst):
    flipped_lst = []
    for i in lst:
        flipped_lst.append(i * -1)
    return flipped_lst

print(flip_sign([1,-2,-3,4]))