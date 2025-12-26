# The Golden Ratio in Computer Science

## Algorithms

### Golden-Section Search

An optimization algorithm for finding the minimum (or maximum) of a unimodal function. It's similar to binary search but uses the golden ratio for dividing the search space.

#### Why Golden Ratio?

The golden ratio ensures that:
- Only one new function evaluation per iteration
- Optimal reduction of search space
- Reuses one boundary point from previous iteration

#### Algorithm

```python
def golden_section_search(f, a, b, tol=1e-6):
    """
    Find minimum of unimodal function f on interval [a, b]

    Uses the golden ratio to efficiently narrow the search space.
    Converges in O(log(1/tol)) iterations.
    """
    phi = (1 + 5**0.5) / 2
    resphi = 2 - phi  # 1/φ ≈ 0.618

    # Initial points
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1, f2 = f(x1), f(x2)

    while abs(b - a) > tol:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)

    return (a + b) / 2


# Example: Find minimum of x² - 4x + 4 (minimum at x=2)
result = golden_section_search(lambda x: x**2 - 4*x + 4, 0, 5)
print(f"Minimum at x = {result}")  # ~2.0
```

#### Convergence

Each iteration reduces the interval by factor of φ:
```
Iteration 1: interval = original / φ
Iteration 2: interval = original / φ²
Iteration n: interval = original / φⁿ
```

### Comparison with Binary Search

| Property | Binary Search | Golden Section |
|----------|--------------|----------------|
| Evaluations/iteration | 2 | 1 |
| Reduction ratio | 0.5 | 0.618 |
| Use case | Sorted arrays | Unimodal functions |
| Total evaluations | O(log n) | O(log n) |

---

## Data Structures

### Fibonacci Heap

A heap data structure with excellent amortized time complexity, used in:
- Dijkstra's shortest path algorithm
- Prim's minimum spanning tree algorithm

#### Why "Fibonacci"?

The maximum degree of any node is O(log n), and the number of nodes in a subtree rooted at a degree-k node is at least F(k+2) (the (k+2)th Fibonacci number).

#### Time Complexities

| Operation | Binary Heap | Fibonacci Heap |
|-----------|------------|----------------|
| Insert | O(log n) | O(1) amortized |
| Find-min | O(1) | O(1) |
| Delete-min | O(log n) | O(log n) amortized |
| Decrease-key | O(log n) | O(1) amortized |
| Merge | O(n) | O(1) |

### Fibonacci Trees

AVL trees where each node's subtree follows Fibonacci structure:

```
            Fib(5)=5
           /       \
      Fib(4)=3    Fib(3)=2
       /   \        /   \
    Fib(3) Fib(2) Fib(2) Fib(1)
      =2     =1     =1     =1
```

The minimum number of nodes in an AVL tree of height h is F(h+2) - 1.

---

## Hashing and Distribution

### Golden Ratio Hashing

The golden ratio is optimal for hash distribution because φ is the "most irrational" number—it has the worst rational approximation.

#### Multiplicative Hashing

```python
def golden_hash(key, table_size):
    """
    Hash using golden ratio multiplication method.

    The golden ratio ensures maximum distribution of sequential keys.
    """
    phi = (5**0.5 - 1) / 2  # 1/φ ≈ 0.618033988749895

    # Multiply and take fractional part
    fractional = (key * phi) % 1

    # Scale to table size
    return int(table_size * fractional)


# Sequential keys distribute well
for i in range(10):
    print(f"Key {i} -> Bucket {golden_hash(i, 100)}")
```

Output:
```
Key 0 -> Bucket 0
Key 1 -> Bucket 61
Key 2 -> Bucket 23
Key 3 -> Bucket 85
Key 4 -> Bucket 47
Key 5 -> Bucket 9
Key 6 -> Bucket 70
Key 7 -> Bucket 32
Key 8 -> Bucket 94
Key 9 -> Bucket 56
```

Notice: No clustering of sequential keys!

#### Why It Works

The continued fraction of 1/φ = [0; 1, 1, 1, 1, ...] has all 1s, making it the "worst approximable" number. This means multiples of 1/φ are maximally spread across [0, 1).

### Low-Discrepancy Sequences

For quasi-random sequences (Monte Carlo simulation, sampling):

```python
def golden_sequence(n):
    """Generate n points using golden ratio for low discrepancy"""
    phi = (1 + 5**0.5) / 2
    return [(i / phi) % 1 for i in range(n)]

# First 10 points
points = golden_sequence(10)
# Well-distributed across [0, 1)
```

---

## Fibonacci Sequence Computation

### Methods and Complexities

| Method | Time | Space |
|--------|------|-------|
| Naive recursion | O(φⁿ) | O(n) |
| Memoization | O(n) | O(n) |
| Iteration | O(n) | O(1) |
| Matrix exponentiation | O(log n) | O(1) |
| Binet's formula | O(1)* | O(1) |

*Binet's formula has precision issues for large n

### Matrix Exponentiation

```python
import numpy as np

def fib_matrix(n):
    """Calculate F(n) using matrix exponentiation in O(log n)"""
    if n <= 1:
        return n

    def matrix_mult(A, B):
        return np.array([
            [A[0,0]*B[0,0] + A[0,1]*B[1,0], A[0,0]*B[0,1] + A[0,1]*B[1,1]],
            [A[1,0]*B[0,0] + A[1,1]*B[1,0], A[1,0]*B[0,1] + A[1,1]*B[1,1]]
        ], dtype=object)

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_pow(M, p // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(M, matrix_pow(M, p - 1))

    fib_matrix = np.array([[1, 1], [1, 0]], dtype=object)
    result = matrix_pow(fib_matrix, n)
    return result[0, 1]
```

### Binet's Formula Implementation

```python
import math

def fib_binet(n):
    """
    Calculate F(n) using Binet's formula.

    Warning: Loses precision for n > ~70 due to floating-point.
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    return round((phi**n - psi**n) / math.sqrt(5))

# Works well for small n
for i in range(20):
    print(f"F({i}) = {fib_binet(i)}")
```

---

## Algorithm Analysis

### Euclidean Algorithm

The golden ratio appears in the analysis of the Euclidean algorithm for GCD:

**Worst case**: Consecutive Fibonacci numbers require the most steps.

```python
def gcd_steps(a, b):
    """Count steps in Euclidean algorithm"""
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return steps

# Fibonacci numbers are worst case
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
for i in range(1, len(fib)):
    steps = gcd_steps(fib[i], fib[i-1])
    print(f"gcd({fib[i]}, {fib[i-1]}) takes {steps} steps")
```

**Theorem (Lamé, 1844)**: The number of steps is at most 5 times the number of digits in the smaller number.

### Fibonacci Search

Alternative to binary search that uses Fibonacci numbers:

```python
def fibonacci_search(arr, target):
    """
    Search sorted array using Fibonacci numbers.

    Useful when array access cost varies (e.g., tape drives).
    """
    n = len(arr)

    # Generate Fibonacci numbers
    fib2 = 0  # F(k-2)
    fib1 = 1  # F(k-1)
    fib = fib1 + fib2  # F(k)

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1
```

---

## Random Number Generation

### Weyl Sequence

Using the golden ratio for quasi-random numbers:

```python
class GoldenWeyl:
    """Quasi-random number generator using golden ratio"""

    def __init__(self, seed=0.5):
        self.phi = (5**0.5 - 1) / 2  # 1/φ
        self.state = seed

    def next(self):
        self.state = (self.state + self.phi) % 1
        return self.state

    def next_n(self, n):
        return [self.next() for _ in range(n)]


# Generate 10 quasi-random numbers
gen = GoldenWeyl()
numbers = gen.next_n(10)
print(numbers)
```

### 2D Distribution

For placing points in 2D (e.g., sampling, dithering):

```python
def golden_points_2d(n):
    """Generate n well-distributed 2D points using golden ratio"""
    phi = (1 + 5**0.5) / 2
    points = []
    for i in range(n):
        x = (i / phi) % 1
        y = (i / (phi ** 2)) % 1
        points.append((x, y))
    return points
```

---

## Graphics and Visualization

### Golden Spiral Rendering

```python
import matplotlib.pyplot as plt
import numpy as np

def draw_golden_spiral(ax, n_quarters=10):
    """Draw a golden spiral using quarter circles"""
    phi = (1 + np.sqrt(5)) / 2

    # Fibonacci-like scaling
    scale = 1
    x, y = 0, 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Up, Left, Down

    for i in range(n_quarters):
        # Draw quarter circle
        theta = np.linspace(0, np.pi/2, 50)
        dir_idx = i % 4

        # Calculate arc
        if dir_idx == 0:
            cx, cy = x + scale, y
            arc_x = cx - scale * np.cos(theta)
            arc_y = cy + scale * np.sin(theta)
            x, y = x + scale, y + scale
        elif dir_idx == 1:
            cx, cy = x, y + scale
            arc_x = cx - scale * np.sin(theta)
            arc_y = cy - scale * np.cos(theta)
            x, y = x - scale, y + scale
        elif dir_idx == 2:
            cx, cy = x - scale, y
            arc_x = cx + scale * np.cos(theta)
            arc_y = cy - scale * np.sin(theta)
            x, y = x - scale, y - scale
        else:
            cx, cy = x, y - scale
            arc_x = cx + scale * np.sin(theta)
            arc_y = cy + scale * np.cos(theta)
            x, y = x + scale, y - scale

        ax.plot(arc_x, arc_y, 'b-', linewidth=2)

        # Next scale
        scale *= phi

    ax.set_aspect('equal')
    ax.axis('off')
```

### Phyllotaxis Visualization

```python
def draw_phyllotaxis(ax, n_points=500):
    """Draw sunflower seed pattern"""
    golden_angle = np.pi * (3 - np.sqrt(5))  # ~137.5° in radians

    r = np.sqrt(np.arange(n_points))
    theta = golden_angle * np.arange(n_points)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    ax.scatter(x, y, c=np.arange(n_points), cmap='viridis', s=20)
    ax.set_aspect('equal')
    ax.axis('off')
```

---

## Practical Applications

### UI/UX Component Sizing

```python
def golden_sizes(base, n_larger=3, n_smaller=3):
    """Generate size scale based on golden ratio"""
    phi = (1 + 5**0.5) / 2
    sizes = {'base': base}

    for i in range(1, n_larger + 1):
        sizes[f'lg{i}'] = round(base * (phi ** i), 2)

    for i in range(1, n_smaller + 1):
        sizes[f'sm{i}'] = round(base / (phi ** i), 2)

    return sizes

print(golden_sizes(16))
# {'base': 16, 'lg1': 25.89, 'lg2': 41.89, 'lg3': 67.77,
#  'sm1': 9.89, 'sm2': 6.11, 'sm3': 3.78}
```

### Animation Timing

```python
def golden_easing(t):
    """Easing function based on golden ratio"""
    phi = (1 + 5**0.5) / 2
    return t ** phi / (t ** phi + (1 - t) ** phi)

# Creates a smooth S-curve with golden-ratio-based inflection
```

---

## Summary Table

| Application | How Golden Ratio is Used |
|-------------|--------------------------|
| Golden-section search | Optimal interval reduction |
| Fibonacci heap | Subtree size bounds |
| Hashing | Maximum dispersion |
| GCD analysis | Worst-case bound |
| Quasi-random | Low-discrepancy sequences |
| Graphics | Spiral generation |

## References

1. Wikipedia: "Golden-section search"
2. GeeksforGeeks: "Fibonacci Numbers in Computer Science"
3. Knuth, D. (1997). *The Art of Computer Programming*, Vol. 1
4. Cormen et al. *Introduction to Algorithms* (Fibonacci heaps)
