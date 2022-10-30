# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai)
# 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器。

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

def maxArea(height):
    if max(height) == 0: return 0
    Area, i, j = 0, 0, len(height) - 1
    while i < j:
        if min(height[i], height[j]) * (j - i) > Area:
            Area = min(height[i], height[j]) * (j - i)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return Area
