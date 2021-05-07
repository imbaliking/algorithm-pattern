def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    max_sum = -1001

    def division(node, max_sum):
        current_max = node.val
        left_max_sum = -1001
        right_max_sum = -1001
        left_max_path = 0
        right_max_path = 0
        if node.left is not None:
            left_max_sum, left_max_path = division(node.left, max_sum)

        if node.right is not None:
            right_max_sum, right_max_path = division(node.right, max_sum)

        max_path = max(current_max, current_max + left_max_path, current_max + right_max_path)
        max_sum = max(max_sum, max_path, current_max + left_max_path + right_max_path, left_max_sum, right_max_sum)
        return max_sum, max_path

    max_sum, max_path = division(root, max_sum)
    return max(max_sum, max_path)