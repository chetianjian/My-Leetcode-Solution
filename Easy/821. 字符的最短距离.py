# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
#  返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的
# 字符 c 的 距离 。
#  两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
#
#  示例 1：
#
# 输入：s = "loveleetcode", c = "e"
# 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
# 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
# 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
# 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
# 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
# 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。



def shortestToChar(s, c):
    location = [i for i in range(len(s)) if s[i] == c]

    index, answer = 0, list(s)
    for i in range(len(answer[:location[index]])):
        answer[i] = abs(location[index] - i)

    while index + 1 < len(location):
        diff = location[index + 1] - location[index]
        if diff == 1:
            answer[location[index + 1]], answer[location[index]] = 0, 0
            index += 1
            continue

        elif diff % 2 == 1:  # 说明它们隔着偶数个元素
            answer[(location[index]):int(location[index] + (diff - 1) / 2 + 1)] = list(
                range(0, int((diff - 1) / 2 + 1)))
            answer[(location[index + 1] - int((diff - 1) / 2)):(location[index + 1] + 1)] = list(
                range(int((diff - 1) / 2), -1, -1))

        else:
            answer[location[index]:int(location[index] + diff / 2 + 1)] = list(range(0, int(diff / 2 + 1)))
            answer[(location[index + 1] - int(diff / 2) + 1):(location[index + 1] + 1)] = list(
                range(int(diff / 2) - 1, -1, -1))
        index = index + 1
    answer[location[index]:] = list(range(0, len(answer) - location[index]))

    return answer