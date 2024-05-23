import math


def goodPairs(lst):
    pair_count = {}
    for i, x in enumerate(lst):
        if x in pair_count:
            pair_count[x] += 1
        else:
            pair_count[x] = 1
    sum = 0
    for x in pair_count:
        if pair_count[x] > 1:
            sum += (pair_count[x] * (pair_count[x] - 1)) // 2
    return sum


def numIdenticalPairs(nums) -> int:
    output = 0
    dict_number = dict()
    for n in nums:
        if n in dict_number:
            output += dict_number[n]
            dict_number[n] += 1
        else:
            dict_number[n] = 1
    return output


print(numIdenticalPairs([1, 2, 3, 1, 1, 3, 1]))
