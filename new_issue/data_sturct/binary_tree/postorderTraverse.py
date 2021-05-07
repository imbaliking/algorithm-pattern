from initTree import init_tree_from_list
def postorder_traverse(node,op_func):
    if node.left_child != None:
        postorder_traverse(node.left_child,op_func)

    if node.right_child != None:
        postorder_traverse(node.right_child,op_func)

    op_func(node)

def postorder_traverse_nonRecursion(node,op_func):
    stack = [node]
    root = node
    last_node = None

    while len(stack) != 0 or root != None:
        while root != None:
            stack.append(root)
            root = root.left_child
        op_node = stack[-1]
        if op_node.right_child == None or op_node.right_child == last_node:
            op_node = stack.pop()
            op_func(op_node)
            last_node = op_node
        else:
            root = op_node.right_child

if __name__ == "__main__":
    test_list = range(10)
    root_node = init_tree_from_list(test_list)
    def visit(node):
        print node.value
    postorder_traverse_nonRecursion(root_node,visit)