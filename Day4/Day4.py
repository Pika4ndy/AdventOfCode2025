""" Advent of Code 2025 - Day 4: Printing Departement
Author: Pika4ndy

Part I:
On a large grid, there is randomly placed rolls of paper. We want to identify which ones are accessible
Accessible: surrounded by less than 4 other rolls of paper.

Part II:
We extend the previous puzzle by repeating it until no rolls of paper are accessible anymore.

Difficulties encountered:
- Map the grid schema
- count the number of neighbor (indexError)
    -> I added one layer of 0 at the positive boundary of the grid, since the negative one just wrap to the end
"""
import numpy as np

sample = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

equiv_dict = {
    "." : 0,
    "@": 1
}

def sampleTest() -> None:
    global sample
    global equiv_dict

    count = 0

    lines = [x for x in sample.splitlines()]
    sample_input = []
    lines.append("." * len(lines[0]))

    for i, line in enumerate(lines):
        new_line = []
        for char in line:
            new_line.append(char)

        new_line.append('.')

        sample_input.append(list(map(lambda x : equiv_dict[x], new_line)))

    array = np.array(sample_input) # Just for visualization

    removed = 1
    while removed != 0:
        removed = 0
        for i, line in enumerate(sample_input[:-1]):
            for j, instance in enumerate(line[:-1]):
                if line[j-1] + line[j+1] + sample_input[i-1][j-1] + sample_input[i-1][j] + sample_input[i-1][j+1] + sample_input[i+1][j-1] + sample_input[i+1][j] + sample_input[i+1][j+1] < 4 and instance:
                    count += 1
                    print(f"Validated: ({i},{j})")
                    array[i][j] = 2
                    sample_input[i][j] = 0
                    removed += 1

    print(np.array(sample_input), end="\n\n")
    # print(array)
    print(count)

def main():
    global equiv_dict

    count = 0

    with open("Day4/Day4_input") as file:
        reader = file.read()

    lines = [x for x in reader.splitlines()]
    array = []
    lines.append("." * len(lines[0]))

    for i, line in enumerate(lines):
        new_line = []
        for char in line:
            new_line.append(char)

        new_line.append('.')

        array.append(list(map(lambda x : equiv_dict[x], new_line)))


    removed = 1
    while removed != 0:
        removed = 0
        for i, line in enumerate(array[:-1]):
            for j, instance in enumerate(line[:-1]):
                if line[j-1] + line[j+1] + array[i-1][j-1] + array[i-1][j] + array[i-1][j+1] + array[i+1][j-1] + array[i+1][j] + array[i+1][j+1] < 4 and instance:
                    count += 1
                    array[i][j] = 0
                    removed += 1

    print(count)

if __name__ == '__main__':
    main()