
from initTree import init_tree_from_list

def preorder_traverse(node,op_func):
    op_func(node)
    if node.left_child != None:
        preorder_traverse(node.left_child,op_func)

    if node.right_child != None:
        preorder_traverse(node.right_child,op_func)


def preorder_traverse_nonRecursion(node,op_func):
    stack = [node]

    while len(stack) != 0:
        op_node = stack.pop()
        op_func(op_node)
        if op_node.right_child != None:
            stack.append(op_node.right_child)

        if op_node.left_child != None:
            stack.append(op_node.left_child)




if __name__ == "__main__":
    test_list = range(10)
    base_node = init_tree_from_list(test_list)
    def visit(node):
        print node.value

    preorder_traverse_nonRecursion(base_node,visit)