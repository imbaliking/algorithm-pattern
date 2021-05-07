from initTree import init_tree_from_list
def dfs_recursion(node,op_func):
    op_func(node)
    if node.left_child != None:
        dfs_recursion(node.left_child,op_func)
    if node.right_child != None:
        dfs_recursion(node.right_child,op_func)

def dfs_division(node):
    ret = [node.value]
    right = []
    left = []
    if node.left_child != None:
        left = dfs_division(node.left_child)

    if node.right_child != None:
        right = dfs_division(node.right_child)

    ret += left
    ret += right
    return ret

if __name__ == "__main__":
    test_list = range(10)
    base_node = init_tree_from_list(test_list)
    def visit(node):
        print node.value

    print dfs_division(base_node)

