class Solution {
public:
        std::string longestPalindrome(std::string s)
	{
		int start = 0;
		int len = 0;
		int a;
		int b;
		for (int  i = 0; i < s.length(); i++)
		{
			a = i;
			b = i;
			while (a <  s.length() && s[a] == s[a + 1])
				a++;
			i = a;
			while (a <  s.length()  && b > 0  && s[a + 1] == s[b - 1])
			{
				a++;
				b--;
			}
			if (len < a - b + 1)
			{
				len = a - b + 1;
				start = b;
			}
		}
		return (s.substr(start, len));
	}
};