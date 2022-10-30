def threeSum(nums):
    result = []
    nums.sort()
    if len(nums) < 3: return []

    for i in range(0, len(nums) - 2):
        if (nums[i] == nums[i-1] and i-1 >= 0) or (nums[i] + nums[-1] + nums[-2] < 0):
            continue
        if nums[i] > 0: return result

        for j in range(i+1, len(nums) - 1):
            if ((nums[j] == nums[j-1]) and (j-1 > i)) or (nums[i]+nums[j] > 0):
                continue

            if 0-nums[i]-nums[j] in nums[j+1:]:
                result.append([nums[i], nums[j], 0-nums[i]-nums[j]])
    return result


def threeSum1(nums):
    result = []
    nums.sort()
    n = len(nums)
    if len(nums) < 3: return result

    for i in range(n):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i-1]: continue
        L, R = i+1, n-1

        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                result.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L+1]:
                    L = L + 1
                while L < R and nums[R] == nums[R-1]:
                    R = R - 1
                L = L + 1
                R = R - 1
            elif nums[i] + nums[L] + nums[R] > 0:
                R = R - 1
            else: L = L + 1

    return result

print(threeSum1([0,0,0,0]))

