class Node:
    def __init__(self, data, next_node):
        self._data = data
        self.next_node = next_node

    def get_data(self):
        return self._data

    def set_next_node(self, new_node):
        self.next_node = new_node


class Stack:
    def __init__(self, node, size):
        self._head_node = node
        self._size = size

    def pop_from_stack(self):
        top_node = self._head_node
        self._head_node = top_node._next_node
        return top_node.get_data

