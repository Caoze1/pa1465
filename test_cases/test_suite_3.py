"""Test suite testing data structures, custom ones and built in ones"""

import collections as cl
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

    ### Adjacency List Graph
    graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
    }
    pickle_results.append(("Graph (adjacency list)", pickler(graph)))

    ### Nested dict
    nested_dict = {"x": [1, 2, {"a": True}], "y": cl.deque([3, 4])}
    pickle_results.append(("Nested dict", pickler(nested_dict)))

    ### Tree as Nested Dict
    tree = {
        "root": {
            "left": {"value": 1},
            "right": {
                "left": {"value": 2},
                "right": {"value": 3}
            }
        }
    }
    pickle_results.append(("Tree (nested dict)", pickler(tree)))

    ### Queue (deque with popleft)
    q = cl.deque()
    for i in range(5000):
        q.append(i)
    for _ in range(2500):
        q.popleft()
    pickle_results.append(("Queue (deque, FIFO)", pickler(q)))

    ### Large set
    s = set(range(50000))
    pickle_results.append(("Set (50000 ints)", pickler(s)))

    ### Text set
    s = {"strawberry", "jordgubbe", "framboise", "mansikat"}
    pickle_results.append(("Set with strings", pickler(s)))
    
    ### Text and integer Dictionary
    dict = {"english":"strawberry", "swedish":"jordgubbe", "french":"framboise", "finish":"mansikat", "number":12, "n2":15}
    pickle_results.append(("Dictionary with strings and ints", pickler(dict)))

    ### Tuple with mixed data structures
    t = (["a", "b"], {"k": "v"}, set())
    pickle_results.append(("Tuple (mixed structures)", pickler(t)))

    ### Stack (LIFO list)
    stack = []
    for i in range(1000):
        stack.append(i)
    for _ in range(500):
        stack.pop()
    pickle_results.append(("Stack (list, LIFO)", pickler(stack)))

    ### Heap-ish nested list (Fibonacci-like)
    fib_like = [1]
    for i in range(2, 10):
        fib_like = [i, fib_like]
    pickle_results.append(("Nested list chain (Fibonacci-like)", pickler(fib_like)))

    ### Frozen sets
    fs = frozenset([1, 2, 3])
    fs_str = frozenset(['a', 'b', 'c', 'd'])
    pickle_results.append(("Simple frozen set numbers", pickler(fs)))
    pickle_results.append(("Simple frozen set letters", pickler(fs_str)))

    ### Type
    t = type(fs)
    pickle_results.append(("Type", pickler(t)))
    
    ### Defaultdict
    dd = cl.defaultdict(int)
    dd['a'] += 1
    dd['b'] = 12
    pickle_results.append(("Default Dict", pickler(dd)))

    ### Ordered dict
    od = cl.OrderedDict()
    od['1'] = 1
    od['2'] = 2
    pickle_results.append(("Ordered Dict", pickler(od)))

    ### Counter
    cnt = cl.Counter(['a', 'a', 'a', 'b'])
    pickle_results.append(("Collections Counter ", pickler(cnt)))
    
    ### ChainMap
    cm = cl.ChainMap({'a':1}, {'b':2})
    pickle_results.append(("Chainmap ", pickler(cm)))

    ### Binary Search Tree
    random.seed(123)
    b = BST()
    for i in range(10000):
        b.insert(random.randrange(0,40000))
    
    pickle_results.append(("Binary tree with 10,000 elements", pickler(b)))

    ### Deque
    d = cl.deque()
    random.seed(123)
    for i in range(10000):
        d.append(random.randrange(0,40000))

    pickle_results.append(("Deque with 10,000 elements", pickler(d)))

    ### Recursive list
    a = []
    a.extend([1,2,3])
    a.append(a)
    a[3].append(a)
    pickle_results.append(("List containing itself", pickler(a)))

    ### Cyclic set of nodes
    # root -> node_1 -> node_2 -> root
    root = Cnode(10)
    node_1 = Cnode(20)
    node_2 = Cnode(30)
    root.add_child(node_1)
    node_1.add_child(node_2)
    node_2.add_child(root)
    pickle_results.append(("A cyclic set of nodes", pickler(root)))


    return [t + (3,) for t in pickle_results]

