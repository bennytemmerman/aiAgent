from functions.run_python import run_python_file

if __name__ == "__main__":
    print("Test 1: run_python_file('calculator', 'main.py')")
    print(run_python_file("calculator", "main.py"), end="\n\n")

    print("Test 2: run_python_file('calculator', 'tests.py')")
    print(run_python_file("calculator", "tests.py"), end="\n\n")

    print("Test 3: run_python_file('calculator', '../main.py')")
    print(run_python_file("calculator", "../main.py"), end="\n\n")

    print("Test 4: run_python_file('calculator', 'nonexistent.py')")
    print(run_python_file("calculator", "nonexistent.py"), end="\n\n")
