def longestCommonPrefix(strs):
    shortest = min([len(i) for i in strs])
    while shortest >= 0:
        lst = list(map(lambda x: x[0:shortest], strs))
        if len(set(lst)) == 1:
            return lst[0]
        else:
            shortest -= 1
    return ""


def longestCommonPrefix2(strs):
    ans = ''
    for i in zip(*strs):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans

# zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
print(list(zip(["flower", "flow", "flavor"])))

# zip(*)用法相当于解压
print(list(zip(*["flower", "flow", "flavor"])))
