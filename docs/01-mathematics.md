# Mathematics of the Golden Ratio

## Definition

The Golden Ratio (φ, phi) is defined as the positive solution to the quadratic equation:

```
x² - x - 1 = 0
```

Using the quadratic formula:

```
       -(-1) ± √((-1)² - 4(1)(-1))
x = ────────────────────────────────
              2(1)

       1 ± √5
x = ──────────
         2
```

This gives us:
- **φ (Phi)** = (1 + √5) / 2 ≈ **1.6180339887498948482...**
- **ψ (psi)** = (1 - √5) / 2 ≈ -0.6180339887498948482...

## Fundamental Properties

### Self-Referential Nature

The golden ratio is unique in that it can be defined in terms of itself:

```
φ = 1 + 1/φ
```

This leads to the remarkable property:

```
φ² = φ + 1 = 2.6180339887...
```

### Reciprocal Relationship

```
1/φ = φ - 1 = 0.6180339887...
```

The decimal portions of φ and 1/φ are identical!

### Powers of Phi

| Power | Expression | Approximate Value |
|-------|------------|-------------------|
| φ⁻² | 2 - φ | 0.3819660113 |
| φ⁻¹ | φ - 1 | 0.6180339887 |
| φ⁰ | 1 | 1.0000000000 |
| φ¹ | φ | 1.6180339887 |
| φ² | φ + 1 | 2.6180339887 |
| φ³ | 2φ + 1 | 4.2360679775 |
| φ⁴ | 3φ + 2 | 6.8541019662 |
| φ⁵ | 5φ + 3 | 11.0901699437 |

**Pattern**: φⁿ = F(n)φ + F(n-1), where F(n) is the nth Fibonacci number.

## Continued Fraction Representation

The golden ratio has the simplest possible infinite continued fraction:

```
φ = 1 + 1/(1 + 1/(1 + 1/(1 + 1/(1 + ...))))
```

Or in compact notation:
```
φ = [1; 1, 1, 1, 1, ...]
```

This makes φ the "most irrational" number—it converges the slowest of all continued fractions.

## Binet's Formula

Named after Jacques Philippe Marie Binet (though discovered earlier by de Moivre and Euler), this formula calculates the nth Fibonacci number directly using the golden ratio:

```
        φⁿ - ψⁿ       φⁿ - (-1/φ)ⁿ
F(n) = ─────────  =  ────────────────
          √5              √5
```

For large n, since |ψ| < 1, the ψⁿ term becomes negligible:

```
F(n) ≈ φⁿ / √5  (rounded to nearest integer)
```

### Example Calculation

For n = 10:
```
F(10) = (φ¹⁰ - ψ¹⁰) / √5
      = (122.9919... - 0.0081...) / 2.236...
      = 122.9838... / 2.236...
      = 55
```

## Fibonacci Sequence Connection

The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

The ratio of consecutive terms approaches φ:

```python
def fibonacci_ratio_convergence():
    a, b = 1, 1
    phi = (1 + 5**0.5) / 2
    for i in range(20):
        ratio = b / a
        error = abs(ratio - phi)
        print(f"F({i+2})/F({i+1}) = {ratio:.10f}, error = {error:.2e}")
        a, b = b, a + b
```

Output:
```
F(2)/F(1) = 1.0000000000, error = 6.18e-01
F(3)/F(2) = 2.0000000000, error = 3.82e-01
F(4)/F(3) = 1.5000000000, error = 1.18e-01
F(5)/F(4) = 1.6666666667, error = 4.86e-02
...
F(19)/F(18) = 1.6180339632, error = 2.55e-08
F(20)/F(19) = 1.6180339985, error = 9.77e-09
```

## Geometric Constructions

### The Golden Rectangle

A rectangle with sides in the ratio 1:φ. When you remove a square from a golden rectangle, the remaining rectangle is also golden.

```
┌────────────────────┐
│          │         │
│  Square  │ Golden  │
│   (1×1)  │ Rect    │
│          │ (φ-1×1) │
└────────────────────┘
      φ = 1.618...
```

### The Golden Triangle

An isoceles triangle with:
- Two equal sides of length φ
- Base of length 1
- Angles: 72°, 72°, 36°

### Pentagon and Pentagram

The golden ratio appears extensively in regular pentagons:

```
      ★
     /│\
    / │ \
   /  │  \
  /   │   \
 ★────★────★
  \   │   /
   \  │  /
    \ │ /
     \│/
      ★
```

- Diagonal to side ratio = φ
- Each intersection creates more golden ratios
- The ratio appears 10+ times in a pentagram

### Golden Spiral

Created by connecting quarter circles in nested golden rectangles:

```
Radius of each quarter arc = F(n)
Where F(n) is the Fibonacci sequence

Arc 1: radius = 1
Arc 2: radius = 1
Arc 3: radius = 2
Arc 4: radius = 3
Arc 5: radius = 5
Arc 6: radius = 8
...
```

## Algebraic Identity Summary

| Identity | Description |
|----------|-------------|
| φ² = φ + 1 | Defining property |
| φ = 1 + 1/φ | Self-reference |
| 1/φ = φ - 1 | Reciprocal |
| φ × (φ-1) = 1 | Product relationship |
| φ + (1/φ) = √5 | Sum relationship |
| φ - (1/φ) = 1 | Difference relationship |
| φⁿ + φ⁻ⁿ = L(n) | Lucas numbers |
| φⁿ - φ⁻ⁿ = F(n)√5 | Fibonacci relation |

## Lucas Numbers

Related sequence: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76...

```
L(n) = L(n-1) + L(n-2)
L(n) = φⁿ + ψⁿ
```

Connection to Fibonacci:
```
L(n) = F(n-1) + F(n+1)
F(n) × L(n) = F(2n)
```

## Matrix Representation

The Fibonacci matrix:

```
    ┌     ┐ⁿ    ┌              ┐
    │ 1 1 │  =  │ F(n+1)  F(n) │
    │ 1 0 │     │ F(n)  F(n-1) │
    └     ┘     └              ┘
```

Eigenvalues of this matrix are φ and ψ!

## Trigonometric Relationships

```
cos(36°) = φ/2
cos(72°) = (φ-1)/2
sin(18°) = (φ-1)/2
sin(54°) = φ/2

2cos(π/5) = φ
2sin(π/10) = 1/φ
```

## Nested Radicals

```
φ = √(1 + √(1 + √(1 + √(1 + ...))))
```

Proof:
Let x = √(1 + √(1 + √(1 + ...)))
Then x = √(1 + x)
x² = 1 + x
x² - x - 1 = 0
x = φ (taking positive root)

## References

1. Livio, M. (2002). *The Golden Ratio: The Story of PHI*
2. Dunlap, R. A. (1997). *The Golden Ratio and Fibonacci Numbers*
3. Posamentier, A. S. & Lehmann, I. (2011). *The Glorious Golden Ratio*
