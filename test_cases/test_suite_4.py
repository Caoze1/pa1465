import random
import decimal


def pickle(pickler):
    """Returns pickles result from test suite"""
    pickle_results = []
    random.seed(123)

    # Test 1: Basic float
    pickle_results.append(("Basic float", pickler(3.14159)))

    # Test 2: Negative float
    pickle_results.append(("Negative float", pickler(-2.71828)))

    # Test 3: Zero and negative zero
    pickle_results.append(("Zero", pickler(0.0)))
    pickle_results.append(("Negative zero", pickler(-0.0)))

    # Test 4: Infinity and -Infinity
    pickle_results.append(("Positive infinity", pickler(float("inf"))))
    pickle_results.append(("Negative infinity", pickler(float("-inf"))))

    # Test 5: NaN (Not a Number)
    pickle_results.append(("NaN", pickler(float("nan"))))

    # Test 6: Very large and very small floats
    pickle_results.append(("Very large float", pickler(1.79e308)))
    pickle_results.append(("Very small float", pickler(5e-324)))

    # Test 7: Subnormal float
    pickle_results.append(("Subnormal float", pickler(1e-320)))

    # Test 8: List of random floats
    rand_floats = [random.uniform(-1e10, 1e10) for _ in range(1000)]
    pickle_results.append(("List of 1000 random floats", pickler(rand_floats)))

    # Test 9: List of special floats (inf, -inf, nan, 0.0, -0.0)
    special_floats = [float("inf"), float("-inf"), float("nan"), 0.0, -0.0]
    pickle_results.append(("List of special floats", pickler(special_floats)))

    # Test 10: Nested structure with floats
    nested = {
        "a": [1.1, 2.2, [3.3, 4.4, {"b": -5.5, "c": float("nan")}]],
        "d": (float("inf"), float("-inf")),
        "e": {"f": 0.0, "g": -0.0},
    }
    pickle_results.append(("Nested structure with floats", pickler(nested)))

    # Test 11: Tuple of floats
    pickle_results.append(("Tuple of floats", pickler((1.23, -4.56, 7.89))))

    # Test 12: Set of floats
    pickle_results.append(("Set of floats", pickler({1.1, 2.2, 3.3, -4.4, 0.0})))

    # Test 13: Decimal to float conversion
    dec = decimal.Decimal("2.718281828459045")
    pickle_results.append(("Decimal converted to float", pickler(float(dec))))

    # Test 14: Matrix of floats
    matrix = [[float(i * j) for j in range(10)] for i in range(10)]
    pickle_results.append(("10x10 matrix of floats", pickler(matrix)))

    # Test 15: Floats in dict keys and values
    float_dict = {float(i): float(i * i) for i in range(-5, 6)}
    pickle_results.append(("Dict with floats as keys and values", pickler(float_dict)))

    return pickle_results
