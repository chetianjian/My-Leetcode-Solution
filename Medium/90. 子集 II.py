# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

#  示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
#  示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#  提示：
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    from itertools import combinations
    lst = []
    for x in range(1, len(nums)):
        lst = lst + list(map(list, list(combinations(nums, x))))

    return list(map(lambda x: x if not x else list(map(int, x)), map(lambda x: [] if not x else x.split("@"), set(map(lambda x: "@".join(map(str, x)), map(sorted, [[]] + lst + [nums]))))))


print(subsetsWithDup(nums = [1,2,3,4,5,6,7,8,10,0]))
