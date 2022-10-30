# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#  示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#  示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#  提示：
#  1 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁴



def merge(intervals):
    intervals.sort(key = lambda x:x[0])
    result = [intervals[0]]
    for r in intervals[1:]:
        l = result[-1]
        if r[0] <= l[1] <= r[1]:
            result[-1] = [l[0], r[1]]
        elif r[0] <= r[1] < l[1]:
            continue
        elif r not in result:
            result.append(r)
        else:
            continue
    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
