# Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.

def valid_palindrome(s):
    def is_palindrome_range(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # If there is a mismatch, check by skipping one character
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1
    return True