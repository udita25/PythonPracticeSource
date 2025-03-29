#leetcode - Max Consecutive Ones
#Given a binary array nums, return the maximum number of consecutive 1's in the array.

nums = [int(x) for x in input('Enter binary numbers seperated by spaces: ').split()]

def findmaxconsecutiveones(nums):
    maxconsecutiveones = 0
    currentconsecutiveones = 0

    for x in nums:
        if x == 1:
            currentconsecutiveones += 1
            maxconsecutiveones = max(maxconsecutiveones, currentconsecutiveones)
        else:
            currentconsecutiveones = 0
    
    return maxconsecutiveones

result = findmaxconsecutiveones(nums)
print(result)

