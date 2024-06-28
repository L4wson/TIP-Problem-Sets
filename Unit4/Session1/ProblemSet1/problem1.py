#  Problem 1: Long Pressed

# Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

# The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.

# Use the two-pointer approach to solve the problem, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one string and a second pointer at the beginning of a second string, then increment each pointer conditionally to solve a problem.

def is_long_pressed(name, typed):
    i, j = 0, 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
        j += 1
    return i == len(name)

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
