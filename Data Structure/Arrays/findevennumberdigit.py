#leetcode - Find Numbers with Even Number of Digits
#Given an array nums of integers, return how many of them contain an even number of digits.


nums = [int(x) for x in input('Enter numbers seperated by spaces: ').split()]

def findnumb(nums):
    count = 0
    for i in nums:
        numberofdigits = len(str(abs(i)))
        if numberofdigits % 2 == 0:
            count += 1
    
    return count

result = findnumb(nums)
print(result)