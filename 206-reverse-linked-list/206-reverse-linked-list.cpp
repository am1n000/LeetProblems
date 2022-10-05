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
    ListNode* reverseList(ListNode* head)
    {
        ListNode *new_head;
        ListNode *temp;
    
        if (!head || !head->next)
            return (head);
        new_head = head;
        head = head->next;
        new_head->next = NULL;

        while (head)
        {
            temp = head->next;
            head->next = new_head;
            new_head = head;
            head = temp;
        }
        return (new_head);
    }
};