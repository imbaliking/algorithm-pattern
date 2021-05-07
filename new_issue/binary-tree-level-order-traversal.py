def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    queue = [root]
    ret = [[]]
    last_father = root
    while len(queue) != 0:
        op_node = queue[0]
        queue.remove(op_node)
        if last_father is not None and (last_father.left == op_node or last_father.right == op_node):
            local_ret = [op_node.val]
            ret.append(local_ret)
            last_father = None
        else:
            ret[-1].append(op_node.val)
        if op_node.left is not None:
            queue.append(op_node.left)
            if last_father is None:
                last_father = op_node
        if op_node.right is not None:
            queue.append(op_node.right)
            if last_father is None:
                last_father = op_node

    return ret