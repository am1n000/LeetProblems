class Solution {
public:
    
    int maxArea(std::vector<int>& height)
	{
        int area = 0;
		int i = 0;
		int j = height.size() - 1;
		while (i < j)
		{
            int minim = std::min(height[i], height[j]);
			if ((j - i) * minim > area)
            	area = (j - i) * minim;
            while (height[i] <= minim && i < j) i++;
            while (height[j] <= minim && i < j) j--;
		}
		return (area);
    }
};