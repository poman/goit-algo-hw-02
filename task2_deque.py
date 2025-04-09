from collections import deque

def is_palindrome(string):
    cleaned_string = ''.join(string.lower().split())
    char_deque = deque(cleaned_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Test cases
print("Radar є паліндромом: ", is_palindrome("Radar"))
print("Hello НЕ є паліндромом: ", is_palindrome("Hello"))
print("Was it a car or a cat I saw є паліндромом: ", is_palindrome("Was it a car or a cat I saw"))
