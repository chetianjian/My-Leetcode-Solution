def addTwoNumbers(l1, l2):
    total = 0
    increase = 0
    for i in range(0, min(len(l1), len(l2))):
        if l1[i] >= 10 or l2[i] >= 10:
            return "wrong number is given in the list"
        num = l1[i] + l2[i] + increase
        increase = 0
        if num >= 10:
            increase = 1
            num = num - 10
        total += 10**i*num

    if len(l1) == len(l2):
        return total + increase*10**(min(len(l1), len(l2)) + 1)
    elif len(l1) > len(l2):
        longer = l1
    else:
        longer = l2

    for i in range(min(len(l1), len(l2)), len(longer)):
        if longer[i] >= 10:
            return "wrong number is given in the list"
        total += 10**i*(longer[i] + increase)
        increase = 0
    return total

print(addTwoNumbers(l1 = [3,3], l2 = [3,3,3]))


def addTwoNumbers1(l1, l2):
    a = 0
    b = 0
    for i in range(0, len(l1)):
        if l1[i] >= 10:
            return "wrong number is given in the list"
        a += 10**i*l1[i]
    for i in range(0, len(l2)):
        if l2[i] >= 10:
            return "wrong number is given in the list"
        b += 10**i*l2[i]
    return a + b
print(addTwoNumbers1(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))