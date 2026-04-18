class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        total_len = m + n 
        is_even = total_len % 2 == 0
        max_len = (total_len >> 1) 
       
        new_nums =[] 
        idx = 0 
        p1, p2 = 0 ,0  

        while idx <= max_len and p1 <= m -1 and p2 <= n - 1: 
            if nums1[p1] < nums2[p2] :
                new_nums.append(nums1[p1])
                p1 += 1
            else:
                new_nums.append(nums2[p2])
                p2 += 1
            idx += 1
        
        while idx <= max_len and p1 <= m -1: 
            new_nums.append(nums1[p1])
            p1 += 1
            idx += 1

        while idx <= max_len and p2 <= n-1 :
            new_nums.append(nums2[p2])
            p2 += 1
            idx += 1     
            
        if is_even :
            return (new_nums[idx-1] + new_nums[idx -2]) / 2
        else:
            return new_nums[idx-1] 


        