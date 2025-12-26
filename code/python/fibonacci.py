#!/usr/bin/env python3
"""
Fibonacci Sequence Implementations

Multiple algorithms for computing Fibonacci numbers with different
time/space complexities. Includes analysis and comparison.
"""

import math
import time
from functools import lru_cache
from typing import List, Tuple, Generator
import numpy as np

# Constants
PHI = (1 + math.sqrt(5)) / 2
PSI = (1 - math.sqrt(5)) / 2


def fib_recursive(n: int) -> int:
    """
    Naive recursive Fibonacci.

    Time: O(φⁿ) - exponential
    Space: O(n) - call stack
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(maxsize=None)
def fib_memoized(n: int) -> int:
    """
    Memoized recursive Fibonacci.

    Time: O(n)
    Space: O(n)
    """
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)


def fib_iterative(n: int) -> int:
    """
    Iterative Fibonacci.

    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_generator(n: int) -> Generator[int, None, None]:
    """
    Generator for Fibonacci sequence.

    Time: O(n) total
    Space: O(1)
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_binet(n: int) -> int:
    """
    Binet's formula using golden ratio.

    Time: O(1) - but O(log n) for exponentiation
    Space: O(1)

    Warning: Loses precision for n > ~70
    """
    return round((PHI**n - PSI**n) / math.sqrt(5))


def fib_matrix(n: int) -> int:
    """
    Matrix exponentiation method.

    Time: O(log n)
    Space: O(1)

    Uses the identity:
    [[1, 1], [1, 0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]]
    """
    if n <= 1:
        return n

    def matrix_mult(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        return np.array([
            [A[0, 0] * B[0, 0] + A[0, 1] * B[1, 0],
             A[0, 0] * B[0, 1] + A[0, 1] * B[1, 1]],
            [A[1, 0] * B[0, 0] + A[1, 1] * B[1, 0],
             A[1, 0] * B[0, 1] + A[1, 1] * B[1, 1]]
        ], dtype=object)

    def matrix_pow(M: np.ndarray, p: int) -> np.ndarray:
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_pow(M, p // 2)
            return matrix_mult(half, half)
        return matrix_mult(M, matrix_pow(M, p - 1))

    F = np.array([[1, 1], [1, 0]], dtype=object)
    result = matrix_pow(F, n)
    return result[0, 1]


def fib_fast_doubling(n: int) -> int:
    """
    Fast doubling method.

    Time: O(log n)
    Space: O(log n) - recursion

    Uses identities:
    F(2k) = F(k) * [2*F(k+1) - F(k)]
    F(2k+1) = F(k)² + F(k+1)²
    """
    def fib_pair(n: int) -> Tuple[int, int]:
        """Returns (F(n), F(n+1))"""
        if n == 0:
            return (0, 1)

        a, b = fib_pair(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fib_pair(n)[0]


def lucas_number(n: int) -> int:
    """
    Calculate nth Lucas number.

    Lucas: 2, 1, 3, 4, 7, 11, 18, 29, 47...
    L(n) = L(n-1) + L(n-2), L(0)=2, L(1)=1

    Connected to Fibonacci:
    L(n) = F(n-1) + F(n+1)
    F(n) * L(n) = F(2n)
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def tribonacci(n: int) -> int:
    """
    Tribonacci sequence.

    T(n) = T(n-1) + T(n-2) + T(n-3)
    T(0)=0, T(1)=0, T(2)=1

    Ratio approaches the tribonacci constant: ~1.839
    """
    if n < 2:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


def fibonacci_properties(n: int) -> dict:
    """
    Calculate various Fibonacci-related properties for F(n).
    """
    fib_n = fib_iterative(n)
    fib_n1 = fib_iterative(n + 1) if n >= 0 else 0

    return {
        'n': n,
        'F(n)': fib_n,
        'F(n+1)': fib_n1,
        'ratio': fib_n1 / fib_n if fib_n > 0 else None,
        'ratio_error': abs(fib_n1 / fib_n - PHI) if fib_n > 0 else None,
        'L(n)': lucas_number(n),
        'is_prime': is_prime(fib_n),
        'digit_count': len(str(fib_n))
    }


def is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci_primes(max_index: int) -> List[Tuple[int, int]]:
    """Find Fibonacci primes up to index max_index."""
    primes = []
    for i in range(2, max_index + 1):
        f = fib_iterative(i)
        if is_prime(f):
            primes.append((i, f))
    return primes


def gcd_euclidean(a: int, b: int) -> Tuple[int, int]:
    """
    Euclidean algorithm with step count.

    Consecutive Fibonacci numbers are the worst case.
    """
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return a, steps


def benchmark_algorithms(n: int = 35) -> dict:
    """Benchmark different Fibonacci implementations."""
    results = {}

    # Skip recursive for large n (too slow)
    if n <= 35:
        start = time.perf_counter()
        fib_recursive(n)
        results['recursive'] = time.perf_counter() - start
    else:
        results['recursive'] = 'skipped (too slow)'

    start = time.perf_counter()
    fib_memoized(n)
    results['memoized'] = time.perf_counter() - start

    start = time.perf_counter()
    fib_iterative(n)
    results['iterative'] = time.perf_counter() - start

    start = time.perf_counter()
    fib_binet(n)
    results['binet'] = time.perf_counter() - start

    start = time.perf_counter()
    fib_matrix(n)
    results['matrix'] = time.perf_counter() - start

    start = time.perf_counter()
    fib_fast_doubling(n)
    results['fast_doubling'] = time.perf_counter() - start

    return results


def demo():
    """Demonstrate Fibonacci implementations."""
    print("=" * 60)
    print("FIBONACCI SEQUENCE IMPLEMENTATIONS")
    print("=" * 60)

    print("\n" + "-" * 40)
    print("First 20 Fibonacci Numbers")
    print("-" * 40)
    fibs = list(fib_generator(20))
    print(fibs)

    print("\n" + "-" * 40)
    print("Algorithm Comparison (n=35)")
    print("-" * 40)
    benchmarks = benchmark_algorithms(35)
    for algo, time_taken in benchmarks.items():
        if isinstance(time_taken, float):
            print(f"  {algo:15}: {time_taken*1000:.4f} ms")
        else:
            print(f"  {algo:15}: {time_taken}")

    print("\n" + "-" * 40)
    print("Ratio Convergence to φ")
    print("-" * 40)
    for i in range(1, 16):
        f_n = fib_iterative(i)
        f_n1 = fib_iterative(i + 1)
        ratio = f_n1 / f_n
        error = abs(ratio - PHI)
        print(f"  F({i+1})/F({i}) = {f_n1}/{f_n} = {ratio:.10f}, error = {error:.2e}")

    print("\n" + "-" * 40)
    print("Fibonacci Primes (first 12)")
    print("-" * 40)
    primes = fibonacci_primes(50)[:12]
    for idx, prime in primes:
        print(f"  F({idx}) = {prime}")

    print("\n" + "-" * 40)
    print("Lucas Numbers (first 15)")
    print("-" * 40)
    lucas = [lucas_number(i) for i in range(15)]
    print(f"  {lucas}")

    print("\n" + "-" * 40)
    print("Euclidean GCD - Worst Case (Fibonacci pairs)")
    print("-" * 40)
    for i in range(5, 15):
        a = fib_iterative(i + 1)
        b = fib_iterative(i)
        gcd, steps = gcd_euclidean(a, b)
        print(f"  gcd({a}, {b}) = {gcd}, steps = {steps}")

    print("\n" + "-" * 40)
    print("Tribonacci Numbers (first 15)")
    print("-" * 40)
    tribs = [tribonacci(i) for i in range(15)]
    print(f"  {tribs}")

    print("\n" + "-" * 40)
    print("Large Fibonacci Numbers")
    print("-" * 40)
    for n in [50, 100, 1000]:
        f = fib_fast_doubling(n)
        digits = len(str(f))
        print(f"  F({n}) has {digits} digits")
        if digits <= 20:
            print(f"    = {f}")


if __name__ == "__main__":
    demo()
