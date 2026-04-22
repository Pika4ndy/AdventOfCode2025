""" Advent of Code 2025 - Day 1: The Secret Entrance
Author: Pika4ndy

Part I:
We are searching the password of an entrance with an attached document and by using a dial.
The dial can turn from 0-99 and return back with a full turn, it begins at 50.
The document contains the way the dial should be turned.
The password is equal to the number of times is left pointing at 0 after any rotation of the sequence (=0 after rotating the dial).

What the code is doing:
- Compute the addition, modulo 100, of the rotation to the dial 
- Add the answer in a list after each sequence
- Count the number of 0 in the list

Part II:
Using the method 0x434C49434B, we do not check not only the number of times it ends on 0 but also the number of times it passes on 0.

What is added to the code:
- 

Difficulties I encountered:
- starting and ending on 0 caused me troubles >:(
    -> Resolved by imagining in mind what was happening: when turning to L, increment of 1 when starting from 0
    - when turning to the right, decrement of 1 when ending on 0
"""

sample = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

dial = 50

def sampleTest() -> None:
    """ This is a test with the sample """
    global dial
    global sample
    dial_list = [1]
    count = 0

    with open("Day1/Day1_test_input") as file:
        reader = file.read()

    

    for line in reader.splitlines():
        if line[0] == "L":
            dial -= int(line[1:])

            division = dial // 100 
            print(f"{line = }, {dial = }, {division = }")

            dial %= 100
            print(f"moduled {dial = }")

            if dial_list[-1] == 0:
                count += abs(division + 1)

            else:
                count += abs(division)

            print(f"{count = }\n")

            dial_list.append(dial)

                    

        else:
            dial += int(line[1:])

            division = dial // 100
            print(f"{line = }, {dial = }, {division = }")


            dial %= 100
            print(f"moduled {dial = }")

            if dial:
                count += division

            else:
                count += division - 1

            print(f"{count = }\n")
            dial_list.append(dial)


    print(dial_list)
    print(count)
    print(f"password = {dial_list.count(0) + count} ")

def main():
    global dial
    dial_list = [1]
    count = 0
    
    try:
        with open("Day1/Day1_input") as file:
            input = file.read()

    except FileNotFoundError:
        try:
            with open("./Day1_input") as file: # try opening the parent folder in VS Code if it doesn't work
                input = file.read()

        except FileNotFoundError:
            raise FileNotFoundError

    input = input.splitlines()

    for line in input:
        if line[0] == "L":
            dial -= int(line[1:])

            division = dial // 100 

            dial %= 100

            if dial_list[-1] == 0:
                count += abs(division + 1)

            else:
                count += abs(division)

            dial_list.append(dial)

                    

        else:
            dial += int(line[1:])

            division = dial // 100

            dial %= 100

            if dial:
                count += division

            else:
                count += division - 1

            dial_list.append(dial)

    password = dial_list.count(0) + count

    print(password) # Right answer: 


if __name__ == '__main__':
    main()