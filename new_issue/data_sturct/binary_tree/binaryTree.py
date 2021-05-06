class binaryTreeNode:

    def __init__(self,left_child,right_child,value):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_node(self):
        return self.right_child

    def get_value(self):
        return self.value
