import os
from openai import OpenAI

client = None

def set_api_key(api_key):
    global client
    client = OpenAI(api_key=api_key)

def generate_tests(input_file):
    global client
    # if client is None:
    #     client = OpenAI()  # This will use the OPENAI_API_KEY environment variable
    client = OpenAI(api_key="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")

    # Get the file name from the input_file path
    file_name = os.path.basename(input_file)

    # Read the content of the input file
    with open(input_file, 'r') as file:
        code_content = file.read()
    
    # Prepare the system message and user prompt for GPT-4
    system_message = f"""
You are an expert Python developer specializing in unit testing. Your task is to create comprehensive, readable, and effective unit tests for given Python code. Follow these guidelines:

Use the unittest framework unless otherwise specified.
Create a test class that inherits from unittest.TestCase.
Write individual test methods for each function/method and different scenarios.
Use descriptive names for test methods, starting with "test_".
Include tests for normal operations, edge cases, and potential error conditions.
Use appropriate assert methods (assertEqual, assertTrue, assertRaises, etc.).
Implement setUp and tearDown methods if necessary.
Cover all public methods/functions of the given code.
Aim for high code coverage while maintaining readability.
Include comments explaining complex test logic if necessary.
Follow PEP 8 style guidelines.
If mocking is required, use the unittest.mock module.

Provide the complete test file content, including necessary imports and the main block to run the tests."""
    
    user_prompt = f"""
    Please create a comprehensive unit test for the following Python code from the file '{file_name}':

    {code_content}

Please ensure the unit tests cover all methods and include tests for normal operations, edge cases, and potential error conditions.
Only return the code with no explanations, do not use code blocks.
    """
    
    # Call the OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ]
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {str(e)}")
        return
    
    # Extract the generated test code
    test_code = response.choices[0].message.content
    
    # Create the test file
    base_name = os.path.splitext(file_name)[0]
    test_file_name = f"test_{base_name}.py"
    
    with open(test_file_name, 'w') as test_file:
        test_file.write(f"import {base_name}\n\n")
        test_file.write(test_code)
    
    print(f"Unit tests generated in {test_file_name}")