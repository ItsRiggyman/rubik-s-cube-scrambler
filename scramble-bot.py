import random
import sys
import os


def main():
    scramble = []

    moves = int(input("Please enter the ammount of moves you would like in your scramble: "))

    notation = ["L", "L'", "L2", "R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2", "F",
                "F'", "F2", "B", "B'", "B2", "M", "M'", "M2"]

    for i in range(moves):
        if not bool(scramble):
            move = random.choice(notation)
            scramble.append(move)
        else:
            move = random.choice(notation)
            if move == scramble[-1] or move[0] == scramble[-1][0]:
                scramble.pop()
                scramble.append(move)
            else:
                scramble.append(move)

    print("Your scramble is: " + ' '.join(scramble))
    answer = input("\nWould you like another scramble (Y/N): ")

    if answer.upper() == "Y":
        os.system("cls")
        main()
    else:
        print("Goodbye!")
        input("...")
        sys.exit()


if __name__ == '__main__':
    main()
