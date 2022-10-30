# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
#  注意:
#  3 <= points.length <= 50.
#  不存在重复的点。
#  -50 <= points[i][j] <= 50.
#  结果误差值在 10^-6 以内都认为是正确答案。


def largestTriangleArea(points):
    import math
    from itertools import combinations

    # 海伦公式：S = sqrt(p(p-a)(p-b)(p-c))，其中p为三角形周长的一半，a,b,c分别为三角形边长
    def areaCal(x, y, z):
        p = (math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) +
             math.sqrt((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) +
             math.sqrt((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2)) / 2

        return math.sqrt(p * abs(p - math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)) *
                         abs(p - math.sqrt((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2)) *
                         abs(p - math.sqrt((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2)))

    return max(map(lambda x: areaCal(x[0], x[1], x[2]), combinations(points, 3)))

print(largestTriangleArea([[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]))
