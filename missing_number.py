"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_sum = set(nums)
        n_sum_complete = set(range(0,max(nums)+1))
        num = n_sum_complete - n_sum
        if len(num) >0:
            return num.pop()
        else:
            return max(nums)+1


"""
length=len(nums)
return ((length**2+length)>>1)-sum(nums)
"""
