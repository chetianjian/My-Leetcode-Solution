# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否
# 则返回 -1。
#
# 示例 1:
#  输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
#
#  示例 2:
#  输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#  提示：
#  你可以假设 nums 中的所有元素是不重复的。
#  n 将在 [1, 10000]之间。
#  nums 的每个元素都将在 [-9999, 9999]之间。



def search(nums, target):
    import math
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    if len(nums) == 2:
        for k in range(2):
            if nums[k] == target:
                return k
        else: return -1

    i, j = 0, len(nums)-1
    while i+1 < j:
        if nums[i] == target or nums[j] == target:
            return i if nums[i] == target else j
        elif nums[math.floor((i+j)/2)] == target:
            return math.floor((i+j)/2)
        elif nums[math.floor((i+j)/2)] < target:
            i = math.floor((i+j)/2)
        else:
            j = math.floor((i+j)/2)
    if nums[i] == target: return i
    elif nums[j] == target: return j
    return -1