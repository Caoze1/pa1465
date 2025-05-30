## Pickle Consistency Testing
This repository contains a test suite for testing the stability and correctness of the Python Pickle module. The main goal is to verify whether the function pickle.dumps() produces an identical serialized output (verified using hashing - SHA-256) for the same input object across different setups. Our testing has been done for different Python versions: 3.8, 3.10 and 3.12, and across different Operating systems: Windows, Linux and Mac OS.

## The test suite
The repository contains 4 different test suites, testing different objects:
1. **Integers, floats and other numbers**
2. **String representation** - different sets of characters, such as ascii and greek.
3. **Data structures** - build in python data structures such as list, tuple and dictionary. Other data structure, such as Deque and Frozen set. Also recursive data structures and custom ones.
4. **Functions and imported libraries**  - different functions, regex, datetime, Numpy arrays and Pandas dataframes.
## Running the program
To run the program you need to install Python 3. It must be at least Python 3.4 (but some more recent version is recommended) to support Pickle 4.0 that is being used. To be able to run different Python versions, you can consider using [venv](https://docs.python.org/3/library/venv.html) to create virtual environments. 

The program uses [numpy](https://github.com/numpy/numpy) and [pandas](https://github.com/pandas-dev/pandas), which can be installed with pip:
```
pip install numpy, pandas
```

To run the program, simply use the terminal and write:
```
python3 main.py
```
## The result
Test results are stored in the file **test_results.json**. When running **main.py**, the program will identify missmatched hashes, and print that in the terminal. Each test case has one entry in the result-file, which includes the name of the test, the hash, the Python version and the operating system. To compare the results further (for the Python versions and operating systems specified) you can run:
```
python3 export.py
```
to generate LaTeX tables (in output files ltx1.txt, ltx2.txt, ltx3.txt, ltx4.txt and ltx.txt) containing data on how well the hash values match. This data can be used to generate LaTeX tables.