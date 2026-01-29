# HW3 - CI Pipeline with Flask

A simple Flask web application with automated CI/CD pipeline using GitHub Actions.

## Features

This app has 3 main endpoints:
- **GET /**: Home page with welcome message
- **GET /health**: Health check endpoint (returns JSON status)
- **POST /calculate**: Simple calculation endpoint (add two numbers)

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
git clone https://github.com/yijinwang2003-wq/hw3-ci-flask.git
cd hw3-ci-flask


2. Install dependencies: pip install -r requirements.txt


### Running the Application

Start the Flask server: python app.py


The app will run on `http://localhost:5000`

## Testing

Run all tests with pytest: pytest


Run tests with coverage report: pytest --cov=. --cov-report=html


## CI Pipeline

The project uses GitHub Actions for continuous integration. The pipeline automatically:

1. **Triggers**: Runs on push to main branch and on pull requests
2. **Environment Setup**: Checks out code, sets up Python 3.9, installs dependencies
3. **Code Quality Checks**: 
   - Runs `flake8` for linting
   - Runs `black` to check code formatting
4. **Testing**: 
   - Executes all unit tests with pytest
   - Generates coverage report
   - Enforces 80% minimum test coverage
5. **Build Verification**: Ensures the application builds successfully

### Pipeline Configuration

See `.github/workflows/ci.yml` for the complete CI configuration.

## Project Structure

```
hw3-ci-flask/
├── app.py                  # Main Flask application
├── tests/                  # Test directory
│   └── test_app.py        # Unit tests
├── requirements.txt        # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI pipeline
├── .flake8                # Flake8 configuration
├── pyproject.toml         # Black configuration
└── README.md              # This file
```

## Technologies Used

- **Flask**: Web framework
- **pytest**: Testing framework
- **flake8**: Code linting
- **black**: Code formatting
- **pytest-cov**: Test coverage
- **GitHub Actions**: CI/CD platform
