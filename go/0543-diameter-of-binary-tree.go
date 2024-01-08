/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func Max(x int, y int) int {
     if x>y{
         return x
     }
     return y
}

func diameterOfBinaryTree(root *TreeNode) int {
    var diameter int
    var depth func(node *TreeNode) int
        depth = func(node *TreeNode) int {
        if node == nil{
            return 0
        }
        left:= depth(node.Left)
        right:= depth(node.Right)
        
        diameter = Max(diameter, left+right)
        return (Max(left, right) + 1)
    }
    depth(root)
    return diameter
}
