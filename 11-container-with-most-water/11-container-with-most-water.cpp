class Solution {
public:
    
    int maxArea(std::vector<int>& height)
	{
        int area = 0;
		int i = 0;
		int j = height.size() - 1;
		while (i < j)
		{
			if ((j - i) * std::min(height[i], height[j]) > area)
				area = (j - i) * std::min(height[i], height[j]);
			if (height[i] > height[j])
				j--;
			else
				i++;
		}
		return (area);
    }
};