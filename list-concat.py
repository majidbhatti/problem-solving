def getConcatenation(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums


print(getConcatenation([1, 2, 1]))
