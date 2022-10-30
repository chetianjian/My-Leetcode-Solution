# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。
#
#  示例 1：
# 输入：nums = [2,1,2]
# 输出：5
#
#  示例 2：
# 输入：nums = [1,2,1]
# 输出：0
#
#
#  提示：
#  3 <= nums.length <= 10⁴
#  1 <= nums[i] <= 10⁶


def largestPerimeter(nums: list[int]) -> int:
    nums = sorted(nums)
    i, j, k = len(nums) - 3, len(nums) - 2, len(nums) - 1
    while i >= 0:
        if nums[i] + nums[j] > nums[k]:
            return nums[i] + nums[j] + nums[k]
        else:
            i, j, k = i - 1, j - 1, k - 1
    return 0
