"""Test suite testing floats, integers and other numbers"""

import decimal
import fractions
import random


def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []
    random.seed(123)

    ### Integers
    # Basic integer
    pickle_results.append(("Basic integer", pickler(random.randint(1,99))))

    # Large integer
    pickle_results.append(("Very large integer (10**100)", pickler(10**100)))

    # Negative numbers
    pickle_results.append(("Negative integer", pickler(random.randint(-5000, -1))))

    # Tuple of mixed numbers
    mixed = (random.randint(1, 99), 1 + random.random(), random.randint(-5000, -1), 0.0, float('nan'), decimal.Decimal("1.1"), fractions.Fraction(1, 3))
    pickle_results.append(("Tuple of mixed numbers", pickler(mixed)))

    # Fraction
    frac = fractions.Fraction(353, 113) # two prime numbers
    pickle_results.append(("Fraction (353/113)", pickler(frac)))

    ### Floats & decimals
    # Basic float
    pickle_results.append(("Basic float", pickler(3.14159)))

    # Zero and negative zero
    pickle_results.append(("Zero", pickler(0.0)))
    pickle_results.append(("Negative zero", pickler(-0.0)))

    # Infinity and -Infinity
    pickle_results.append(("Positive infinity", pickler(float("inf"))))
    pickle_results.append(("Negative infinity", pickler(float("-inf"))))

    # NaN (Not a Number)
    pickle_results.append(("NaN", pickler(float("nan"))))

    # Very large and very small floats
    pickle_results.append(("Very large float", pickler(1.79e308)))
    pickle_results.append(("Very small float", pickler(5e-324)))

    # Subnormal float
    pickle_results.append(("Subnormal float", pickler(1e-320)))

    # List of random floats
    rand_floats = [random.uniform(-1e10, 1e10) for _ in range(1000)]
    pickle_results.append(("List of 1000 random floats", pickler(rand_floats)))

    # List of special floats (inf, -inf, nan, 0.0, -0.0)
    special_floats = [float("inf"), float("-inf"), float("nan"), 0.0, -0.0]
    pickle_results.append(("List of special floats", pickler(special_floats)))

    # Nested structure with floats
    nested = {
        "a": [1.1, 2.2, [3.3, 4.4, {"b": -5.5, "c": float("nan")}]],
        "d": (float("inf"), float("-inf")),
        "e": {"f": 0.0, "g": -0.0},
    }
    pickle_results.append(("Nested structure with floats", pickler(nested)))

    # Tuple of floats
    pickle_results.append(("Tuple of floats", pickler((1.23, -4.56, 7.89))))

    # Set of floats
    pickle_results.append(("Set of floats", pickler({1.1, 2.2, 3.3, -4.4, 0.0})))

    # Decimal to float conversion
    dec = decimal.Decimal("2.718281828459045")
    pickle_results.append(("Decimal converted to float", pickler(float(dec))))

    ### Decimal high precision
    dec = decimal.Decimal("3.1415926535897932384626433832")
    pickle_results.append(("Decimal with high precision", pickler(dec)))

    # Matrix of floats
    matrix = [[float(i * j) for j in range(10)] for i in range(10)]
    pickle_results.append(("10x10 matrix of floats", pickler(matrix)))

    # Floats in dict keys and values
    float_dict = {float(i): float(i * i) for i in range(-5, 6)}
    pickle_results.append(("Dict with floats as keys and values", pickler(float_dict)))

    ### Return results
    return pickle_results
