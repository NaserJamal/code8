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
    
    # Prepare the system message and user prompt for GPT
    system_message = f"You an expert at generating Python unit tests for the file named '{file_name}'."
    
    user_prompt = f"""
    Please generate unit tests for the following Python code from the file '{file_name}':

    {code_content}

    Provide a complete unittest class with test methods for each function in the code.
    Cover all aspects and possible edge cases in the code.
    Do not include any explanations, do not use code blocks, just the unittest code.
    """
    
    # Call the OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
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