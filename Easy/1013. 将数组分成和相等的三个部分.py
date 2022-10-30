# 给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。
#  形式上，如果可以找出索引 i + 1 < j 且满足 (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] +
# arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
# 就可以将数组三等分。
#
#  示例 1：
# 输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#  示例 2：
# 输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
#
#  示例 3：
# 输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#  提示：
#  3 <= arr.length <= 5 * 10⁴
#  -10⁴ <= arr[i] <= 10⁴

# 未改进的算法
def canThreePartsEqualSum0(arr):
    if len(arr) < 100:
        i, j, avg = 1, len(arr) - 1, sum(arr) / 3
        while i < j:
            if not (sum(arr[:i]) == avg or sum(arr[j:]) == avg):
                i, j = i + 1, j - 1
            elif sum(arr[:i]) != avg:
                i = i + 1
            elif sum(arr[j:]) != avg:
                j = j - 1
            else:
                break
        return True if i < j else False


# 改进后：
def canThreePartsEqualSum(arr):
    i, j, avg = 0, len(arr) - 1, sum(arr) / 3
    left, right = arr[0], arr[len(arr) - 1]
    while i < j - 1:
        if left != avg and right != avg:
            i, j = i + 1, j - 1
            left, right = left + arr[i], right + arr[j]
        elif left != avg:
            i = i + 1
            left = left + arr[i]
        elif right != avg:
            j = j - 1
            right = right + arr[j]
        else:
            break
    return True if i < j - 1 else False

print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4] ))