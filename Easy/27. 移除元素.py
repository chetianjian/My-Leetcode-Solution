def removeElement1(nums, val):
    count = 0
    for i in nums:
        if i == val: count += 1
    for i in range(0, count):
        nums.remove(val)
    return nums


def removeElement2(nums, val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    return nums

def sdf(nums, val):
    for i in range(0, len(nums)):
        if i >= len(nums): break
        while nums[-1] == val: nums.pop()
        if nums[i] == val:
            nums[i], nums[-1] = nums[-1], nums[i]
            nums.pop()