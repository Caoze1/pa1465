import pickle
from hashlib import sha256
from test_cases import test_suite_0, test_suite_1, test_suite_2, test_suite_3
from tests import test_classes
import unittest
import sys, platform

### TEST RESULT: (ID, DESCRIPTION, SHA-256 HASH, PYTHON_VERSION, OS_INFO)

def pickler(obj):
    """Creates a pickler dumps and return the sha-256 hash result"""
    pickled = pickle.dumps(obj)
    return sha256(pickled).hexdigest()

def env_info():
    print("--- Environment Info ---")
    print(f"Python version : {sys.version}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Machine        : {platform.machine()}")
    print(f"Processor      : {platform.processor()}")
    print(f"OS Version     : {platform.version()}")
    print(f"File Encoding  : {sys.getfilesystemencoding()}")
    print("---")
    
def run_class_tests():
    print("\nRunning class tests...")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_classes.TestPickleClasses)
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)

    result = runner.run(suite)
    if result.wasSuccessful():
        print("Class test: OK")
    else:
        print("Class test: FAILED")

def main():
    env_info()

    ### Perform tests
    test_results = []
    test_results.extend(test_suite_0.pickle(pickler))
    test_results.extend(test_suite_1.pickle(pickler))
    test_results.extend(test_suite_2.pickle(pickler))
    test_results.extend(test_suite_3.pickle(pickler))

    for test in test_results:
        print(test)
        
    run_class_tests()
    
if __name__=='__main__':
    main()
