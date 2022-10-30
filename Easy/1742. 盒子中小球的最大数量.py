def countBalls(lowLimit, highLimit):
    dic = {}

    def strSum(n):
        return sum(list(map(int, list(str(n)))))

    for i in range(lowLimit, highLimit + 1):
        numSum = strSum(i)
        dic[numSum] = dic.get(numSum, 0) + 1

    return max(dic.values())

print(countBalls(3, 5))