# 请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#  示例 1:
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#
#  示例 2:
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#
#  示例 3:
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
#
#  提示：
#  1 <= temperatures.length <= 10⁵
#  30 <= temperatures[i] <= 100


def dailyTemperatures(temperatures: list) -> list:
    def get_index(lst):
        try:
            return lst.index(True) + 1
        except:
            return 0

    temperatures = list(map(get_index, map(lambda x: list(
        map(lambda z: z > 0, map(lambda y: y - temperatures[x], temperatures[x + 1:]))),
                                           range(len(temperatures)))))
    return temperatures


def dailyTemperatures1(temperatures: list) -> list:
    length = len(temperatures)
    for i in range(length):
        count = 0
        for j in temperatures[i:]:
            if j <= temperatures[i]:
                count += 1
            else:
                temperatures[i] = count
                break
        else:
            temperatures[i] = 0
    return temperatures


print(dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures1(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
