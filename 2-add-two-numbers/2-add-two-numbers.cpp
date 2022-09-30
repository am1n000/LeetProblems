// struct ListNode
// {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };



class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode *result = new ListNode;
        ListNode *ptr = result;
        div_t sum = {0, 0};
        while (sum.quot == 1 || l1 || l2)
        {
            if (l1)
            {
                sum.quot += l1->val; 
                l1 = l1->next;
            }
            if (l2)
            {
                sum.quot += l2->val; 
                l2 = l2->next;
            }
            sum = div(sum.quot, 10);
            ptr->next = new ListNode(sum.rem);
            ptr = ptr->next;
        }
        return (result->next);
    }
};