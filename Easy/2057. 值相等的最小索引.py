# 给你一个下标从 0 开始的整数数组 nums ，返回 nums 中满足 i mod 10 == nums[i] 的最小下标 i ；如果不存在这样的下标，返回 -1 。
# x mod y 表示 x 除以 y 的 余数 。


# 输入：nums = [4,3,2,1]
# 输出：2
# 解释：
# i=0: 0 mod 10 = 0 != nums[0].
# i=1: 1 mod 10 = 1 != nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# i=3: 3 mod 10 = 3 != nums[3].
# 2 唯一一个满足 i mod 10 == nums[i] 的下标

import math


def smallestEqual(nums):
    for i in range(math.floor(len(nums) / 10)):
        a = [j for j in range(len(nums[i * 10:i * 10 + 10]))
             if nums[i * 10:i * 10 + 10][j] == j]
        try:
            return i * 10 + a[0]
        except:
            continue
    for i in range(len(nums) - math.floor(len(nums) / 10) * 10):
        if nums[math.floor(len(nums) / 10) * 10 + i] % 10 == i:
            return math.floor(len(nums) / 10) * 10 + i
    return -1


def smallestEqual2(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]: return i
    return -1
