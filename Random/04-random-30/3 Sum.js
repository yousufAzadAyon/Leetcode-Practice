/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = (nums) => {
    if (!nums || nums.length < 3) {
        return [];
    }
    nums.sort((a, b) => a - b);
    const set = new Set();
    const result = [];
    for (let i = 0; i < nums.length - 2; i++) {
        let j = i + 1;
        let k = nums.length - 1;
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            if (sum < 0) {
                j++;
            } else if (sum > 0) {
                k--;
            } else {
                const s = `${nums[i]}-${nums[j]}-${nums[k]}`;
                if (!set.has(s)) {
                    set.add(s);
                    result.push([nums[i], nums[j], nums[k]]);
                }
                j++;
                k--;
            }
        }
    }
    return result;
};