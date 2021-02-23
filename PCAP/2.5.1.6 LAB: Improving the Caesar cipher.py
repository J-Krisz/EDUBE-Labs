"""
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit
harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all
non-alphabetical characters should remain untouched.

Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range
    1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool
    you!)
    prints out the encoded text.
"""

text = input("Enter text for encryption here : ")
shift = 0
cipher = ''

while not shift:
    try:
        shift = int(input("Enter a shift value between 1-25 : "))
        if shift not in range(1, 26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Wrong shift value")


for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord("A")
        else:
            first = ord("a")
            code -= first
            code %= 26
            cipher += chr(first + code)
    else:
        cipher += char

print(cipher)