from initTree import init_tree_from_list
def bfs(node,op_func):
    queue = [node]

    while len(queue) != 0:
        op_node = queue[0]
        queue.remove(op_node)
        op_func(op_node)
        if op_node.left_child is not None:
            queue.append(op_node.left_child)
        if op_node.right_child is not None:
            queue.append(op_node.right_child)


if __name__ == "__main__":
    test_list = range(10)
    base_node = init_tree_from_list(test_list)
    def visit(node):
        print node.value

    bfs(base_node,visit)