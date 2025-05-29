"""Test suite testing classes, functions, regex, numpy and pandas"""

import re
import numpy as np
import pandas as pd

# Test case for pickling/unpickling Classes
class Class: # Data hold
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False
        return self.data == other.data

### Test functions
def increment(x):
    return x + 1

def dict_add(d):
    d["a"] = 10

def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []

    ### Custom class with data
    original = Class({"user": "ben", "score": [5, 10, 20]})
    pickle_results.append(("Custom class with data", pickler(original)))
    
    ### Functions increment and add
    pickle_results.append(("Function increment", pickler(increment)))
    pickle_results.append(("Function dictionary add", pickler(dict_add)))

    ### Regex
    rem = re.match(r"(\d+)", "regex 232 match")
    pickle_results.append(("Simple Queue", pickler(rem)))

    ### Numpy tests
    n1 = np.array([123,412,54,243,43])
    n2 = np.array([[123,412,54,243,43],[89,33,41,3,0]])
    pickle_results.append(("Numpy 1D-array", pickler(n1)))
    pickle_results.append(("Numpy 2D-array", pickler(n2)))

    ### Pandas tests
    p1 = pd.DataFrame({'name':['Alpha','Beta','Gamma'],'value':[15,93,54]})
    pickle_results.append(("Pandas dataframe - 3 entries", pickler(p1)))
    
    return pickle_results

    