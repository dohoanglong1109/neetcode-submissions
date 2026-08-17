class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums_dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums_dict:
                result.append(nums_dict[diff])
                result.append(index)
                break
            nums_dict[value] = index
        return result