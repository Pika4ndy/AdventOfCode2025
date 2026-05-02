""" Advent of Code 2025 - Day 6: Trash Compactor
Author: Pika4ndy

Part I:
We are somehow blocked in a trash compactor, a cephalod family can help us open the door and while waiting they want us to help their child with their math homework.
(Cephalopods math works the same as ours)
The homework only consist of adding or multiplicating the numbers of each column of numbers according to the character at the bottom (+|*)

Part II:
It looks like cephalopod's reading of math is different from ours: each digits has their own column and is read from right to left. The numbers are defined by their column and the highest rank of number is at the top.
E.g.: 
2
3 -> 234
4


Difficulties encountered:
- Reading column numbers, and separating each calculation
"""

sample = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

def sampleTest():
    global sample

    lines = sample.splitlines()

    input = []

    for line in lines:
        input.append([char for char in line])

    operator_list = input[-1]

    while operator_list.count(' '):
        operator_list.remove(' ')

    print(f"{operator_list = }")

    answers = []
    calculation = []
    calculation_index = 0

    for i in range(len(input[0])): # i: column
        actual_number : str = ''

        for line in input[:-1]: # j: line
            actual_number += line[i] # Concatenating the strings of each line of the i-th column

        if actual_number.strip() != '': # if it is not the end of that calculation (each calculation is separated with one column of blank space so it just verify is the column is blank)
            calculation.append(int(actual_number.strip()))

        else:
            match operator_list[calculation_index]:
                case "+":
                    answers.append(sum(calculation))
                    calculation = []

                case "*":
                    number = 1
                    for num in calculation:
                        number *= num

                    answers.append(number)
                    calculation = []

                case _:
                    print("There is an error, the program didn't detected any operator.")
                    print(f"{calculation_index}")

            calculation_index += 1

    if len(calculation):
        match operator_list[calculation_index]:
                case "+":
                    answers.append(sum(calculation))
                    calculation = []

                case "*":
                    number = 1
                    for num in calculation:
                        number *= num

                    answers.append(number)
                    calculation = []

                case _:
                    print("There is an error, the program didn't detected any operator.")
                    print(f"{calculation_index}")

    print(calculation_index)
    print(calculation)
    print(answers)
    print(sum(answers))

    # for line in chars:
    #     while line.count(""):
    #         line.remove('')

    # calculation_len = len(chars[0])

    # print(chars)

    # Part I
    # for i in range(calculation_len):
    #     calculation = []
    #     for value in chars:
    #         calculation.append(value[i])

    #     match calculation[-1]:
    #         case "+":
    #             answers.append(sum(map(int, calculation[:-1])))

    #         case "*":
    #             product = 1
    #             for number in map(int, calculation[:-1]):
    #                 product *= number

    #             answers.append(product)

    #         case _:
    #             ...

def main():

    with open("Day6/Day6_input") as file:
        reader = file.read()

    lines = reader.splitlines()

    input = []

    for line in lines:
        input.append([char for char in line])

    operator_list = input[-1]

    while operator_list.count(' '):
        operator_list.remove(' ')

    print(f"{operator_list = }")

    answers = []
    calculation = []
    calculation_index = 0

    for i in range(len(input[0])): # i: column
        actual_number : str = ''

        for line in input[:-1]: # j: line
            actual_number += line[i] # Concatenating the strings of each line of the i-th column

        if actual_number.strip() != '': # if it is not the end of that calculation (each calculation is separated with one column of blank space so it just verify is the column is blank)
            calculation.append(int(actual_number.strip()))

        else:
            match operator_list[calculation_index]:
                case "+":
                    answers.append(sum(calculation))
                    calculation = []

                case "*":
                    number = 1
                    for num in calculation:
                        number *= num

                    answers.append(number)
                    calculation = []

                case _:
                    print("There is an error, the program didn't detected any operator.")
                    print(f"{calculation_index}")

            calculation_index += 1

    if len(calculation):
        match operator_list[calculation_index]:
                case "+":
                    answers.append(sum(calculation))
                    calculation = []

                case "*":
                    number = 1
                    for num in calculation:
                        number *= num

                    answers.append(number)
                    calculation = []

                case _:
                    print("There is an error, the program didn't detected any operator.")
                    print(f"{calculation_index}")

    print(sum(answers))

if __name__ == '__main__':
    main()