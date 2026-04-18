class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0 
        res = []
        for r in range(k-1, len(nums)):
            m = float('-inf')
            for i in nums[l:r+1]:
                m = max(m, i)
            res.append(m)

            l += 1
        return res  


        