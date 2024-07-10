def minion_game(string):
    stuart = 0
    kevin = 0
    for letter in range(len(string)):
        if string[letter].lower() in "aeiou":

            kevin += len(string) - letter

        else:

            stuart += len(string) - letter

    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Stuart", stuart)
    # your code goes here


if __name__ == "__main__":
    # s = input("Enter a string")
    minion_game("Banana")
