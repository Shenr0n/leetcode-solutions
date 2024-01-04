/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {

    var previousNode *ListNode
    currentNode := head

    for currentNode != nil {
        nextNode := currentNode.Next
        currentNode.Next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    }
    return previousNode
}
