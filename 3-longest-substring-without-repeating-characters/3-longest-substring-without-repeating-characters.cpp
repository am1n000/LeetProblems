class Solution {
public:
    
    int lengthOfLongestSubstring(std::string s)
    {
        int len = 0;
        int index = -1;
        std::vector<int> arr(256,-1);

        for (int i = 0; i < s.length(); i++)
        {
            if (arr[s[i]] > index)
                index = arr[s[i]];
            arr[s[i]] = i;
            len = std::max(len, i - index);
        }
        return (len);
    }   
};