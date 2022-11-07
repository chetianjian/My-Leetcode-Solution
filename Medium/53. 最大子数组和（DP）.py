# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#  子数组 是数组中的一个连续部分。

#  示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  示例 2：
# 输入：nums = [1]
# 输出：1
#
#
#  示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#  提示：
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


def maxSubArray(nums: list[int]) -> int:
    tmp = nums[0]
    high = tmp
    n = len(nums)
    for i in range(1, n):
        if tmp + nums[i] > nums[i]:
            high = max(high, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            high = max(high, tmp, tmp + nums[i], nums[i])
            tmp = nums[i]
    return high


print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray(nums=[1]))
print(maxSubArray(nums=[5, 4, -1, 7, 8]))
print(maxSubArray(nums=[-1]))


# Time Limit Exceeded
def maxSubArray1(nums: list[int]) -> int:
    dp = [max(nums)]
    for i in range(2, len(nums) + 1):
        dp.append(max(dp[-1], max([sum(nums[j:j + i]) for j in range(len(nums) - i + 1)])))
    return max(dp)


print(maxSubArray1(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray1(nums=[1]))
print(maxSubArray1(nums=[5, 4, -1, 7, 8]))
print(maxSubArray1(nums=[-1]))
