""" Advent of Code 2025 - Day 3: Lobby
Author: Pika4ndy

Part I:
In banks (bank: line) of batteries represented with their *joltage* (number between 1-9), we must select 2 batteries to activate in a way that their sum (by concatenation)
represent the highest number possible. 

Part II:
Same thing from Part I, just that we select 12 batteries rather than 2.

Difficulties encountered:
- Selecting the 12 batteries together was difficult for me
    -> I created a list where a selector add the highest number from the bank and remove the last battery activated if the number is higher than it
        A countdown counter, verify if we didn't exceed the number of battery to remove 
"""
sample = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def sampleTest():
    global sample
    input_list:list[list[int]] = []

    for line in sample.splitlines(): 
        line_list = []
        for digit in line:
            line_list.append(int(digit))

        input_list.append(line_list)

    list_ = []

    for bank in input_list:
        highest = []
        to_delete = len(bank) - 12
        for joltage in bank:
            if to_delete > 0 and len(highest) and joltage > highest[-1]:
                highest.pop()
                to_delete -= 1

            highest.append(joltage)

        list_.append(int(''.join(highest[:12])))

    print(sum(list_))

def main():
    with open("Day3/Day3_input") as file:
        reader = file.read()
 
    input_list = []

    for line in reader.splitlines():
        line_list = []
        for digit in line:
            line_list.append(digit)

        input_list.append(line_list)


    # ------- My first approach --------- #
    # joltages_list = []
    # for bank in numbers_list:
    #     highest = 0
    #     for i, joltage in enumerate(bank):
    #         for rest in bank[i+1:]:
    #             if int(joltage + rest) > highest:
    #                 highest = int(joltage + rest)
    #     joltages_list.append(highest)

    # print(sum(joltages_list))

    joltages_list = []

    for bank in input_list:
        highest = []
        to_delete = len(bank) - 12
        for joltage in bank:
            while to_delete > 0 and len(highest) and joltage > highest[-1]:
                highest.pop()
                to_delete -= 1

            highest.append(joltage)

        joltages_list.append(int(''.join(highest[:12])))

    print(sum(joltages_list))

if __name__ == '__main__':
    main()