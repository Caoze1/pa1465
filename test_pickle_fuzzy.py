import pickle
import os
import random

def generate_random_bytes(max_length=100):
    length = random.randint(1, max_length)
    return os.urandom(length)

def fuzz_pickle(iterations=1000):
    for i in range(iterations):
        data = generate_random_bytes()
        try:
            pickle.loads(data)
        except (pickle.UnpicklingError, EOFError, AttributeError, IndexError, TypeError, ValueError) as e:
            # Expected errors during fuzzing
            pass
        except Exception as e:
            print(f"[!] Unexpected exception on iteration {i}: {type(e).__name__} - {e}")
        else:
            print(f"[+] Valid load on iteration {i}: {data}")

if __name__ == "__main__":
    fuzz_pickle()
