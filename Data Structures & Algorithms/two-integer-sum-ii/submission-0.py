class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        start, end = 0, len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1 
            else:
                res.append(start + 1)
                res.append(end + 1)
                return res
            
        return res
                