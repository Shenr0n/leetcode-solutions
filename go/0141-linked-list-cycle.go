/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 //Floyd's tortoise and hare algorithm
 
func hasCycle(head *ListNode) bool {

    if head == nil || head.Next == nil {
        return false
    }

    tortoise, hare := head, head

    for hare != nil && hare.Next != nil {
        tortoise = tortoise.Next
        hare = hare.Next.Next

        if tortoise == hare{
            return true
        }
    }
    return false
}
