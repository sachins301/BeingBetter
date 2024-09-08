class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quadruplet = []

        def kSum(k, nums, target):
            if k != 2:
                for i in range(len(nums) - k + 1):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    quadruplet.append(nums[i])
                    kSum(k - 1, nums[i+1:], target - nums[i])
                    quadruplet.pop()
                return
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quadruplet + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4, nums, target)
        return res