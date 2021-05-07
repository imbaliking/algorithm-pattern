from initTree import init_tree_from_list
def inorder_traverse(node,op_func):

    if node.left_child != None:
        inorder_traverse(node.left_child,op_func)

    op_func(node)

    if node.right_child != None:
        inorder_traverse(node.right_child,op_func)


def inorder_traverse_nonResursion(node,op_func):
    stack = []
    root = node
    while len(stack) != 0 or root != None:
        while root != None:
            stack.append(root)
            root = root.left_child
        op_node = stack.pop()
        op_func(op_node)
        root = op_node.right_child


if __name__ == "__main__":
    test_list = range(10)
    root_node = init_tree_from_list(test_list)
    def visit(node):
        print node.value
    inorder_traverse_nonResursion(root_node,visit)