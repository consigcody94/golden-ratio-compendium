"""Tests for Fibonacci functions."""

import pytest

from golden_ratio.constants import PHI
from golden_ratio.fibonacci import (
    Fibonacci,
    fib_iterative,
    fib_binet,
    fib_generator,
    fib_matrix,
    fib_fast_doubling,
    lucas_number,
    tribonacci,
    is_fibonacci,
    is_prime,
    fibonacci_primes,
    gcd_euclidean,
)


class TestFibonacciClass:
    """Test Fibonacci class methods."""

    def test_sequence_empty(self):
        """Test empty sequence."""
        assert Fibonacci.sequence(0) == []
        assert Fibonacci.sequence(-1) == []

    def test_sequence_one(self):
        """Test sequence of length 1."""
        assert Fibonacci.sequence(1) == [1]

    def test_sequence_known_values(self):
        """Test first 10 Fibonacci numbers."""
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        assert Fibonacci.sequence(10) == expected

    def test_nth_zero(self):
        """Test nth with n=0."""
        assert Fibonacci.nth(0) == 0

    def test_nth_one(self):
        """Test nth with n=1."""
        assert Fibonacci.nth(1) == 1

    def test_nth_known_values(self):
        """Test known Fibonacci values."""
        assert Fibonacci.nth(10) == 55
        assert Fibonacci.nth(20) == 6765

    def test_ratio_convergence(self):
        """Test that ratios converge to PHI."""
        convergence = Fibonacci.ratio_convergence(20)
        # Last ratio should be very close to PHI
        last_ratio = convergence[-1][1]
        assert abs(last_ratio - PHI) < 1e-8


class TestFibonacciAlgorithms:
    """Test different Fibonacci algorithms."""

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
        (20, 6765),
    ])
    def test_fib_iterative(self, n, expected):
        """Test iterative Fibonacci."""
        assert fib_iterative(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (10, 55),
        (20, 6765),
    ])
    def test_fib_binet(self, n, expected):
        """Test Binet's formula."""
        assert fib_binet(n) == expected

    def test_fib_generator(self):
        """Test Fibonacci generator."""
        gen = fib_generator(10)
        result = list(gen)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert result == expected

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (10, 55),
        (20, 6765),
    ])
    def test_fib_matrix(self, n, expected):
        """Test matrix exponentiation method."""
        assert fib_matrix(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (10, 55),
        (20, 6765),
        (50, 12586269025),
    ])
    def test_fib_fast_doubling(self, n, expected):
        """Test fast doubling method."""
        assert fib_fast_doubling(n) == expected

    def test_algorithms_agree(self):
        """Test that all algorithms produce same result."""
        for n in [10, 15, 20, 25, 30]:
            iterative = fib_iterative(n)
            binet = fib_binet(n)
            matrix = fib_matrix(n)
            fast = fib_fast_doubling(n)

            assert iterative == binet == matrix == fast


class TestLucasNumbers:
    """Test Lucas number calculations."""

    def test_lucas_base_cases(self):
        """Test Lucas base cases."""
        assert lucas_number(0) == 2
        assert lucas_number(1) == 1

    def test_lucas_sequence(self):
        """Test first several Lucas numbers."""
        expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
        for i, exp in enumerate(expected):
            assert lucas_number(i) == exp


class TestTribonacci:
    """Test Tribonacci calculations."""

    def test_tribonacci_base_cases(self):
        """Test Tribonacci base cases."""
        assert tribonacci(0) == 0
        assert tribonacci(1) == 0
        assert tribonacci(2) == 1

    def test_tribonacci_sequence(self):
        """Test first several Tribonacci numbers."""
        expected = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
        for i, exp in enumerate(expected):
            assert tribonacci(i) == exp


class TestIsFibonacci:
    """Test is_fibonacci function."""

    def test_is_fibonacci_true(self):
        """Test known Fibonacci numbers."""
        fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for n in fib_numbers:
            assert is_fibonacci(n), f"{n} should be Fibonacci"

    def test_is_fibonacci_false(self):
        """Test non-Fibonacci numbers."""
        non_fib = [4, 6, 7, 9, 10, 11, 12, 14, 15]
        for n in non_fib:
            assert not is_fibonacci(n), f"{n} should not be Fibonacci"

    def test_is_fibonacci_negative(self):
        """Test negative numbers."""
        assert not is_fibonacci(-1)
        assert not is_fibonacci(-5)


class TestIsPrime:
    """Test is_prime function."""

    def test_primes(self):
        """Test known primes."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in primes:
            assert is_prime(p), f"{p} should be prime"

    def test_non_primes(self):
        """Test known non-primes."""
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
        for n in non_primes:
            assert not is_prime(n), f"{n} should not be prime"


class TestFibonacciPrimes:
    """Test fibonacci_primes function."""

    def test_first_fibonacci_primes(self):
        """Test first few Fibonacci primes."""
        primes = fibonacci_primes(15)
        # F(3)=2, F(4)=3, F(5)=5, F(7)=13, F(11)=89, F(13)=233
        expected_indices = [3, 4, 5, 7, 11, 13]
        actual_indices = [p[0] for p in primes]
        assert actual_indices == expected_indices


class TestGCDEuclidean:
    """Test gcd_euclidean function."""

    def test_gcd_basic(self):
        """Test basic GCD calculation."""
        gcd, _ = gcd_euclidean(48, 18)
        assert gcd == 6

    def test_gcd_coprime(self):
        """Test coprime numbers."""
        gcd, _ = gcd_euclidean(17, 13)
        assert gcd == 1

    def test_gcd_fibonacci_worst_case(self):
        """Test Fibonacci pairs (worst case)."""
        # Consecutive Fibonacci numbers require the most steps
        gcd, steps = gcd_euclidean(89, 55)
        assert gcd == 1
        assert steps == 10  # Should require many steps
