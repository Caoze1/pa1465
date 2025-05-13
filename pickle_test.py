import pickle
import hashlib
import platform
import sys
import os

# Fixed input (dict with consistent key order)
data = {
    "name": "Alice",
    "age": 30,
    "salary": 70000.0
}

# Pickle with fixed protocol (e.g., 4)
pickled = pickle.dumps(data, protocol=4)

# Hash the pickled data
hash_value = hashlib.sha256(pickled).hexdigest()

# Output for comparison
print(f"SHA256: {hash_value}")
print("✅ Environment Info")
print(f"Python version : {sys.version}")
print(f"Platform       : {platform.system()} {platform.release()}")
print(f"Machine        : {platform.machine()}")
print(f"Processor      : {platform.processor()}")
print(f"OS Version     : {platform.version()}")
print(f"Working Dir    : {os.getcwd()}")
print(f"File Encoding  : {sys.getfilesystemencoding()}")


#Petters Dator
# SHA256: 8ddad3409b8aefb763d07aef4bec37985abd0f0c54c94f704bbaff29946221b2
# ✅ Environment Info
# Python version : 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]
# Platform       : Darwin 24.3.0
# Machine        : x86_64
# Processor      : i386
# OS Version     : Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:00 PST 2025; root:xnu-11215.81.4~3/RELEASE_X86_64
# Working Dir    : /Users/pettereriksson/Documents/Programming/git_reps/Software_Testing/pa1465
# File Encoding  : utf-8

#Viktors Dator
# SHA256: 9dad965394f53f7c220dbd15d64a052cd5414184c0c11fe1e309afd177d0a052
# ✅ Environment Info
# Python version : 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Platform       : Windows 10
# Machine        : AMD64
# Processor      : Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
# OS Version     : 10.0.22631
# Working Dir    : C:\Users\vikto\OneDrive\Dokument\skola\3\testning av mjukvara\pa1465
# File Encoding  : utf-8