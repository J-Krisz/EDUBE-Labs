word_without_vowels = ""

user_word = input("Please enter a word. : ")
user_word = user_word.upper()
vowels = ['A', 'E', 'I', 'O', 'U']


for letter in user_word:
    if letter in vowels:
        continue
    else:
        word_without_vowels = letter

    print(word_without_vowels)

# Not returning all letter assinged to empty string when outside of the for loop
