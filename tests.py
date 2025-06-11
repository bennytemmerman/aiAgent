import sys
import os

# Ensure the project root is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from functions.get_files_info import get_files_info

def run_tests():
    print('Test 1: get_files_info("calculator", ".")')
    print(get_files_info("calculator", "."))
    print()

    print('Test 2: get_files_info("calculator", "pkg")')
    print(get_files_info("calculator", "pkg"))
    print()

    print('Test 3: get_files_info("calculator", "/bin")')
    print(get_files_info("calculator", "/bin"))
    print()

    print('Test 4: get_files_info("calculator", "../")')
    print(get_files_info("calculator", "../"))
    print()

if __name__ == "__main__":
    run_tests()

