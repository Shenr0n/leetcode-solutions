/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

    if list1 == nil && list2 ==nil{
        return nil
    } else if list2 == nil{
        return list1
    }else if list1 == nil{
        return list2
    }

    var head, tail *ListNode

    if list1.Val < list2.Val{
        head, tail = list1, list1
        list1 = list1.Next
    } else {
        head, tail = list2, list2
        list2 = list2.Next
    }

    for list1!=nil && list2!=nil{
        if list1.Val < list2.Val{
            tail.Next = list1
            list1 = list1.Next
            tail = tail.Next
        } else{
            tail.Next = list2
            list2 = list2.Next
            tail = tail.Next
        }
    }

    if list1 != nil{
        tail.Next = list1
    } else{
        tail.Next = list2
    }

    return head
}
