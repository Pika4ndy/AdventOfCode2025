""" Advent of Code 2025 - Day 5: Cafeteria
Author: Pika4ndy

Part I:


Part II:


Difficulties encountered:
- Memory management

Note:
- My first approach take some time to load
"""
import numpy

sample = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

def rangeGenerator(single_range: list[int]):
    start = single_range[0]
    end = single_range[1]
    n = start

    while n != end:
        yield n
        n += 1

def sampleTest() -> None:
    global sample

    lines = [line for line in sample.splitlines()]

    blank_line_index = lines.index('')

    ranges = lines[:blank_line_index]
    IDs = lines[blank_line_index+1:]
    ranges = [list(map(int, line.split("-"))) for line in ranges]
    IDs = [int(x) for x in IDs]

    print(ranges, IDs)
    count = 0

    for id in IDs:
        for single_range in ranges:
            if single_range[0] <= id <= single_range[1]:
                count += 1
                break

    fresh_meals = set()
    for single_range in ranges:
        generator = rangeGenerator(single_range)

        for number in generator:
            fresh_meals.add(number)

        print(fresh_meals)

    # Connect all ranges that overlap
    # for single_range in ranges.copy():
    #     print(f"\n{single_range = }")
    #     ranges2 = ranges.copy()
    #     ranges2.remove(single_range)
    #     print(f"{ranges2 = }")

    #     for single_range2 in ranges2:
    #         print(f"{single_range2 = }")
    #         if single_range2[0] < single_range[0] < single_range2[1]:
    #             if single_range[1] > single_range2[1]:
    #                 ranges[ranges.index(single_range2)][1] = single_range[1]

    #             ranges.remove(single_range)

    # Compute the length of each range
    # fresh_meals = 0
    # for single_range in ranges:
    #     fresh_meals += single_range[1] - single_range[0] + 1

    # for single_range in ranges:
    #     for number in range(int(single_range[0]), int(single_range[1])+1):
    #         fresh_meals.add(number)

    # print(fresh_meals)

    # count = 0
    # for id in IDs:
    #     if id in fresh_meals:
    #         count += 1

    # print(ranges)
    # print(fresh_meals)
    print(count)


def main():
    with open("Day5/Day5_input") as file:
        reader = file.read()

    lines = [line for line in reader.splitlines()]

    blank_line_index = lines.index('')

    ranges = lines[:blank_line_index]
    IDs = lines[blank_line_index+1:]


    ranges = [list(map(int, line.split("-"))) for line in ranges]
    IDs = [int(x) for x in IDs]

    count = 0
    for id in IDs:
        for single_range in ranges:
            if single_range[0] <= id <= single_range[1]:
                count += 1
                break
    
    ranges.sort(key=lambda x: x[0])

    # Connect all ranges that overlap

    merged = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])

        else:
            merged.append([start, end])

    # print(numpy.array(merged))

    # Compute the length of each range
    fresh_meals = sum(end - start + 1 for start, end in merged)

    print(fresh_meals)
    print(count) # for Part I

if __name__ == '__main__':
    main()