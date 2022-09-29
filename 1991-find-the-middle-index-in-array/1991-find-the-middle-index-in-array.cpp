class Solution {
public:
    int findMiddleIndex(std::vector<int>& nums)
    {
        if (nums.size() == 1)
            return (0);
        int sum1 = std::accumulate(nums.begin(), nums.end(), 0);
        int sum2 = 0;
        int i = 0;
        std::vector<int>::iterator f_index = nums.begin();
        while (f_index != nums.end())
        {
            sum1 -= *f_index;
            if (sum1 == sum2)
                return (i);
            sum2 += *f_index;
            f_index++;
            i++;
        }
        return (-1);
    }
};