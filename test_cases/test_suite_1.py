import decimal
import fractions
import random


def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []
    random.seed(123)

    ### Test 1: Basic integer
    pickle_results.append(("Basic integer", pickler(random.randint(1,99))))

    ### Test 2: Large integer
    pickle_results.append(("Very large integer (10**100)", pickler(10**100)))

    ### Test 3: Basic float
    pickle_results.append(("Basic float", pickler(random.randint(1, 9) + random.random())))

    ### Test 4: Special float values
    pickle_results.append(("Positive infinity", pickler(float('inf'))))
    pickle_results.append(("Negative infinity", pickler(float('-inf'))))
    pickle_results.append(("NaN", pickler(float('nan'))))

    ### Test 5: Decimal
    dec = decimal.Decimal("3.1415926535897932384626433832")
    pickle_results.append(("Decimal with high precision", pickler(dec)))

    ### Test 6: Fraction
    frac = fractions.Fraction(353, 113) # two prime numbers
    pickle_results.append(("Fraction (353/113)", pickler(frac)))

    ### Test 7: Negative numbers
    pickle_results.append(("Negative integer", pickler(random.randint(-5000, -1))))
    pickle_results.append(("Negative float", pickler(random.randint(-5000, -1) + random.random())))

    ### Test 8: Tuple of mixed numbers
    mixed = (random.randint(1, 99), 1 + random.random(), random.randint(-5000, -1), 0.0, float('nan'), decimal.Decimal("1.1"), fractions.Fraction(1, 3))
    pickle_results.append(("Tuple of mixed numbers", pickler(mixed)))

    ### Test 9: List of numbers
    nums = [i * 0.1 for i in range(-1000, 1001)]
    pickle_results.append(("List of floats from -100.0 to 100.0", pickler(nums)))

    ### Return results
    return pickle_results
