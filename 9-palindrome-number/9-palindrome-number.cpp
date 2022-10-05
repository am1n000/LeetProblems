class Solution {
public:
    bool isPalindrome(int x)
    {
        int temp = x;
        unsigned long rev = 0;
        if (x < 0)
            return (0);
        while (x)
        {
            rev *= 10;
            rev += x % 10;
            x /= 10;
        }
        if (rev == temp)
            return (1);
        return (0);
    }
};