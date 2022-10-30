# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
