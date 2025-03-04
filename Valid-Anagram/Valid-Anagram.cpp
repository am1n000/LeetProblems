class Solution {
public:
    bool isAnagram(string s, string t)
    {
        int min = 255;
        int max = 0;
        int trac1[255] = {0};
        int trac2[255] = {0};
        size_t len_s = s.size();
        size_t len_tt = t.size();
        if (len_s != len_tt)
            return (false);
        int i = -1;
        while (++i < len_s)
            trac1[s[i]]++;
        i = -1;
        while (++i < len_tt)
            trac2[t[i]]++;
        i = -1;
        while (++i < 255)
        {
            if (trac1[i] != trac2[i])
                return (false);
        }
        return (true);
    }
};
