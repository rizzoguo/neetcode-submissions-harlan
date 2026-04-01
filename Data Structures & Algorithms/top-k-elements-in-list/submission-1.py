class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resdict = defaultdict(int)
        nums = sorted(nums)
        prev = nums[0]
        resdict[prev] += 1
        

        for i in range(1, len(nums)):
            
            if nums[i] == prev:
                resdict[prev] += 1
            
            else:
                prev = nums[i]
                resdict[prev] += 1

        sorted_dict = sorted(resdict.items(), key = lambda x: x[1], reverse = True)
        k_res = [item[0] for item in sorted_dict[:k]]
        return k_res