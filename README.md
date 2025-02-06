# ai-code-reviewer
Code prototype for an Autonomous Code Review &amp; Optimization Agent

This AI agent will:
- Analyse code commits for security vulnerabilities, performance bottlenecks, and style violations
- Suggest optimizations (e.g., replacing loops with vectorized operations)
- Auto-generate unit test templates for new code
- Integrate with GitHub Actions for real-time feedback in pull requests


## Folder Structure

![image](https://github.com/user-attachments/assets/823f6f3e-ccb8-4edc-a268-3c6989fdbbb2)


Running the Demo

A. Install Dependencies
> pip install flask openai

B. Start Flask App
> python main.py

C. Test API with a Sample Request
**Code Review**

> curl -X POST "http://127.0.0.1:5000/review" -H "Content-Type: application/json" -d '{"code": "def calculate_sum(numbers): total = 0\n for num in numbers:\n total += num\n return total"}'

**Response Example:**

{
  "code_review": "Performance issue: Replace loop-based sum with numpy.sum().\nSecurity: No vulnerabilities found.\nBest Practice: Use list comprehensions where possible."
}


**Unit Test Generation**

> curl -X POST "http://127.0.0.1:5000/generate_tests" -H "Content-Type: application/json" -d '{"code": "def calculate_sum(numbers): return sum(numbers)"}'

**Response Example:**

{
  "unit_tests": "import pytest\n\ndef test_calculate_sum():\n    assert calculate_sum([1, 2, 3]) == 6\n    assert calculate_sum([]) == 0\n    assert calculate_sum([-1, 1, 0]) == 0"
}

**This GitHub Actions workflow will:**
1.	Trigger on pull requests
2.	Send the code to the AI agent
3.	Post the AI review feedback as a PR comment

**Future Enhancements**

1.	VS Code Plugin for real-time feedback   
2.	More advanced AI models for deep code analysis
3.	Security-focused integrations like OWASP Dependency Check

