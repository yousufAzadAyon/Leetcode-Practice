package main

func searchInsert(nums []int, target int) int {
	l := -1
	r := len(nums) - 1
	for r-l > 1 {
		m := (l + r) >> 1
		if nums[m] >= target {
			r = m
		} else {
			l = m
		}
	}
	if nums[r] < target {
		r++
	}
	return r
}
