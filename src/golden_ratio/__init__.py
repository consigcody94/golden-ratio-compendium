"""
Golden Ratio Library

A comprehensive toolkit for working with the golden ratio (phi) and Fibonacci sequences.
Includes utilities for mathematics, design, finance, and more.
"""

from golden_ratio.constants import (
    PHI,
    PSI,
    GOLDEN_ANGLE,
    GOLDEN_ANGLE_DEGREES,
)
from golden_ratio.core import (
    GoldenRatio,
    GoldenRectangle,
)
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
)
from golden_ratio.design import DesignScale
from golden_ratio.trading import FibonacciTrading
from golden_ratio.phyllotaxis import Phyllotaxis
from golden_ratio.hashing import GoldenHash

__version__ = "1.0.0"
__all__ = [
    # Constants
    "PHI",
    "PSI",
    "GOLDEN_ANGLE",
    "GOLDEN_ANGLE_DEGREES",
    # Core classes
    "GoldenRatio",
    "GoldenRectangle",
    # Fibonacci
    "Fibonacci",
    "fib_iterative",
    "fib_binet",
    "fib_generator",
    "fib_matrix",
    "fib_fast_doubling",
    "lucas_number",
    "tribonacci",
    "is_fibonacci",
    # Design
    "DesignScale",
    # Trading
    "FibonacciTrading",
    # Phyllotaxis
    "Phyllotaxis",
    # Hashing
    "GoldenHash",
]
