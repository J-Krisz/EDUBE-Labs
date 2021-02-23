secret_word = 'chupacabra'


while True:
    word = input("Enter a word.: ")
    if word == secret_word:
        print("You've succefully left the loop")
        break
    else:
        print("Guess again!!")
