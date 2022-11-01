# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


#  示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#  示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#  示例 3：
# 输入：nums = [1]
# 输出：[[1]]


#  提示：
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  nums 中的所有整数 互不相同


def permute(nums: list[int]) -> list[list[int]]:
    from itertools import permutations
    return list(map(list, permutations(nums, len(nums))))


def permute0(nums: list[int]) -> list[list[int]]:
    def DP(p):
        return [lst[:i]+[nums[p-1]]+lst[i:] for lst in dp[p-1] for i in range(0, len(lst)+1)]

    length = len(nums)
    dp = [None, [[nums[0]]], [nums[:2], nums[1::-1]]]

    if length <= 2:
        return dp[length]
    else:
        for p in range(3, length + 1):
            dp.append(DP(p))
    return dp[-1]



print(permute(nums=[1, 2, 3]))
print(permute0([1, 2, 3, 4]))
