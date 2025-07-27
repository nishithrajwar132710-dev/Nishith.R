def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

