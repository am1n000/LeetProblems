class Solution {
public:
    int trap(std::vector<int>& height) 
	{
		int i = 0;
		int j = height.size() - 1;
		int maxleft = 0;
		int maxright = 0;
		int trap = 0;
		while (i < j)
		{
			if (height[i] <= height[j])
			{
				if (height[i] > maxleft)
					maxleft = height[i];
				else
				{
					trap += maxleft - height[i];
					i++;
				}
			}
			else
			{
				if (height[j] > maxright)
					maxright = height[j];
				else
				{
					trap += maxright - height[j];
					j--;
				}
			}
		}
		return (trap);
    }
};