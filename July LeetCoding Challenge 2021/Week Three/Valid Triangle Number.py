class Solution(object):
    def triangleNumber(self, nums):
        nums = sorted (nums)
        print (nums)
        count = 0
        for i in range(0, len (nums) -2):
            if 0== nums [i]:
                continue ;
            k= i+2
            for j in range (i+1,len (nums)-1):
                while( k< len (nums) and nums[i] + nums [j] > nums[k] ):
                    k= k+ 1
                count = count + (k-j-1)
        return count 