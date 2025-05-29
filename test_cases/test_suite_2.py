"""Test suite testing string representation"""
import random

def random_unicode_string(start, end, length):
    return ''.join(chr(random.randint(start, end)) for _ in range(length))

def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []

    random.seed(123)

    # Random unicode strings
    pickle_results.append(("Random ASCII", pickler(random_unicode_string(32, 126, 50))))
    pickle_results.append(("Random Latin-1", pickler(random_unicode_string(160, 255, 50))))
    pickle_results.append(("Random Hebrew", pickler(random_unicode_string(0x0590, 0x05FF, 50))))
    pickle_results.append(("Random Greek", pickler(random_unicode_string(0x0370, 0x03FF, 50))))
    pickle_results.append(("Random Cyrillic", pickler(random_unicode_string(0x0400, 0x04FF, 50))))
    pickle_results.append(("Random CJK Han", pickler(random_unicode_string(0x4E00, 0x9FFF, 50))))
    pickle_results.append(("Random Emoji", pickler(random_unicode_string(0x1F300, 0x1FAFF, 30))))

    ### Return results
    return pickle_results
