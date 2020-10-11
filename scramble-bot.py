import random
import sys
import os
import json

def main():
    scramble = []

    with open("config.json") as f:
    	moves = int(json.loads(f.read())[0]['moves']) #Reads the preffered move count in the JSON file (default:15)

    notation = ["L", "L'", "L2", "R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2", "F",
                "F'", "F2", "B", "B'", "B2"]

    while len(scramble) != moves:
        if not bool(scramble):
            move = random.choice(notation)
            scramble.append(move)
        else:
            if scramble[-1][0] == "L" or scramble[-1][0] == "R":
                selection = [item for item in notation if item[0] not in ("R", "L")]
                move = random.choice(selection)
                scramble.append(move)
            elif scramble[-1][0] == "U" or scramble[-1][0] == "D":
                selection = [item for item in notation if item[0] not in ("U", "D")]
                move = random.choice(selection)
                scramble.append(move)
            else:
                selection = [item for item in notation if item[0] not in ("F", "B")]
                move = random.choice(selection)
                scramble.append(move)

    print("Your scramble is: " + ' '.join(scramble))
    answer = input("\nWould you like another scramble (Y/N): ")

    if answer.upper() == "Y":
        os.system("clear")
        main()
    else:
        print("Goodbye!")
        input("...")
        sys.exit()


if __name__ == '__main__':
    main()
