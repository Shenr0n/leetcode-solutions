/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func Max(x int, y int) int {
    if x >= y{
        return x
    }
    return y
 }
func maxDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }else {
        left:= maxDepth(root.Left)
        right:= maxDepth(root.Right)
        return Max(left, right) + 1
    }
}
