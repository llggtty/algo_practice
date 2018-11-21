# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] +nums[j]==target:
                return [i,j]
                break

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashMap=dict()
    for i,x in enumerate(nums):
        if target-x in hashMap:
            return [i, hashMap[target-x]]
        hashMap[x] = i

nums = [3,2,4]
target = 6
twoSum(nums, target)

