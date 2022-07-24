def pivot_index(nums: list[int]):
    sum_of_array = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (sum_of_array - left_sum - x):
            return i
        left_sum += x
    return -1


test_array = [1, 7, 3, 6, 5, 6]
test_result = pivot_index(test_array)
print(test_result)
