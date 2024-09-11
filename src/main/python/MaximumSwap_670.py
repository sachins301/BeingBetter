class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [[int(i), pos] for pos, i in enumerate(str(num))]

        for i in range(len(nums)-1):
            m = max(nums[i+1:])
            if nums[i][0] < m[0]:
                nums[i], nums[m[1]] = nums[m[1]], nums[i]
                break
        nums = [str(n) for n, pos in nums]

        return int(''.join(nums))
