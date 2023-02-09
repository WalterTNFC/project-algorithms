def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    if isinstance(nums[0], str) or nums[0] < 0:
        return False

    for i, x in enumerate(nums):
        if x in nums[:i]:
            return x

    return False
