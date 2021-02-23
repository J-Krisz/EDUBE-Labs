secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Have a guess: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop")
    guess = int(input("Have a guess: "))
    if guess == secret_number:
        print(secret_number)
        print("Well done, muggle! You are free now.")