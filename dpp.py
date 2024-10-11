import os
import hashlib
from collections import Counter

import numpy
import numpy as np

list_of_files = []


def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)

    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            list_of_files.append([full_path, compute_file_hash(full_path)])
    return list_of_files
# Specify the directory path you want to start from

directory_path = 'D:\\test'
list_files_recursive(directory_path)
print(list_of_files)
files_numpy = numpy.array(list_of_files)
idx_sort = np.argsort(files_numpy)
print(idx_sort)
