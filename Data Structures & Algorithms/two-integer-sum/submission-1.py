class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, el in enumerate(nums):
            diff = target - el

            if diff in seen:
                return [seen[diff], index]
            seen[el] = index 
        return 0 
        