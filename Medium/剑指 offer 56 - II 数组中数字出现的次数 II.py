# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4
#
# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#
#
#  限制：
#  1 <= nums.length <= 10000
#  1 <= nums[i] < 2^31


def singleNumber(nums: list[int]) -> int:
    length = len(set(nums))
    for i in set(nums):
        nums.remove(i)
        if len(set(nums)) != length:
            return i


print(singleNumber([9, 1, 7, 9, 7, 9, 7]))


def singleNumber1(nums: list[int]) -> int:
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    for i in dic.keys():
        if dic[i] != 3:
            return i


print(singleNumber1([3, 4, 3, 3]))
