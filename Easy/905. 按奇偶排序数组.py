# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#  你可以返回满足此条件的任何数组作为答案。

#  示例：
#  输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。


def sortArrayByParity(nums) -> object:
    i, j = 0, len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) % 2 == 1:
            if nums[i] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
            continue
        elif nums[j] % 2 == 0:
            i = i + 1
        else:
            j = j - 1
    return nums

def sortArrayByParity2(nums) -> object:

    x, y = 0, len(nums) - 1

    def isodd(x):
        return True if nums[x] % 2 != 0 else False

    while x < y:
        if isodd(x):
            nums[x], nums[y], y = nums[y], nums[x], y - 1
        else:
            x += 1
    return nums


print(sortArrayByParity([2, 5, 67, 2, 1, 44, 24, 5, 25, 1, 5, 42, 8, 90, 1, 3, 5, 5424]))
print(sortArrayByParity2([2, 5, 67, 2, 1, 44, 24, 5, 25, 1, 5, 42, 8, 90, 1, 3, 5, 5424]))

