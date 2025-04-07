# Sentiment Analysis API

## Overview | Setup | Usage | Collaboration | Evaluation

**Updates** 07/04/2025: Initial release with sentiment analysis capabilities using DistilBERT.

## Introduction
Sentiment Analysis API is a lightweight, efficient framework for deploying pre-trained NLP models as RESTful services. Its key features include:

- **High Efficiency**: Leverages Hugging Face Transformers for state-of-the-art sentiment analysis with minimal latency.
- **Simple REST API**: Clean FastAPI implementation providing straightforward endpoints for sentiment analysis tasks.
- **Collaborative Development**: Structured for team-based development with GitHub workflow integration.
- **Extensible Design**: Modular architecture allows for easy integration of additional models and features.

## Installation

In a Python environment with supported versions (we recommend 3.8+), install the required packages:
Create a virtual environment
python -m venv env
Activate it (Windows)
env\Scripts\activate
OR (Mac/Linux)
source env/bin/activate
Install required packages
pip install -r requirements.txt
Copy
## Usage

### Running the API locally
From the project root
uvicorn app.main --reload
Copy
The API will be available at http://127.0.0.1:8000. You can access the automatic documentation at http://127.0.0.1:8000/docs.

### API Endpoints

#### Analyze Sentiment
POST /analyze

Request body:
{
"text": "Your text to analyze"
}
Copy
Response:
{
"text": "Your text to analyze",
"sentiment": "positive",
"score": 0.95
}
Copy
### Code Example
import requests
url = "http://127.0.0.1:8000/analyze"
payload = {"text": "I love this product, it works great!"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
result = response.json()
print(result)
Output: {"text": "I love this product, it works great!", "sentiment": "positive", "score": 0.97}
Copy
## Collaborative Development

### GitHub Workflow

We follow a structured GitHub workflow for this project:

1. **Feature Branches**: Create a branch for each new feature or bugfix
git checkout -b feature/add-language-detection
Copy
2. **Pull Requests**: Submit PRs for code review before merging to main

3. **Code Reviews**: All code must be reviewed by at least one team member before merging

4. **Versioning**: We use semantic versioning to track changes
- Major version: Breaking API changes
- Minor version: New features, backwards compatible
- Patch version: Bug fixes, backwards compatible

## Project Structure
sentiment-analysis-api/
├── app/
│   ├── init.py
│   ├── main.py         # FastAPI application
│   └── model.py        # Sentiment analysis model implementation
├── tests/
│   ├── init.py
│   ├── test_api.py     # API tests
│   └── test_model.py   # Model tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
Copy
## License

This project is licensed under the MIT License - see the LICENSE file for details.