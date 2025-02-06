from flask import Flask, request, jsonify
from app.code_analyzer import review_code
from app.test_generator import generate_tests

app = Flask(__name__)

@app.route("/review", methods=["POST"])
def review():
    """Endpoint to analyze and review code."""
    data = request.json
    code_snippet = data.get("code", "")
    feedback = review_code(code_snippet)
    return jsonify({"code_review": feedback})

@app.route("/generate_tests", methods=["POST"])
def generate_tests_api():
    """Endpoint to generate unit tests."""
    data = request.json
    code_snippet = data.get("code", "")
    test_cases = generate_tests(code_snippet)
    return jsonify({"unit_tests": test_cases})

if __name__ == "__main__":
    app.run(debug=True)
