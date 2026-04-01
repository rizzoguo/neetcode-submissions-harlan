class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            dictionary[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dictionary and dictionary[diff] != i:
                return [i, dictionary[diff]]
        
