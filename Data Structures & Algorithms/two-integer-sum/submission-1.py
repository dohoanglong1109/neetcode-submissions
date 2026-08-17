class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums_dict:
                return [nums_dict[diff], index]
            nums_dict[value] = index
