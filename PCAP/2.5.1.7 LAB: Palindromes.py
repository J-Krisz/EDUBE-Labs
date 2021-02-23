"""
Your task is to write a program which:

    asks the user for some text;
    checks whether the entered text is a palindrome, and prints result.

Note:

    assume that an empty string isn't a palindrome;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent;
    there are more than a few correct solutions - try to find more than one.

"""

text = input("Enter your text : ")

if text:
    check = text.lower().replace(" ", "")
    if len(check) > 1 and check == check[::-1]:
        print(f"{text} is palindrome")
    else:
        print(f"{text} is not a palindrome")
