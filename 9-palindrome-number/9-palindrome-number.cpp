class Solution {
public:
    bool isPalindrome(int x)
    {
        int  rev = 0;
        if (x < 0 || (x != 0 && x % 10 == 0))
            return (0);
        while (x > rev)
        {
            rev = (rev * 10) + (x % 10);
            x = x / 10;
            // std::cout << rev << "  " << x << std::endl;
        }
        return (rev == x || x == rev / 10);
    }
};