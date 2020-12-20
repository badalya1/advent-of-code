'''the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
'''

import sys
import itertools

def find_n(n, nums, total):
    all_combinations = itertools.combinations(nums, n)
    for combination in all_combinations:
        if sum(combination)==total:
            return combination
    raise RuntimeError()



def main(numbers):
    print(find_n(2, numbers, 2020))
    print(find_n(3, numbers, 2020))

    

if __name__=="__main__":
    nums = []
    with open("input.txt") as f:
        for line in f:
            nums.append(int(line))
    main(nums)
