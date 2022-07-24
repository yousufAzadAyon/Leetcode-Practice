def running_sum(nums: list[int]):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


test_array = [1, 2, 3, 4]
result = running_sum(test_array)
print(result)
