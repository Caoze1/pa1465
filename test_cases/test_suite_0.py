from collections import deque
import random

class BST:
    """Binary Search Tree"""
    class Node:
        """Node in BST"""
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        self._root = None

    def _insert_at_node(self, element, node: Node):
        if element > node.data:
            if node.right is None:
                node.right = self.Node(element)
            else:
                self._insert_at_node(element, node.right)
        elif element < node.data:
            if node.left is None:
                node.left = self.Node(element)
            else:
                self._insert_at_node(element, node.left)

    def insert(self, element):
        """Insert an element into bst"""
        if self._root is None:
            self._root = self.Node(element)
        else:
            self._insert_at_node(element, self._root)

    def _find_at_node(self, element, node: Node):
        if element > node.data:
            if node.right is None:
                return False
            return self._find_at_node(element, node.right)
        if element < node.data:
            if node.left is None:
                return False
            return self._find_at_node(element, node.left)
        return True

    def find(self, element):
        """Search for an element in tree. Returns true if element
        is in tree, otherwise false"""
        if self._root is None:
            return False
        return self._find_at_node(element, self._root)

    def _replace_node(self, node_old: Node, parent: Node, node_new: Node):
        if parent is None:
            self._root = node_new
        elif parent.left is not None and parent.left.data == node_old.data:
            parent.left = node_new
        else:
            parent.right = node_new

    def _move_max_node(self, node:Node, parent:Node):
        if node.right is None:
            max_value = node.data
            self._replace_node(node, parent, node.left)
            return max_value
        return self._move_max_node(node.right, node)

    def _remove_at_node(self, element, node:Node, parent:Node):
        if element > node.data and node.right is not None:
            self._remove_at_node(element, node.right, node)
        elif element < node.data and node.left is not None:
            self._remove_at_node(element, node.left, node)
        elif element == node.data:
            if node.left is None and node.right is None:
                self._replace_node(node, parent, None)
            elif node.left is None:
                self._replace_node(node, parent, node.right)
            elif node.right is None:
                self._replace_node(node, parent, node.left)
            else:
                node.data = self._move_max_node(node.left, node)

    def remove(self, element):
        if self._root is None:
            return
        self._remove_at_node(element, self._root, None)

    def _pre_order_at_node(self, node: Node, lst: list):
        lst.append(node.data)
        if node.left is not None:
            self._pre_order_at_node(node.left, lst)
        if node.right is not None:
            self._pre_order_at_node(node.right, lst)

    def pre_order_walk(self):
        """Returns a list that walks through the nodes pre-order"""
        if self._root is None:
            return []
        lst = []
        self._pre_order_at_node(self._root, lst)
        return lst

    def _in_order_at_node(self, node: Node, lst: list):
        if node.left is not None:
            self._in_order_at_node(node.left, lst)
        lst.append(node.data)
        if node.right is not None:
            self._in_order_at_node(node.right, lst)

    def in_order_walk(self):
        """Returns a list that walks through the nodes in-order"""
        if self._root is None:
            return []
        lst = []
        self._in_order_at_node(self._root, lst)
        return lst

    def _post_order_at_node(self, node: Node, lst: list):
        if node.left is not None:
            self._post_order_at_node(node.left, lst)
        if node.right is not None:
            self._post_order_at_node(node.right, lst)
        lst.append(node.data)

    def post_order_walk(self):
        """Returns a list that walks through the nodes post-order"""
        if self._root is None:
            return []
        lst = []
        self._post_order_at_node(self._root, lst)
        return lst

    def _tree_height_at_node(self, node: Node):
        l_height = r_height = 0
        if node.left is not None:
            l_height = self._tree_height_at_node(node.left)+1
        if node.right is not None:
            r_height = self._tree_height_at_node(node.right)+1
        return max(l_height, r_height)

    def get_tree_height(self):
        """Returns the height of the bst. If empty retuns -1"""
        if self._root is None:
            return -1
        return self._tree_height_at_node(self._root)

    def _min_from_node(self, node: Node):
        if node.left is None:
            return node.data
        return self._min_from_node(node.left)

    def get_min(self):
        """Returns the smallest element in tree"""
        if self._root is None:
            return None
        return self._min_from_node(self._root)

    def _max_from_node(self, node: Node):
        if node.right is None:
            return node.data
        return self._max_from_node(node.right)

    def get_max(self):
        """Returns the largest element in tree"""
        if self._root is None:
            return None
        return self._max_from_node(self._root)

class Cnode:
    def __init__(self, value):
        self.value = value
        self.child = None

    def add_child(self, child):
        self.child = child

    def __repr__(self):
        return self.value

def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []

    ### Test 1: Binary Search Tree
    random.seed(123)
    b = BST()
    for i in range(10000):
        b.insert(random.randrange(0,40000))
    
    pickle_results.append(("Binary tree with 10,000 elements", pickler(b)))

    ### Test 2: Deque
    d = deque()
    random.seed(123)
    for i in range(10000):
        d.append(random.randrange(0,40000))

    pickle_results.append(("Deque with 10,000 elements", pickler(d)))

    ### Test 3: Recursive list
    a = []
    a.extend([1,2,3])
    a.append(a)
    a[3].append(a)
    pickle_results.append(("List containing itself", pickler(a)))

    ### Test 4: Cyclic set of nodes
    # root -> node_1 -> node_2 -> root
    root = Cnode(10)
    node_1 = Cnode(20)
    node_2 = Cnode(30)
    root.add_child(node_1)
    node_1.add_child(node_2)
    node_2.add_child(root)
    pickle_results.append(("A cyclic set of nodes", pickler(root)))

    ### Return results    
    return pickle_results

