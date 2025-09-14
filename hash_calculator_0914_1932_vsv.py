# 代码生成时间: 2025-09-14 19:32:48
import hashlib
import sys

"""
Hash Calculator Tool

This tool calculates the hash value of a given string using various hashing algorithms.
"""

# Supported hashing algorithms
SUPPORTED_HASHES = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

def calculate_hash(data: str, algorithm: str) -> str:
    """
    Calculate the hash value of the given data using the specified algorithm.

    Args:
        data (str): The input data to be hashed.
        algorithm (str): The hashing algorithm to use.

    Returns:
        str: The hash value of the input data.
    """
    try:
        # Create a new hash object
        hash_object = getattr(hashlib, algorithm)()
        # Update the hash object with the input data
        hash_object.update(data.encode('utf-8'))
        # Return the hexadecimal representation of the hash value
        return hash_object.hexdigest()
    except AttributeError:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")
    except Exception as e:
        raise ValueError(f"Error calculating hash: {str(e)}")

def main():
    """
    Main function to process command line arguments and calculate hash values.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python hash_calculator.py <data> <algorithm>")
        sys.exit(1)

    # Extract the input data and algorithm from the command line arguments
    data = sys.argv[1]
    algorithm = sys.argv[2]

    # Check if the specified algorithm is supported
    if algorithm not in SUPPORTED_HASHES:
        print(f"Unsupported hashing algorithm: {algorithm}. Supported algorithms are: {', '.join(SUPPORTED_HASHES)}")
        sys.exit(1)

    # Calculate the hash value and print the result
    try:
        hash_value = calculate_hash(data, algorithm)
        print(f"Hash value ({algorithm}): {hash_value}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()