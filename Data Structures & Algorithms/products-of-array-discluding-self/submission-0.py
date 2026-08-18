class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        left = 1
        right = 1

        for i in range(n):
            if i == 0:
                continue
            left *= nums[i-1]
            output[i] = left

        for i in range(n-1, -1, -1):
            if i == (n-1):
                continue
            right *= nums[i+1]
            output[i] *= right

        return output 