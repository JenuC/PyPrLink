# Contributing to PyPrLink

Thank you for your interest in contributing to PyPrLink! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a respectful and inclusive community.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/PyPrLink.git
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests:
   ```bash
   pytest
   ```

4. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions and classes
- Keep functions focused and small
- Use meaningful variable names

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Include both unit and integration tests
- Use pytest for testing

## Documentation

- Update documentation for new features
- Follow the existing documentation style
- Include examples where appropriate
- Update the changelog

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.md with details of changes
3. The PR will be merged once you have the sign-off of at least one maintainer

## Reporting Issues

- Use the GitHub issue tracker
- Include a clear description of the problem
- Provide steps to reproduce
- Include system information
- Add relevant logs

## Feature Requests

- Use the GitHub issue tracker
- Clearly describe the feature
- Explain why it would be useful
- Provide examples if possible

## Questions?

Feel free to open an issue for any questions about contributing.
