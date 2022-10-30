def intToRoman(num):
    dic = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM", 1000: "M", 500: "D", 100: "C", 50: "L", 10: "X",
           5: "V", 1: "I"}
    result = ""
    num = list(map(int, list(str(num))))
    for i in range(len(num)):
        if num[i] == 0:
            continue
        elif num[i] in [1,4,5,9]:
            result += dic.get(num[i] * 10 ** (len(num) - i - 1))
        elif num[i] < 5:
            result += dic.get(10 ** (len(num) - i - 1)) * num[i]
        else:
            result += dic.get(5 * 10 ** (len(num) - i - 1)) + dic.get(10 ** (len(num) - i - 1)) * (num[i] - 5)
    return result


print(intToRoman(2964))