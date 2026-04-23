""" Advent of Code 2025 - Day 2: Gift Shop
Author: Pika4ndy

Part I:
Recognize a sequence of pattern repeated twice inside a range of numbers as invalid IDs. In the input, ranges are separated by comma(,) and IDs by dash(-)

How I did:
- The first thing to come to my mind is using regex to search for patterns even if I think other options are possible, regex is the easier one.

Part II:

Difficulties encountered:
- In part I, trying to match only the pattern repeated twice, part II was just coming back from that problem
"""
import re


sample = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def separateRangeIDs(input: str) -> list[list[int]]:
    ranges : list[str] = input.split(",")
    IDs = []

    for id in ranges:
        IDs.append(id.split("-"))

    for i, range in enumerate(IDs):
        for j, id in enumerate(range):
            IDs[i][j] = int(id)

    return IDs


def sampleTest() -> None:
    IDs = separateRangeIDs(sample)
    addition = 0

    for range_num in IDs:
        for number in range(range_num[0], range_num[1]+1):
            if re.fullmatch(r'(.+?)\1+', str(number)):
            # if re.fullmatch(r'(.+?)\1{1}', str(number)): # For part I
                print(number)
                addition += number

    # print("trouvé" if re.fullmatch(r"(.+?)\1{1}", "232323232323") else "pas trouvé")
    print(addition)

def main():
    with open("Day2/Day2_input") as file:
        reader = file.read()

    IDs = separateRangeIDs(reader)

    addition = 0

    for range_num in IDs:
        for number in range(range_num[0], range_num[1]+1):
            if re.fullmatch(r'(.+?)\1+', str(number)):
            # if re.fullmatch(r'(.+?)\1{1}', str(number)): # For part I
                addition += number

    print(addition)

if __name__ == '__main__':
    main()