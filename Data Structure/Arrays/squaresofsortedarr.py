#Leetcode - Squares of a Sorted Array
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

nums = [int(x) for x in input('Enter numbers seperated by spaces: ').split()]
n = len(nums)
def sortedSquares(nums, n):
    for i in range(n):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    

sortedSquares(nums, n)
for i in range(n):
    print(nums[i], end = ' ')

