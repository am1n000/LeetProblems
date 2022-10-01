class Solution {
public:
        std::string convert(std::string s, int numRows)
	{
		int len = s.length() - 1;
		int num = (numRows - 1) * 2;
		std::string result = "";
		if (len + 1 < 2 || numRows < 2 || numRows > len + 1)
			return (s);
		result += s[0];
		for (int i = num; i <= len ; i += num)
			result += s[i];
		for (int i = 1; i < numRows - 1; i++)
		{
			result += s[i];
			int j = num;
			while (j - i <= len)
			{
				if (j - i <= len)
					result += s[j - i];
				if (j + i <= len)
				    result += s[j + i];
				j+= num;
			}
		}
		result += s[numRows - 1];
		for (int i = num + numRows - 1; i <= len ; i += num)
			result += s[i];
		return (result);
    }

};