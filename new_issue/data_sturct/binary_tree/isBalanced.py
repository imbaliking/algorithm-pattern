from initTree import init_tree_from_list
def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    flag = True
    if root is None:
        return flag

    def division(node, depth, flag):
        if flag is False:
            return 0, False
        left_flag = True
        right_flag = True
        depth += 1
        left_depth = depth
        right_depth = depth
        if node.left_child is not None:
            left_depth, left_flag = division(node.left_child, depth, flag)
        if node.right_child is not None:
            right_depth, right_flag = division(node.right_child, depth, flag)
        if abs(right_depth - left_depth) > 1:
            flag = False
        else:
            flag = left_flag and right_flag
        return max(depth,left_depth, right_depth), flag

    max_depth, flag = division(root, 0, flag)
    return flag

if __name__ == "__main__":
    test_list = [1,2,3,4,5,6,None,8]
    root = init_tree_from_list(test_list)
    print isBalanced(root)