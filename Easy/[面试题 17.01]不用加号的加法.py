# 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
#
#  示例:
#
#  输入: a = 1, b = 1
# 输出: 2
#
#  提示：
#
#  a, b 均可能是负数或 0
#  结果不会溢出 32 位整数
#  Related Topics 位运算 数学 👍 58 👎 0

import random

def add(a, b):
    dic = {'10': '1', '11': '2', '12': '3', '13': "4", '14': '5', '15': '6', '16': '7', '17': '8',
           '18': '9', '19': 'K0', '20': '2', '21': '3', '22': '4', '23': '5', '24': '6', '25': '7',
           '26': '8', '27': '9', '28': 'K0', '29': 'K1', '30': '3', '31': '4', '32': '5', '33': '6',
           '34': '7', '35': '8', '36': '9', '37': 'K0', '38': 'K1', '39': 'K2', '40': '4', '41': '5',
           '42': '6', '43': '7', '44': '8', '45': '9', '46': 'K0', '47': 'K1', '48': 'K2', '49': 'K3',
           '50': '5', '51': '6', '52': '7', '53': '8', '54': '9', '55': 'K0', '56': 'K1', '57': 'K2',
           '58': 'K3', '59': 'K4', '60': '6', '61': '7', '62': '8', '63': '9', '64': 'K0', '65': 'K1',
           '66': 'K2', '67': 'K3', '68': 'K4', '69': 'K5', '70': '7', '71': '8', '72': '9', '73': 'K0',
           '74': 'K1', '75': 'K2', '76': 'K3', '77': 'K4', '78': 'K5', '79': 'K6', '80': '8', '81': '9',
           '82': 'K0', '83': 'K1', '84': 'K2', '85': 'K3', '86': 'K4', '87': 'K5', '88': 'K6','89': 'K7',
           '90': '9', '91': 'K0', '92': 'K1', '93': 'K2', '94': 'K3', '95': 'K4', '96': 'K5','97': 'K6',
           '98': 'K7', '99': 'K8', "00":"0", "01": "1", "02": "2", "03":"3", "04": "4", "05": "5", "06": "6",
           "07":"7", "08": "8", "09": "9"}
    dic1 = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "K0"}
    dic2 = {'01': 'M9', '02': 'M8', '03': 'M7', '04': 'M6', '05': 'M5', '06': 'M4', '07': 'M3',
            '08': 'M2', '09': 'M1', '10': '1', '11': '0', '12': 'M9', '13': 'M8', '14': 'M7',
            '15': 'M6', '16': 'M5', '17': 'M4', '18': 'M3', '19': 'M2', '20': '2', '21': '1',
            '22': '0', '23': 'M9', '24': 'M8', '25': 'M7', '26': 'M6', '27': 'M5', '28': 'M4',
            '29': 'M3', '30': '3', '31': '2', '32': '1', '33': '0', '34': 'M9', '35': 'M8', '36': 'M7',
            '37': 'M6', '38': 'M5', '39': 'M4', '40': '4', '41': '3', '42': '2', '43': '1', '44': '0',
            '45': 'M9', '46': 'M8', '47': 'M7', '48': 'M6', '49': 'M5', '50': '5', '51': '4', '52': '3',
            '53': '2', '54': '1', '55': '0', '56': 'M9', '57': 'M8', '58': 'M7', '59': 'M6', '60': '6',
            '61': '5', '62': '4', '63': '3', '64': '2', '65': '1', '66': '0', '67': 'M9', '68': 'M8',
            '69': 'M7', '70': '7', '71': '6', '72': '5', '73': '4', '74': '3', '75': '2', '76': '1',
            '77': '0', '78': 'M9', '79': 'M8', '80': '8', '81': '7', '82': '6', '83': '5', '84': '4',
            '85': '3', '86': '2', '87': '1', '88': '0', '89': 'M9', '90': '9', '91': '8', '92': '7',
            '93': '6', '94': '5', '95': '4', '96': '3', '97': '2', '98': '1', '99': '0', "00": "0"}
    dic3 = {"0": "M9", "1": "0", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8"}

    res, bull = [], True
    a, b = str(a), str(b)

    if int(a) == 0 and int(b) ==0: return 0
    elif int(a) >= 0 and int(b) >= 0:
        if len(b) > len(a):
            a, b = b, a
        aa = a
        for i in range(len(b)):
            char = "".join((list(reversed(aa))[i], list(reversed(b))[i]))
            a = list(a)
            a.pop()
            a = "".join(a)
            value = dic.get(char)
            res.insert(0, value)
        for i in reversed(a):
            res.insert(0, i)

        while bull:
            last = 0
            for i in range(len(res)):
                if len(res[i]) == 2 and i == 0:
                    res[0] = res[0][1]
                    res.insert(0, "1")

                elif len(res[i]) == 2:
                    res[i] = res[i][1]
                    res[last] = dic1.get(res[last])
                last = i
            for i in range(len(res)):
                if len(res[i]) == 2:
                    break
            else: bull = False
        return int("".join(res))

    elif int(a) < 0 and int(b) < 0:
        minus = a[0]
        a, b = a[1:], b[1:]
        if len(b) > len(a):
            a, b = b, a
        aa = a
        for i in range(len(b)):
            char = "".join((list(reversed(aa))[i], list(reversed(b))[i]))
            a = list(a)
            a.pop()
            a = "".join(a)
            value = dic.get(char)
            res.insert(0, value)
        for i in reversed(a):
            res.insert(0, i)

        while bull:
            last = 0
            for i in range(len(res)):
                if len(res[i]) == 2 and i == 0:
                    res[0] = res[0][1]
                    res.insert(0, "1")

                elif len(res[i]) == 2:
                    res[i] = res[i][1]
                    res[last] = dic1.get(res[last])
                last = i
            for i in range(len(res)):
                if len(res[i]) == 2:
                    break
            else:
                bull = False
        res.insert(0, minus)
        return int("".join(res))

    elif int(a) < 0 or int(b) < 0:
        if int(b) > int(a):

            a, b = b, a

        if abs(int(a)) == abs(int(b)): return 0
        elif abs(int(a)) > abs(int(b)):
            b = b[1:]
            aa = a
            for i in range(len(b)):
                char = "".join((list(reversed(aa))[i], list(reversed(b))[i]))
                a = list(a)
                a.pop()
                a = "".join(a)
                value = dic2.get(char)
                res.insert(0, value)
            for i in reversed(a):
                res.insert(0, i)

            while bull:
                last = 0
                for i in range(len(res)):
                    if len(res[i]) == 2 and i == 0:
                        res[0] = res[0][1]
                        res.insert(0, "1")

                    elif len(res[i]) == 2:
                        res[i] = res[i][1]
                        res[last] = dic3.get(res[last])
                    last = i
                for i in range(len(res)):
                    if len(res[i]) == 2:
                        break
                else:
                    bull = False
            return int("".join(res))

        elif abs(int(a)) < abs(int(b)):
            minus = b[0]
            b = b[1:]
            a, b = b, a
            aa = a
            for i in range(len(b)):
                char = "".join((list(reversed(aa))[i], list(reversed(b))[i]))
                a = list(a)
                a.pop()
                a = "".join(a)
                value = dic2.get(char)
                res.insert(0, value)
            for i in reversed(a):
                res.insert(0, i)

            while bull:
                last = 0
                for i in range(len(res)):
                    if len(res[i]) == 2 and i == 0:
                        res[0] = res[0][1]
                        res.insert(0, "1")
                    elif len(res[i]) == 2:
                        res[i] = res[i][1]
                        res[last] = dic3.get(res[last])
                    last = i
                for i in range(len(res)):
                    if len(res[i]) == 2:
                        break
                else:
                    bull = False
            res.insert(0, minus)
            return int("".join(res))
    return int("".join(res))


for i in range(-10000000,10000000):
    m, n = random.randint(-10000000,10000000), random.randint(-10000000,10000000)
    try:
        if add(m, n) == m+n:
            continue
    except:
        print(m, n)
        break