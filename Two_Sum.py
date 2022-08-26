class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            seenValue = {} #val -> ind
            for i, num in enumerate(nums):
                diff = target - num

                if diff in seenValue:
                    return([seenValue[diff], i])
                seenValue[num] = i
            return