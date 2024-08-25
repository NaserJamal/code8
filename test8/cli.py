import sys
import os
import argparse
from getpass import getpass
from .test_generator import generate_tests, set_api_key

def main():
    parser = argparse.ArgumentParser(description="Generate unit tests for Python files.")
    parser.add_argument('file', nargs='?', help="The Python file to generate tests for")
    parser.add_argument('--key', action='store_true', help="Prompt for OpenAI API key")

    args = parser.parse_args()

    if args.key:
        api_key = getpass("Enter your OpenAI API key: ")
        set_api_key(api_key)
        print("API key has been set.")
        return

    if not args.file:
        print("Usage: test8 <python_file> or test8 --key")
        sys.exit(1)

    input_file = args.file
    if not input_file.endswith('.py'):
        print("Error: Input file must be a .py file")
        sys.exit(1)
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    
    generate_tests(input_file)

if __name__ == "__main__":
    main()