def romanToInt(s):
    result = 0
    dic = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10,
           "V": 5, "I": 1}
    order = ("IV", "IX", "XL", "XC", "CD", "CM")

    for i in range(len(s)):
        if i not in [s.find(k) for k in order if s.find(k) != -1]:
            result += dic.get(s[i])
        else:
            result += dic.get(s[i] + s[i + 1]) - dic.get(s[i + 1])
    return result

print(romanToInt("MCDLXXVI"))
print(romanToInt("MMCMLXIV"))

