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

    ### Test 3: Fraction
    frac = fractions.Fraction(353, 113) # two prime numbers
    pickle_results.append(("Fraction (353/113)", pickler(frac)))

    ### Test 4: Negative numbers
    pickle_results.append(("Negative integer", pickler(random.randint(-5000, -1))))

    ### Test 5: Tuple of mixed numbers
    mixed = (random.randint(1, 99), 1 + random.random(), random.randint(-5000, -1), 0.0, float('nan'), decimal.Decimal("1.1"), fractions.Fraction(1, 3))
    pickle_results.append(("Tuple of mixed numbers", pickler(mixed)))

    ### Return results
    return pickle_results
