class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            j = i + 1
            if nums[i] == nums[j]:
                return True
        
        return False