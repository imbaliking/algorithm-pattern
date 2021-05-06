#coding:utf-8
from binaryTree import binaryTreeNode

def init_tree_from_list(data_list):

    num = len(data_list)
    node_list = [0 for _ in range(num)]
    base_node = binaryTreeNode( None, None,data_list[0])
    node_list[0] = base_node
    for i in range(1,num):
        if data_list[i] == None:
            continue
        new_node = binaryTreeNode(None, None, data_list[i])
        node_list[i] = new_node
        # 定位父节点
        if i % 2 == 0:
            op_node = node_list[i/2 - 1]
            op_node.right_child = new_node
        else:
            op_node = node_list[(i+1)/2 - 1]
            op_node.left_child = new_node


    return base_node

if __name__ == "__main__":
    test_list = range(3)
    base_node = init_tree_from_list(test_list)
    print base_node.value
    print base_node.left_child.value
    print base_node.right_child.value
