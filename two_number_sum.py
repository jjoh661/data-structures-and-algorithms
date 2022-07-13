# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

array1 = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum1 = 10

print(twoNumberSum(array1, targetSum1))
