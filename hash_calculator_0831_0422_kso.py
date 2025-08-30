# 代码生成时间: 2025-08-31 04:22:58
import hashlib
import sys

"""
    A simple hash calculator tool that uses the hashlib library to compute various hash values.
    This tool supports SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, and MD5.
"""

# Define the available hash algorithms
# 改进用户体验
AVAILABLE_HASHES = {
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "md5": hashlib.md5
}

"""
    Calculates the hash of a given string or file.
    
    Parameters:
        file_path (str): The path to the file for which the hash will be calculated.
        hash_algorithm (str): The name of the hash algorithm to use.
    
    Returns:
        str: The calculated hash value.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the specified hash algorithm is not supported.
"""
# 优化算法效率
def calculate_hash(file_path, hash_algorithm):
    if hash_algorithm not in AVAILABLE_HASHES:
        raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")

    try:
        with open(file_path, 'rb') as file:
            # Create a hash object
            hash_obj = AVAILABLE_HASHES[hash_algorithm]()
            # Read the file in chunks to avoid memory issues with large files
            while chunk := file.read(4096):
# NOTE: 重要实现细节
                hash_obj.update(chunk)
            # Return the hex digest of the hash
            return hash_obj.hexdigest()
# FIXME: 处理边界情况
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
# FIXME: 处理边界情况
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

"""
    Main function to handle command line arguments and calculate the hash.
"""
def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_calculator.py <file_path> <hash_algorithm>")
        sys.exit(1)
# 优化算法效率

    file_path = sys.argv[1]
    hash_algorithm = sys.argv[2]
    try:
        hash_value = calculate_hash(file_path, hash_algorithm)
# TODO: 优化性能
        print(f"The {hash_algorithm} hash of {file_path} is:
{hash_value}")
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnf:
        print(fnf)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
# TODO: 优化性能