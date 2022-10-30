result = []

def combinationSum(candidates, target, path=None, s=0):
    global result
    if path is None: path = []
    candidates = sorted([candidates[i] for i in range(len(candidates)) if candidates[i] <= target], reverse = True)
    if len(candidates) == 0 or s == len(candidates): return result

    for i in range(s, len(candidates)):
        if sum(path) + candidates[i] == target:
            path.append(candidates[i])
            result.append(path)

        elif sum(path) + candidates[i] < target:
            path.append(candidates[i])
            return combinationSum(candidates, target, path, s)

        elif sum(path) + candidates[i] > target:
            s += 1
            return combinationSum(candidates, target, path, s)
    return result



print(combinationSum(candidates=[3, 6, 2, 1, 4], target=8))
