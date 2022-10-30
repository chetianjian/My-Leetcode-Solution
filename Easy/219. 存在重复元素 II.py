# 给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i和j，使得nums [i] = nums [j]，并且 i 和 j的差的 绝对值 至多为 k。
# 示例 1:
# 输入: nums = [1,2,3,1], k = 3
# 输出: true

# 示例 2:
# 输入: nums = [1,0,1,1], k = 1
# 输出: true

# 示例 3:
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false

def containsNearbyDuplicate(nums, k):
    if len(nums) == len(list(set(nums))): return False
    for i in set(nums):
        position_lst = [j for j in range(len(nums)) if nums[j] == i]
        if len(position_lst) == 1:
            continue
        else:
            index_diff_lst = [position_lst[k + 1] - position_lst[k] for k in range(len(position_lst) - 1)]
        if min(index_diff_lst) > k:
            continue
        else:
            return True
    return False