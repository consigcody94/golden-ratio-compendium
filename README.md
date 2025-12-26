# The Golden Ratio Compendium

[![CI](https://github.com/golden-ratio-compendium/golden-ratio-compendium/actions/workflows/ci.yml/badge.svg)](https://github.com/golden-ratio-compendium/golden-ratio-compendium/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A comprehensive exploration of φ (phi) — the divine proportion that connects mathematics, nature, art, and modern technology.

```
φ = (1 + √5) / 2 ≈ 1.6180339887...
```

## Installation

### Python Package

```bash
# Install from source
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"

# Or install dependencies only
pip install -r requirements.txt
```

### CLI Tool

After installation, use the command-line tool:

```bash
# Display golden ratio information
golden-ratio info

# Generate Fibonacci sequence
golden-ratio fib 20 --ratios

# Calculate golden rectangle dimensions
golden-ratio rect --width 1920

# Generate design scales
golden-ratio scale --base 16

# Calculate Fibonacci trading levels
golden-ratio trading 200 100

# Calculate nth Fibonacci number
golden-ratio nth 100
```

### Rust Library

```bash
cd code/rust
cargo build --release
cargo test
```

### JavaScript/Node.js

```bash
cd code/javascript
npm install
npm run demo
```

## What is the Golden Ratio?

The **Golden Ratio** (φ, phi) is an irrational number approximately equal to **1.618033988749895**. It occurs when a line is divided into two parts such that the ratio of the whole line to the longer part equals the ratio of the longer part to the shorter part.

```
a + b     a
───── = ───── = φ ≈ 1.618
  a       b
```

### Mathematical Properties

| Property | Formula | Value |
|----------|---------|-------|
| Phi (φ) | (1 + √5) / 2 | 1.6180339887... |
| Inverse | 1/φ = φ - 1 | 0.6180339887... |
| Square | φ² = φ + 1 | 2.6180339887... |
| Cube | φ³ = 2φ + 1 | 4.2360679774... |

## Quick Start

### Python Library

```python
from golden_ratio import PHI, GoldenRatio, Fibonacci, DesignScale

# Basic calculations
print(f"φ = {PHI}")
print(f"1/φ = {GoldenRatio.inverse_phi()}")

# Fibonacci sequence
fib = Fibonacci.sequence(10)
print(f"Fibonacci: {fib}")

# Design scale
scale = DesignScale.type_scale(16)
print(f"Typography: {scale}")
```

### JavaScript

```javascript
const { PHI, generateTypeScale, generateSpacingScale } = require('./type-scale');

console.log(`φ = ${PHI}`);

const typeScale = generateTypeScale(16, PHI, 6);
console.log('Type scale:', typeScale);

const spacing = generateSpacingScale(8);
console.log('Spacing:', spacing);
```

## Repository Structure

```
golden-ratio-compendium/
├── README.md                    # This file
├── pyproject.toml               # Python package configuration
├── requirements.txt             # Python dependencies
├── src/
│   └── golden_ratio/            # Python package
│       ├── __init__.py
│       ├── constants.py         # Mathematical constants
│       ├── core.py              # Core calculations
│       ├── fibonacci.py         # Fibonacci implementations
│       ├── design.py            # Design scale utilities
│       ├── trading.py           # Trading calculations
│       ├── phyllotaxis.py       # Natural patterns
│       ├── hashing.py           # Hash utilities
│       └── cli.py               # Command-line interface
├── tests/                       # Python test suite
├── docs/
│   ├── INDEX.md                 # Documentation index
│   ├── 01-mathematics.md        # Mathematical foundations
│   ├── 02-history.md            # Historical overview
│   ├── 03-nature.md             # Golden ratio in nature
│   ├── 04-art-architecture.md   # Art and architecture
│   ├── 05-design.md             # Modern design (UI/UX)
│   ├── 06-music.md              # Music and acoustics
│   ├── 07-photography.md        # Photography composition
│   ├── 08-finance.md            # Financial markets
│   ├── 09-computer-science.md   # Algorithms
│   ├── 10-myths-debunked.md     # Critical analysis
│   └── 11-logo-design.md        # Brand identity
├── code/
│   ├── python/                  # Legacy Python scripts
│   ├── javascript/              # JavaScript implementations
│   └── rust/                    # Rust implementations
├── examples/
│   └── applications.md          # Real-world examples
└── .github/
    └── workflows/               # CI/CD configuration
```

## Documentation

See the [Documentation Index](docs/INDEX.md) for a complete guide.

### Key Topics

| Topic | Description |
|-------|-------------|
| [Mathematics](docs/01-mathematics.md) | Proofs, formulas, geometric constructions |
| [Nature](docs/03-nature.md) | Phyllotaxis, spirals, growth patterns |
| [Design](docs/05-design.md) | Typography, spacing, UI/UX |
| [Computer Science](docs/09-computer-science.md) | Algorithms, data structures |
| [Myths Debunked](docs/10-myths-debunked.md) | Critical analysis |

## Critical Analysis

This compendium takes a **balanced, evidence-based approach**. We classify claims using:

| Level | Meaning |
|-------|---------|
| **Verified** ✓ | Strong scientific evidence |
| **Plausible** ~ | Some evidence, needs research |
| **Overstated** ! | Exaggerated claims |
| **Myth** ✗ | No supporting evidence |
| **Debunked** ✗✗ | Actively disproven |

See [Myths Debunked](docs/10-myths-debunked.md) for detailed analysis.

## Testing

```bash
# Run Python tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=golden_ratio

# Run Rust tests
cd code/rust && cargo test

# Run JavaScript demo
cd code/javascript && npm run demo
```

## Contributing

Contributions are welcome! See our [Contributing Guide](.github/CONTRIBUTING.md).

- Bug reports and feature requests via issues
- Code improvements via pull requests
- Documentation corrections and additions
- New application examples with citations

## References

### Academic Sources
- Devlin, K. (2012). "The Myth That Will Not Go Away"
- Markowsky, G. (1992). "Misconceptions about the Golden Ratio"
- Livio, M. (2002). "The Golden Ratio: The Story of PHI"

### Research Papers
- "The golden ratio—dispelling the myth" (PMC, 2024)
- "New Golden Ratios for Facial Beauty" (PMC)
- Fibonacci Quarterly journal archives

## License

MIT License - See [LICENSE](LICENSE) for details.

---

*"Geometry has two great treasures: one is the Theorem of Pythagoras; the other, the division of a line into extreme and mean ratio. The first we may compare to a measure of gold; the second we may name a precious jewel."* — Johannes Kepler
