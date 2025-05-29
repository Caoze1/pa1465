import pickle
from hashlib import sha256
from test_cases import test_suite_1, test_suite_2, test_suite_3, test_suite_4
import sys, platform
import json

### TEST RESULT: (ID, DESCRIPTION, SHA-256 HASH, PYTHON_VERSION, OS_INFO)
### Python versions: 3.8.10, 3.10.10, 3.12.10
def pickler(obj):
    """Creates a pickler dumps and return the sha-256 hash result"""
    pickled = pickle.dumps(obj)
    return sha256(pickled).hexdigest()

def env_info():
    return (sys.version.split(' ')[0], f"{platform.system()}")

def perform_tests():
    env_inf = env_info()
    print(f"Env: {env_inf}")

    ### Perform tests
    test_results = []
    test_results.extend(test_suite_1.pickle(pickler))
    test_results.extend(test_suite_2.pickle(pickler))
    test_results.extend(test_suite_3.pickle(pickler))
    test_results.extend(test_suite_4.pickle(pickler))

    ### Load JSON result file
    with open('test_results.json', 'r') as open_file:
        results = json.load(open_file)

    ### Store new results
    test_names = set()
    for test_name, test_hash in test_results:
        test_names.add(test_name)
        if test_name not in results:
            results[test_name] = {}
        key_0 = f"{env_inf[0]}, {env_inf[1]}, {0}"
        key = f"{env_inf[0]}, {env_inf[1]}, {1}"

        if key_0 in results[test_name]:
            results[test_name][key] = {"py_ver":env_inf[0], "platform":env_inf[1], "run":1, "hash":test_hash}
        else:
            results[test_name][key_0] = {"py_ver":env_inf[0], "platform":env_inf[1], "run":0, "hash":test_hash}

    ### Remove old test cases
    results = {k: v for k, v in results.items() if k in test_names}

    ### Write results to file
    with open('test_results.json', 'w') as save_file:
        json.dump(results, save_file, ensure_ascii=False, indent = 4)

def compare_results():
    ### Load result JSON File
    with open('test_results.json', 'r') as open_file:
        results = json.load(open_file)
    
    ### Load Compare hashes for each test case
    for test_name, tdict in results.items():
        if len(tdict) == 0:
            continue

        base_hash = None
        for key, tres in tdict.items():
            hs = tres["hash"]
            if base_hash is None:
                base_hash = hs
                continue
            if base_hash != hs:
                print(f"Failed test: {test_name}")
                break


def main():
    perform_tests()
    # compare_results()
    
if __name__=='__main__':
    main()
