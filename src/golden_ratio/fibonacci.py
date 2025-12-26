"""
Fibonacci sequence implementations with various algorithms.

This module provides multiple algorithms for computing Fibonacci numbers,
each with different time and space complexity trade-offs.
"""

import math
from functools import lru_cache
from typing import Generator, List, Tuple

import numpy as np

from golden_ratio.constants import PHI, PSI


class Fibonacci:
    """Fibonacci sequence calculations."""

    @staticmethod
    def sequence(n: int) -> List[int]:
        """Generate the first n Fibonacci numbers.

        Args:
            n: Number of Fibonacci numbers to generate.

        Returns:
            List of the first n Fibonacci numbers.
        """
        if n <= 0:
            return []
        if n == 1:
            return [1]

        fib = [1, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

    @staticmethod
    def nth(n: int) -> int:
        """Calculate the nth Fibonacci number using iteration.

        Args:
            n: The index (1-based) of the Fibonacci number.

        Returns:
            The nth Fibonacci number.
        """
        if n <= 0:
            return 0
        if n <= 2:
            return 1

        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

    @staticmethod
    def nth_binet(n: int) -> int:
        """Calculate nth Fibonacci number using Binet's formula.

        Note: Loses precision for n > ~70 due to floating-point limitations.

        Args:
            n: The index of the Fibonacci number.

        Returns:
            The nth Fibonacci number (approximate for large n).
        """
        return round((PHI**n - PSI**n) / math.sqrt(5))

    @staticmethod
    def ratio_convergence(n: int = 20) -> List[Tuple[int, float, float]]:
        """Show how Fibonacci ratios converge to phi.

        Args:
            n: Number of ratios to compute.

        Returns:
            List of tuples (index, ratio, error from phi).
        """
        fib = Fibonacci.sequence(n + 1)
        convergence = []
        for i in range(1, len(fib)):
            ratio = fib[i] / fib[i - 1]
            error = abs(ratio - PHI)
            convergence.append((i, round(ratio, 10), error))
        return convergence


def fib_iterative(n: int) -> int:
    """Calculate nth Fibonacci number iteratively.

    Time: O(n), Space: O(1)

    Args:
        n: The index of the Fibonacci number (0-based).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@lru_cache(maxsize=None)
def fib_memoized(n: int) -> int:
    """Calculate nth Fibonacci number with memoization.

    Time: O(n), Space: O(n)

    Args:
        n: The index of the Fibonacci number (0-based).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)


def fib_generator(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence up to n numbers.

    Time: O(n) total, Space: O(1)

    Args:
        n: Number of Fibonacci numbers to generate.

    Yields:
        Fibonacci numbers in sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_binet(n: int) -> int:
    """Calculate nth Fibonacci using Binet's formula.

    Time: O(1) (but O(log n) for exponentiation), Space: O(1)
    Warning: Loses precision for n > ~70.

    Args:
        n: The index of the Fibonacci number.

    Returns:
        The nth Fibonacci number.
    """
    return round((PHI**n - PSI**n) / math.sqrt(5))


def fib_matrix(n: int) -> int:
    """Calculate nth Fibonacci using matrix exponentiation.

    Time: O(log n), Space: O(1)

    Uses the identity:
    [[1, 1], [1, 0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]]

    Args:
        n: The index of the Fibonacci number.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n

    def matrix_mult(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        return np.array(
            [
                [a[0, 0] * b[0, 0] + a[0, 1] * b[1, 0], a[0, 0] * b[0, 1] + a[0, 1] * b[1, 1]],
                [a[1, 0] * b[0, 0] + a[1, 1] * b[1, 0], a[1, 0] * b[0, 1] + a[1, 1] * b[1, 1]],
            ],
            dtype=object,
        )

    def matrix_pow(m: np.ndarray, p: int) -> np.ndarray:
        if p == 1:
            return m
        if p % 2 == 0:
            half = matrix_pow(m, p // 2)
            return matrix_mult(half, half)
        return matrix_mult(m, matrix_pow(m, p - 1))

    f = np.array([[1, 1], [1, 0]], dtype=object)
    result = matrix_pow(f, n)
    return result[0, 1]


def fib_fast_doubling(n: int) -> int:
    """Calculate nth Fibonacci using fast doubling method.

    Time: O(log n), Space: O(log n) for recursion

    Uses identities:
    F(2k) = F(k) * [2*F(k+1) - F(k)]
    F(2k+1) = F(k)^2 + F(k+1)^2

    Args:
        n: The index of the Fibonacci number.

    Returns:
        The nth Fibonacci number.
    """

    def fib_pair(k: int) -> Tuple[int, int]:
        """Return (F(k), F(k+1))."""
        if k == 0:
            return (0, 1)

        a, b = fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b

        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fib_pair(n)[0]


def lucas_number(n: int) -> int:
    """Calculate the nth Lucas number.

    Lucas sequence: 2, 1, 3, 4, 7, 11, 18, 29, 47...
    L(n) = L(n-1) + L(n-2), with L(0)=2, L(1)=1

    Connection to Fibonacci:
    - L(n) = F(n-1) + F(n+1)
    - F(n) * L(n) = F(2n)

    Args:
        n: The index of the Lucas number.

    Returns:
        The nth Lucas number.
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
    """Calculate the nth Tribonacci number.

    T(n) = T(n-1) + T(n-2) + T(n-3)
    with T(0)=0, T(1)=0, T(2)=1

    The ratio of consecutive Tribonacci numbers approaches
    the Tribonacci constant (~1.839).

    Args:
        n: The index of the Tribonacci number.

    Returns:
        The nth Tribonacci number.
    """
    if n < 2:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


def is_fibonacci(n: int) -> bool:
    """Check if a number is a Fibonacci number.

    A number is Fibonacci if one of 5n^2 + 4 or 5n^2 - 4 is a perfect square.

    Args:
        n: The number to check.

    Returns:
        True if n is a Fibonacci number.
    """
    if n < 0:
        return False

    def is_perfect_square(x: int) -> bool:
        if x < 0:
            return False
        sqrt = int(math.sqrt(x))
        return sqrt * sqrt == x

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if n is prime.
    """
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
    """Find Fibonacci primes up to a given index.

    Args:
        max_index: Maximum Fibonacci index to check.

    Returns:
        List of (index, Fibonacci prime) tuples.
    """
    primes = []
    for i in range(2, max_index + 1):
        f = fib_iterative(i)
        if is_prime(f):
            primes.append((i, f))
    return primes


def gcd_euclidean(a: int, b: int) -> Tuple[int, int]:
    """Calculate GCD using Euclidean algorithm with step count.

    Consecutive Fibonacci numbers are the worst case for this algorithm.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Tuple of (GCD, number of steps).
    """
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return a, steps
