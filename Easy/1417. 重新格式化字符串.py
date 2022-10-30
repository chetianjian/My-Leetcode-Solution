s = "1e834nfix6230rnc1"

lst = list(s)

def checkInt(x):
    try:
        return int(x)
    except:
        return x

print(list(map(checkInt, lst)))
