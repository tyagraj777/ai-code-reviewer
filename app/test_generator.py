def generate_tests(code_snippet):
    """Uses GPT-4 to generate unit test cases for a given Python function."""
    prompt = f"""
    Generate Python unit test cases for the following function using pytest.

    Function:
    {code_snippet}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
