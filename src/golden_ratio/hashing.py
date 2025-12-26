"""
Golden ratio based hashing utilities.

The golden ratio provides excellent distribution properties for hash functions,
making it useful for hash tables and quasi-random number generation.
"""

import math
from typing import List

from golden_ratio.constants import INV_PHI


class GoldenHash:
    """Golden ratio based hashing utilities."""

    @staticmethod
    def hash(key: int, table_size: int) -> int:
        """Hash using golden ratio multiplication method.

        This method provides excellent distribution for sequential keys,
        which often cause clustering with simpler hash functions.

        The technique multiplies the key by the inverse of phi,
        takes the fractional part, and scales to the table size.

        Args:
            key: The key to hash.
            table_size: Size of the hash table.

        Returns:
            Hash value in range [0, table_size).

        Example:
            >>> GoldenHash.hash(1, 100)  # 61
            >>> GoldenHash.hash(2, 100)  # 23
            >>> # Sequential keys are well-distributed
        """
        fractional = (key * INV_PHI) % 1
        return int(table_size * fractional)

    @staticmethod
    def weyl_sequence(n: int, seed: float = 0.5) -> List[float]:
        """Generate quasi-random numbers using the golden ratio.

        The Weyl sequence uses the irrational nature of phi to produce
        well-distributed values that avoid clustering.

        Args:
            n: Number of values to generate.
            seed: Starting value in [0, 1).

        Returns:
            List of quasi-random values in [0, 1).

        Example:
            >>> values = GoldenHash.weyl_sequence(10)
            >>> # Values are evenly distributed across [0, 1)
        """
        sequence = []
        state = seed
        for _ in range(n):
            state = (state + INV_PHI) % 1
            sequence.append(round(state, 6))
        return sequence

    @staticmethod
    def low_discrepancy_sequence(n: int, dimensions: int = 1) -> List[List[float]]:
        """Generate multi-dimensional low-discrepancy sequence.

        Uses different irrational bases for each dimension based on
        generalized golden ratio concepts.

        Args:
            n: Number of points to generate.
            dimensions: Number of dimensions.

        Returns:
            List of points, each point is a list of coordinates.
        """
        # Generalized golden ratio for each dimension
        def generalized_phi(d: int) -> float:
            """Calculate generalized golden ratio for dimension d."""
            # Uses the plastic constant for higher dimensions
            if d == 1:
                return INV_PHI
            elif d == 2:
                # Plastic constant inverse
                return 0.7548776662466927
            else:
                # Approximate using nth root of phi
                return 1 / (1.0 + math.sqrt(d))

        points = []
        bases = [generalized_phi(d + 1) for d in range(dimensions)]

        for i in range(n):
            point = []
            for d in range(dimensions):
                value = (0.5 + (i + 1) * bases[d]) % 1
                point.append(round(value, 6))
            points.append(point)

        return points

    @staticmethod
    def fibonacci_hash(key: int, table_size: int) -> int:
        """Fibonacci hashing using the Knuth multiplicative method.

        Uses the integer approximation of 2^w * (phi - 1) where w is
        the word size.

        Args:
            key: The key to hash.
            table_size: Size of the hash table (should be power of 2).

        Returns:
            Hash value in range [0, table_size).
        """
        # For 64-bit: 2^64 * (phi - 1) ≈ 11400714819323198485
        # For 32-bit: 2^32 * (phi - 1) ≈ 2654435769
        fib_mult = 11400714819323198485

        # Determine the number of bits needed for table_size
        bits = table_size.bit_length()

        # Multiply and extract top bits
        product = (key * fib_mult) & ((1 << 64) - 1)
        return product >> (64 - bits)
