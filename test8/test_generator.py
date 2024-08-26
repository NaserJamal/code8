import os
import json
import re
from openai import OpenAI
from anthropic import Anthropic

CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"api_key": "", "model_provider": "", "model": ""}

def remove_code_blocks(text):
    # Remove ```python and ``` from the beginning and end of the text
    text = re.sub(r'^```python', '', text)
    text = re.sub(r'\n^```python', '', text)
    text = re.sub(r'^```python\n', '', text)
    text = re.sub(r'```$', '', text)
    text = re.sub(r'\n```$', '', text)
    return text

def generate_tests(input_file):
    config = load_config()
    api_key = config['api_key']
    model_provider = config['model_provider']
    model = config['model']

    if not api_key or not model_provider or not model:
        print("Please configure your settings by running 'test8' without arguments.")
        return

    file_name = os.path.basename(input_file)

    with open(input_file, 'r') as file:
        code_content = file.read()

    system_message = f"You are a helpful assistant that generates Python unit tests for the file named '{file_name}'."
    user_prompt = f"""
    Please generate unit tests for the following Python code from the file '{file_name}':

    {code_content}

    Provide a complete unittest class with test methods for each function in the code.
    Do not include any explanations or code blocks, just the unittest code.
    """

    try:
        if model_provider == 'OpenAI':
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_prompt}
                ]
            )
            test_code = response.choices[0].message.content
        elif model_provider == 'Anthropic':
            client = Anthropic(api_key=api_key)
            response = client.messages.create(
                model=model,
                max_tokens=4000,
                system=system_message,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            test_code = response.content[0].text
        else:
            raise ValueError(f"Unsupported model provider: {model_provider}")
    except Exception as e:
        print(f"Error calling API: {str(e)}")
        return

    test_code = remove_code_blocks(test_code)

    base_name = os.path.splitext(file_name)[0]
    test_file_name = f"test_{base_name}.py"

    with open(test_file_name, 'w') as test_file:
        # test_file.write(f"import {base_name}\n\n")
        test_file.write(test_code)

    print(f"Unit tests generated in {test_file_name}")