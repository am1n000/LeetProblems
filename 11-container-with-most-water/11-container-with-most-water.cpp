class Solution {
public:
    
    int maxArea(std::vector<int>& height)
	{
        int area = 0;
		int i = 0;
		int j = height.size() - 1;
		std::vector<int>::iterator left = height.begin();
		std::vector<int>::iterator right = --height.end();
		while (left != right)
		{
			if ((j - i) * std::min(*left, *right) > area)
				area = (j - i) * std::min(*left, *right);
			if (*left > *right)
			{
				j--;
				right--;
			}
			else
			{
				i++;
				left++;
			}
		}
		return (area);
    }
};