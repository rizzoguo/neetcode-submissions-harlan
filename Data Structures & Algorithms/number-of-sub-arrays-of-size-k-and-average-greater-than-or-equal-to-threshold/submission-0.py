class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        cur = sum(arr[:k])
        res = 1 if cur >= threshold else 0
    
        for i in range(k, len(arr)):
            cur += arr[i]
            cur -= arr[i - k]
            if cur >= threshold:
                res += 1
        
        return res
        