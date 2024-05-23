# This is a sample Python script.
from collections import OrderedDict
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def printPairs(arr, sum):
    arr_size = len(arr)
    hashmap = {}
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if temp in hashmap:
            print("yes")
            return [list(hashmap.values())[0], i]
        hashmap[arr[i]] = i
    print("no")


def two_sum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i,x in enumerate(nums):
        if target-x in map:
            return [map[target-x], i]
        else:
            map[x]=i
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(two_sum([3,2,4], 6))
    print(two_sum([3,3],6))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
