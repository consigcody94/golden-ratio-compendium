# Contributing to Golden Ratio Compendium

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Development Setup

### Python

```bash
# Clone the repository
git clone https://github.com/golden-ratio-compendium/golden-ratio-compendium.git
cd golden-ratio-compendium

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linting
ruff check src/golden_ratio tests
black --check src/golden_ratio tests
mypy src/golden_ratio
```

### Rust

```bash
cd code/rust

# Run tests
cargo test

# Run clippy
cargo clippy

# Build
cargo build --release
```

### JavaScript

```bash
cd code/javascript

# Install dependencies
npm install

# Run demo
npm run demo
```

## Code Style

### Python
- Follow PEP 8 with a line length of 100 characters
- Use type hints for all public functions
- Write docstrings in Google style
- Format with `black` and lint with `ruff`

### Rust
- Follow standard Rust formatting (`cargo fmt`)
- Run `cargo clippy` for linting
- Write documentation for public items

### JavaScript
- Use ES6+ features
- Include JSDoc comments for functions
- Format with Prettier

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation if needed
7. Submit a pull request

## Types of Contributions

### Code Contributions
- New algorithms or implementations
- Bug fixes
- Performance improvements
- Additional language implementations

### Documentation
- Fix typos or clarify explanations
- Add new application examples
- Improve mathematical proofs
- Add citations and references

### Research
- Verify or debunk golden ratio claims
- Add scientific citations
- Provide evidence for applications

## Mathematical Accuracy

When contributing mathematical content:
- Ensure formulas are correct
- Provide proofs or references for claims
- Distinguish between verified and speculative applications
- Follow the evidence classification system (Verified/Plausible/Myth/Debunked)

## Questions?

Open an issue for:
- Feature requests
- Bug reports
- Questions about the codebase
- Clarifications about mathematical content
