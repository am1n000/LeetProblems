/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head)
    {
        ListNode *slow = head;
        ListNode *fast = head;
        ListNode *temp1;
        ListNode *temp2;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        temp1 = slow;
        slow = slow->next;
        temp1->next = NULL;
        while (slow)
        {
            temp2 = slow->next;
            slow->next = temp1;
            temp1 = slow;
            slow = temp2;
        }
        while (temp1)
        {
            if (head->val != temp1->val)
                return (0);
            head = head->next;
            temp1 = temp1->next;
        }
        return (1);
    }
};