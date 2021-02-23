"""
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

    asks the user for two separate texts;
    checks whether, the entered texts are anagrams and prints the result.

Note:

    assume that two empty strings are not anagrams;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent
"""

word_one = input("Enter first word : ")
word_two = input("Enter second word : ")


def split(word):
    return [char.lower() for char in word]


def compare(list_one, list_two):
    return "Anagram" if sorted(list_one) == sorted(list_two) else "Not anagram"


first_word = split(word_one)
second_word = split(word_two)

print(compare(first_word, second_word))
