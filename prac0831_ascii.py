## chr() - returns the character
print(chr(68))

## ord() returns the decimal
print(ord('D'))



'''
# Exercise 1: Sum of ASCII Values
# Write a Python program that calculates the sum of the ASCII values of 
all characters in a given string.
# Example input: text = "hello"
# Expected output: 532
'''
text = 'hello'
sum = 0
for i in text:
    num = ord(i)
    sum = sum + num
    print(num)

'''
# Exercise 2: Character from ASCII Value
# Write a Python program that takes an ASCII value as input and prints 
the corresponding character.
# Example input: ascii_value = 97
# Expected output: 'a'
'''
# Solution for Exercise 2
text = 97
b = chr(text)
print(b)

'''
# Exercise 3: Uppercase to Lowercase Conversion
# Write a Python program that converts an uppercase letter to its lowercase 
equivalent using ASCII values.
# Example input: letter = 'A'
# Expected output: 'a'
'''
# Solution for Exercise 3



'''
# Exercise 4: Lowercase to Uppercase Conversion
# Write a Python program that converts a lowercase letter to its 
uppercase equivalent using ASCII values.
# Example input: letter = 'b'
# Expected output: 'B'
'''


'''
# Exercise 5: ASCII Value Difference
# Write a Python program that calculates the difference between the 
ASCII values of two characters.
# Example input: char1 = 'a', char2 = 'd'
# Expected output: 3
'''


'''
# Exercise 6: Alphabetical Sequence
# Write a Python program that prints the next 5 characters in the ASCII 
sequence from a given character.
# Example input: start_char = 'x'
# Expected output: 'y', 'z', '{', '|', '}'
'''
text = 'x'
for i in range(1,6):
    a = ord(text)
    b = a + i
    c = chr(b)
    print(c)

'''
# Exercise 7: Sum of ASCII Values of Digits
# Write a Python program that calculates the sum of the ASCII values of all 
digit characters in a given string.
# Example input: text = "a1b2c3"
# Expected output: 150
'''
# ord()
text = "a1b2c3"
sum = 0

# loop through every character in the string
for i in text:
    if i.isdigit():
        sum = sum + ord(i)
print(sum)


'''
# Exercise 8: Replace Characters with ASCII Sum
# Write a Python program that replaces each character in a string with the 
sum of its ASCII value and a given integer.
# Example input: text = "abc", increment = 1
# Expected output: 'b', 'c', 'd'
'''


'''
# Exercise 1: Generate a Simple Password
# Write a Python program that generates a random password of a given length 
    using ASCII printable characters.
# Example input: length = 8
# Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# HINT: ASCII printable characters range from 33 to 126
'''
import random
pw = ""
for i in range(8):
    a = random.randint(33,126)
    b = chr(a)
    pw = pw + b 
print(pw)

