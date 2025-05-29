import pickle
from hashlib import sha256
from test_cases import test_suite_0, test_suite_1, test_suite_2, test_suite_3, test_suite_4, test_suite_5
import sys, platform
import json

### TEST RESULT: (ID, DESCRIPTION, SHA-256 HASH, PYTHON_VERSION, OS_INFO)
### Python versions: 3.8.10, 3.10.10, 3.12.10
def pickler(obj):
    """Creates a pickler dumps and return the sha-256 hash result"""
    pickled = pickle.dumps(obj)
    return sha256(pickled).hexdigest()

def env_info():
    return (sys.version.split(' ')[0], f"{platform.system()} {platform.release()}")

def perform_tests():
    env_inf = env_info()

    # ### Perform tests

    for i in range(1,3):
        test_results = []
        test_results.extend(test_suite_0.pickle(pickler))
        test_results.extend(test_suite_1.pickle(pickler))
        test_results.extend(test_suite_2.pickle(pickler))
        test_results.extend(test_suite_3.pickle(pickler))
        test_results.extend(test_suite_4.pickle(pickler))
        test_results.extend(test_suite_5.pickle(pickler))

        with open('test_results.json', 'r') as open_file:
            results = json.load(open_file)

        for test_name, test_hash in test_results:
            if test_name not in results:
                results[test_name] = {}
            key = f"{env_inf[0]}, {env_inf[1]}, {i}"
            tc_result = {"py_ver":env_inf[0], "platform":env_inf[1], "run":i, "hash":test_hash}
            results[test_name][key] = tc_result

        with open('test_results.json', 'w') as save_file:
            json.dump(results, save_file, ensure_ascii=False, indent = 4)


def main():
    perform_tests()
    
if __name__=='__main__':
    main()
