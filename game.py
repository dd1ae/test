import random


def main():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Take a guess: ")
        try:
            guess_int = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess_int < number:
            print("Too low!")
        elif guess_int > number:
            print("Too high!")
        else:
            print("Correct! You guessed my number.")
            break


if __name__ == "__main__":
    main()
