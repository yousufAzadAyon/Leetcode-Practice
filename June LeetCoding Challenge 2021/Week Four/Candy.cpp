#include<iostream>
#include<vector>
using namespace std;

class Solution {
    public:
        int candy(vector<int>& ratings) {
            int n=ratings.size();
            vector<int> left(n,1);
            vector<int> right(n,1);
            int i;
            for(i=1;i<n;i++)
            {
                if(ratings[i]>ratings[i-1])
                    left[i]=left[i-1]+1;
            }
            for(i=n-2;i>=0;i--)
            {
                if(ratings[i]>ratings[i+1])
                    right[i]=right[i+1]+1;
            }
            int total=0;
            for(i=0;i<n;i++)
            {
                total=total+max(left[i],right[i]);
            }
            return total;
        }
};