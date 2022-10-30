# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。

# 输入: nums = [1,3,5,6], target = 5
# 输出: 2

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.sort()
        L = 0
        if target <= nums[0]:
            return 0
        else:
            while L < len(nums) - 1 and target > nums[L]:
                if target > nums[L + 1]:
                    L = L + 1
                    continue
                else:
                    return L + 1
            return len(nums)