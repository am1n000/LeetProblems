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
public : 
    
    ListNode* reverseBetween(ListNode* head, int left, int right)
    {
        ListNode *ptr;
        ListNode *before_left = head;
        ListNode *left_end = head;
        ListNode *temp1;
        ListNode *temp2;

        int i = 1;
        if (!head || !head->next || left == right)
            return (head);
        ptr = head;
        while (left != i)
        {
            before_left = head;
            head = head->next;
            i++;
        }
        left_end = head;
        temp1 = head;
        head = head->next;
        while (i < right)
        {
            temp2 = head->next;
            head->next = temp1;
            temp1 = head;
            head = temp2;
            i++;
        }
        if (left == 1)
            ptr = temp1;
        else
            before_left->next = temp1;
        left_end->next = head;
        return (ptr);
    }
};