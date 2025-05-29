import pickle

# Test case for pickling/unpickling Classes
class Class: # Data hold
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False
        return self.data == other.data

def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []
    original = Class({"user": "ben", "score": [5, 10, 20]})
    pickle_results.append(("Custom class with data", pickler(original)))

    return pickle_results

    