import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def review_code(code_snippet):
    """Uses GPT-4 to analyze code and provide feedback."""
    prompt = f"""
    You are an expert code reviewer. Analyze the following Python code for:
    - Security vulnerabilities
    - Performance optimizations
    - Best practices and style guide adherence

    Also, suggest improvements where necessary.

    Code:
    {code_snippet}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
