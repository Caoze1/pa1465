import pickle
from hashlib import sha256
from test_cases import test_suite_0
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

def main():
    env_info()

    ### Perform tests
    test_results = []
    test_results.extend(test_suite_0.pickle(pickler))
    
    for test in test_results:
        print(test)
    
if __name__=='__main__':
    main()
