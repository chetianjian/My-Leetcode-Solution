# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

# 示例 1：
# 输入：nums = [1,3,2,2,5,2,3,7]
# 输出：5
# 解释：最长的和谐子序列是 [3,2,2,2,3]

def findLHS(nums):
    nums.sort()
    L = 0
    count = 0

    while L < len(nums) - 1:
        if nums[L] == nums[L + 1] or nums[L + 1] > nums[L] + 1:
            L = L + 1
            continue
        else:
            count0 = sum(i == nums[L] or i == nums[L + 1] for i in nums)
            if count0 > count: count = count0
            L = L + 1
    return count


def findLHS2(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i]+1 not in nums and nums[i]-1 not in nums:
            nums.pop(i)
        if len(nums) == 0: return 0
    cat = list(set(nums))
    cat.sort()
    count = -1
    lst = [0, 1]
    for j in cat:
        count0 = sum(k-j in lst for k in nums)
        if count0 > count: count = count0
    return count
