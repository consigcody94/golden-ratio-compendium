# The Golden Ratio Compendium

> A comprehensive exploration of φ (phi) — the divine proportion that connects mathematics, nature, art, and modern technology.

```
φ = (1 + √5) / 2 ≈ 1.6180339887...
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

## Repository Structure

```
golden-ratio-compendium/
├── README.md                    # This file
├── docs/
│   ├── 01-mathematics.md        # Mathematical foundations
│   ├── 02-history.md            # Historical overview
│   ├── 03-nature.md             # Golden ratio in nature
│   ├── 04-art-architecture.md   # Art and architecture applications
│   ├── 05-design.md             # Modern design (UI/UX, typography)
│   ├── 06-music.md              # Music and acoustics
│   ├── 07-photography.md        # Photography composition
│   ├── 08-finance.md            # Financial markets & trading
│   ├── 09-computer-science.md   # Algorithms & data structures
│   ├── 10-myths-debunked.md     # Scientific criticism & myths
│   └── 11-logo-design.md        # Brand identity & logos
├── code/
│   ├── python/                  # Python implementations
│   ├── javascript/              # JavaScript implementations
│   └── rust/                    # Rust implementations
├── examples/
│   └── applications.md          # Real-world application examples
└── assets/                      # Images and diagrams
```

## Quick Start

### Calculate the Golden Ratio

```python
import math

phi = (1 + math.sqrt(5)) / 2
print(f"φ = {phi}")  # φ = 1.618033988749895
```

```javascript
const phi = (1 + Math.sqrt(5)) / 2;
console.log(`φ = ${phi}`);  // φ = 1.618033988749895
```

### Fibonacci & Golden Ratio Relationship

The ratio of consecutive Fibonacci numbers approaches φ:

| n | F(n) | F(n+1) | Ratio |
|---|------|--------|-------|
| 1 | 1 | 1 | 1.000 |
| 2 | 1 | 2 | 2.000 |
| 3 | 2 | 3 | 1.500 |
| 4 | 3 | 5 | 1.667 |
| 5 | 5 | 8 | 1.600 |
| 6 | 8 | 13 | 1.625 |
| 7 | 13 | 21 | 1.615 |
| 8 | 21 | 34 | 1.619 |
| 9 | 34 | 55 | 1.618 |
| 10 | 55 | 89 | 1.618 |

## Key Topics Covered

### Mathematics
- Derivation from quadratic equation x² - x - 1 = 0
- Binet's formula for Fibonacci numbers
- Continued fraction representation [1; 1, 1, 1, ...]
- Geometric constructions (pentagon, dodecahedron)

### Nature (Verified)
- **Phyllotaxis**: Leaf and seed arrangements in plants
- **Sunflower spirals**: 34/55 or 55/89 spiral patterns
- Plant growth patterns following Fibonacci sequences

### Art & Architecture
- **Le Corbusier's Modulor**: Human-scale proportioning system
- Classical architecture analysis
- Modern building design applications

### Modern Applications
- **UI/UX Design**: Layout proportions, spacing systems
- **Typography**: Font scaling ratios (1.618 type scale)
- **Logo Design**: Apple, Twitter, Pepsi, National Geographic
- **Photography**: Golden spiral composition
- **Finance**: Fibonacci retracement levels (38.2%, 61.8%)

### Computer Science
- **Golden-section search**: Optimization algorithm
- **Fibonacci heaps**: Efficient priority queue
- **Hashing**: Quasi-random number distribution
- **Algorithm analysis**: Time complexity calculations

## Critical Analysis

This compendium takes a **balanced, evidence-based approach**. We distinguish between:

- **Verified**: Strong scientific evidence
- **Plausible**: Some evidence, needs more research
- **Myth**: Little to no supporting evidence
- **Debunked**: Actively disproven claims

See [Myths Debunked](docs/10-myths-debunked.md) for critical analysis.

## Tools & Resources

### Calculators
- [Golden Ratio Calculator](code/python/calculator.py)
- [Typography Scale Generator](code/javascript/type-scale.js)
- [Fibonacci Sequence Generator](code/python/fibonacci.py)

### External Tools
- Adobe Photoshop/Lightroom golden ratio overlays
- [GRT Calculator](https://grtcalculator.com/) - Golden Ratio Typography
- [PhiMatrix](https://www.phimatrix.com/) - Design overlay software

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests for:
- Additional code implementations
- Research citations and references
- Corrections to mathematical content
- New application examples

## References

### Academic Sources
- Devlin, K. (2012). "The Myth That Will Not Go Away"
- Markowsky, G. (1992). "Misconceptions about the Golden Ratio"
- Livio, M. (2002). "The Golden Ratio: The Story of PHI"

### Key Websites
- [Golden Number](https://www.goldennumber.net/) - Comprehensive phi resource
- [Math is Fun](https://www.mathsisfun.com/numbers/golden-ratio.html) - Educational
- [Plus Magazine](https://plus.maths.org/content/myths-maths-golden-ratio) - Mathematical analysis

### Research Papers
- PMC: "The golden ratio—dispelling the myth" (2024)
- PMC: "New Golden Ratios for Facial Beauty"
- Fibonacci Quarterly journal archives

## License

MIT License - See [LICENSE](LICENSE) for details.

---

*"Geometry has two great treasures: one is the Theorem of Pythagoras; the other, the division of a line into extreme and mean ratio. The first we may compare to a measure of gold; the second we may name a precious jewel."* — Johannes Kepler

