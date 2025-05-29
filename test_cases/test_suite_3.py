import hashlib
from collections import deque


def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj, protocol=4)).hexdigest()

def stability_check(obj):
    try:
        before = hash_object(obj)
        after = hash_object(pickle.loads(pickle.dumps(obj, protocol=4)))
        return "PASS" if before == after else "FAIL"
    except Exception as e:
        return f"ERROR: {e}"

def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []

    ### Test 1: Adjacency List Graph
    graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
    }
    pickle_results.append(("Graph (adjacency list)", pickler(graph)))

    ### Test 2: Nested dict
    nested_dict = {"x": [1, 2, {"a": True}], "y": deque([3, 4])}
    pickle_results.append(("Nested dict", pickler(nested_dict)))

    ### Test 3: Tree as Nested Dict
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

    ### Test 4: Queue (deque with popleft)
    q = deque()
    for i in range(5000):
        q.append(i)
    for _ in range(2500):
        q.popleft()
    pickle_results.append(("Queue (deque, FIFO)", pickler(q)))

    ### Test 5: Large set
    s = set(range(50000))
    pickle_results.append(("Set (50000 ints)", pickler(s)))

    ### Test 6: Tuple with mixed data structures
    t = (["a", "b"], {"k": "v"}, set())
    pickle_results.append(("Tuple (mixed structures)", pickler(t)))

    ### Test 7: Stack (LIFO list)
    stack = []
    for i in range(1000):
        stack.append(i)
    for _ in range(500):
        stack.pop()
    pickle_results.append(("Stack (list, LIFO)", pickler(stack)))

    ### Test 8: Heap-ish nested list (Fibonacci-like)
    fib_like = [1]
    for i in range(2, 10):
        fib_like = [i, fib_like]
    pickle_results.append(("Nested list chain (Fibonacci-like)", pickler(fib_like)))

    ### Test 9: Frozen set
    fs = frozenset([1, 2, 3])
    pickle_results.append(("Simple frozen set", pickler(fs)))

    ### Test 10: Type
    t = type(fs)
    pickle_results.append(("Type", pickler(t)))

    return pickle_results
