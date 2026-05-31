class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        missing = None
        for i in range(len(nums)):
            missing = target - nums[i]

            if missing in nums:
                j = nums.index(missing)
                if i != j:
                    return sorted([i, j])
        return []
