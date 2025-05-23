import pickle

import unittest

# Test case for pickling/unpickling Classes
class Class: # Data hold
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False
        return self.data == other.data

class TestPickleClasses(unittest.TestCase):
    def test_pickle(self):
        
        original = Class({"user": "ben", "score": [5, 10, 20]})
        pickled = pickle.dumps(original)        
        unpickled = pickle.loads(pickled)
        # Check if the original and loaded objects are equal
        self.assertEqual(original, unpickled)
        self.assertEqual(unpickled.data["user"], "ben")
        self.assertEqual(len(unpickled.data["score"]), 3) # Three values in score
        

if __name__ == '__main__':
    unittest.main()
    