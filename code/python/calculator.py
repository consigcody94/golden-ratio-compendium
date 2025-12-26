#!/usr/bin/env python3
"""
Golden Ratio Calculator

A comprehensive toolkit for working with the golden ratio (φ).
Includes calculations for design, finance, and mathematics.
"""

import math
from typing import List, Tuple, Dict, Optional

# Constants
PHI = (1 + math.sqrt(5)) / 2  # 1.6180339887498948482...
PSI = (1 - math.sqrt(5)) / 2  # -0.6180339887498948482...
GOLDEN_ANGLE = math.pi * (3 - math.sqrt(5))  # ~137.5° in radians
GOLDEN_ANGLE_DEGREES = 360 / (PHI ** 2)  # ~137.5077°


class GoldenRatio:
    """Golden ratio calculations and utilities."""

    @staticmethod
    def phi() -> float:
        """Return the golden ratio φ."""
        return PHI

    @staticmethod
    def inverse_phi() -> float:
        """Return 1/φ (also equals φ - 1)."""
        return 1 / PHI

    @staticmethod
    def phi_power(n: int) -> float:
        """Return φ^n."""
        return PHI ** n

    @staticmethod
    def is_golden_ratio(a: float, b: float, tolerance: float = 0.01) -> bool:
        """
        Check if two values are in golden ratio.

        Args:
            a: Larger value
            b: Smaller value
            tolerance: Acceptable deviation from φ

        Returns:
            True if a/b ≈ φ
        """
        if b == 0:
            return False
        ratio = a / b
        return abs(ratio - PHI) < tolerance


class GoldenRectangle:
    """Golden rectangle calculations."""

    @staticmethod
    def from_width(width: float) -> Dict[str, float]:
        """
        Calculate golden rectangle dimensions from width.

        Returns dictionary with width, height, and area.
        """
        height = width / PHI
        return {
            'width': width,
            'height': round(height, 4),
            'area': round(width * height, 4),
            'ratio': PHI
        }

    @staticmethod
    def from_height(height: float) -> Dict[str, float]:
        """Calculate golden rectangle dimensions from height."""
        width = height * PHI
        return {
            'width': round(width, 4),
            'height': height,
            'area': round(width * height, 4),
            'ratio': PHI
        }

    @staticmethod
    def subdivide(width: float, height: float, n: int = 5) -> List[Dict[str, float]]:
        """
        Recursively subdivide a golden rectangle.

        Returns list of squares and remaining rectangles.
        """
        subdivisions = []
        w, h = width, height

        for i in range(n):
            if w > h:
                # Remove square from left
                subdivisions.append({
                    'type': 'square',
                    'side': h,
                    'iteration': i
                })
                w = w - h
            else:
                # Remove square from bottom
                subdivisions.append({
                    'type': 'square',
                    'side': w,
                    'iteration': i
                })
                h = h - w

        return subdivisions


class Fibonacci:
    """Fibonacci sequence calculations."""

    @staticmethod
    def sequence(n: int) -> List[int]:
        """Generate first n Fibonacci numbers."""
        if n <= 0:
            return []
        if n == 1:
            return [1]

        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

    @staticmethod
    def nth(n: int) -> int:
        """Calculate nth Fibonacci number using iteration."""
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
        """
        Calculate nth Fibonacci number using Binet's formula.

        Note: Loses precision for n > ~70 due to floating-point.
        """
        return round((PHI**n - PSI**n) / math.sqrt(5))

    @staticmethod
    def ratio_convergence(n: int = 20) -> List[Tuple[int, float, float]]:
        """
        Show how Fibonacci ratios converge to φ.

        Returns list of (n, F(n+1)/F(n), error from φ).
        """
        fib = Fibonacci.sequence(n + 1)
        convergence = []
        for i in range(1, len(fib)):
            ratio = fib[i] / fib[i-1]
            error = abs(ratio - PHI)
            convergence.append((i, round(ratio, 10), error))
        return convergence


class DesignScale:
    """Golden ratio design scale generator."""

    @staticmethod
    def spacing_scale(base: float = 16, n_larger: int = 5, n_smaller: int = 3) -> Dict[str, float]:
        """
        Generate a spacing scale based on golden ratio.

        Args:
            base: Base unit size (default 16px)
            n_larger: Number of sizes larger than base
            n_smaller: Number of sizes smaller than base

        Returns:
            Dictionary of size names to values
        """
        sizes = {'base': base}

        for i in range(1, n_larger + 1):
            sizes[f'lg{i}'] = round(base * (PHI ** i), 2)

        for i in range(1, n_smaller + 1):
            sizes[f'sm{i}'] = round(base / (PHI ** i), 2)

        return sizes

    @staticmethod
    def type_scale(base: float = 16, levels: int = 6) -> Dict[str, float]:
        """
        Generate a typography scale based on golden ratio.

        Args:
            base: Base font size (default 16px)
            levels: Number of heading levels

        Returns:
            Dictionary of element names to font sizes
        """
        scale = {'body': base}

        for i in range(1, levels + 1):
            size = base * (PHI ** i)
            scale[f'h{levels - i + 1}'] = round(size, 2)

        scale['small'] = round(base / PHI, 2)
        scale['tiny'] = round(base / (PHI ** 2), 2)

        return scale

    @staticmethod
    def layout_divisions(total_width: float) -> Dict[str, float]:
        """
        Calculate golden ratio layout divisions.

        Returns main content and sidebar widths.
        """
        main = total_width * PHI / (1 + PHI)
        sidebar = total_width / (1 + PHI)

        return {
            'total': total_width,
            'main': round(main, 2),
            'sidebar': round(sidebar, 2),
            'main_percent': round(100 * PHI / (1 + PHI), 2),
            'sidebar_percent': round(100 / (1 + PHI), 2)
        }


class FibonacciTrading:
    """Fibonacci trading calculations."""

    RETRACEMENT_LEVELS = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    EXTENSION_LEVELS = [1.272, 1.618, 2.0, 2.618, 4.236]

    @staticmethod
    def retracements(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """
        Calculate Fibonacci retracement levels.

        Args:
            high: Swing high price
            low: Swing low price
            is_uptrend: True for uptrend, False for downtrend

        Returns:
            Dictionary of level percentages to prices
        """
        diff = high - low
        levels = {}

        for level in FibonacciTrading.RETRACEMENT_LEVELS:
            if is_uptrend:
                price = high - (diff * level)
            else:
                price = low + (diff * level)
            levels[f"{level*100:.1f}%"] = round(price, 4)

        return levels

    @staticmethod
    def extensions(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """Calculate Fibonacci extension levels."""
        diff = high - low
        levels = {}

        for level in FibonacciTrading.EXTENSION_LEVELS:
            if is_uptrend:
                price = low + (diff * level)
            else:
                price = high - (diff * level)
            levels[f"{level*100:.1f}%"] = round(price, 4)

        return levels

    @staticmethod
    def golden_pocket(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """Calculate the golden pocket zone (61.8% - 65%)."""
        diff = high - low

        if is_uptrend:
            upper = high - (diff * 0.618)
            lower = high - (diff * 0.65)
        else:
            lower = low + (diff * 0.618)
            upper = low + (diff * 0.65)

        return {
            'upper': round(upper, 4),
            'lower': round(lower, 4),
            'midpoint': round((upper + lower) / 2, 4)
        }


class Phyllotaxis:
    """Phyllotaxis pattern generation."""

    @staticmethod
    def sunflower_pattern(n_points: int, c: float = 2.0) -> List[Tuple[float, float]]:
        """
        Generate sunflower seed pattern points.

        Args:
            n_points: Number of points to generate
            c: Scaling constant

        Returns:
            List of (x, y) coordinates
        """
        points = []
        for i in range(n_points):
            r = c * math.sqrt(i)
            theta = i * GOLDEN_ANGLE
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((round(x, 4), round(y, 4)))
        return points

    @staticmethod
    def golden_spiral_points(n_points: int = 100, growth: float = PHI) -> List[Tuple[float, float]]:
        """
        Generate points along a golden spiral.

        Args:
            n_points: Number of points
            growth: Growth factor per full rotation

        Returns:
            List of (x, y) coordinates
        """
        points = []
        for i in range(n_points):
            angle = i * 0.1
            r = growth ** (angle / (2 * math.pi))
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append((round(x, 4), round(y, 4)))
        return points


class GoldenHash:
    """Golden ratio based hashing utilities."""

    INV_PHI = (math.sqrt(5) - 1) / 2  # ~0.618

    @staticmethod
    def hash(key: int, table_size: int) -> int:
        """
        Hash using golden ratio multiplication method.

        Provides excellent distribution for sequential keys.
        """
        fractional = (key * GoldenHash.INV_PHI) % 1
        return int(table_size * fractional)

    @staticmethod
    def weyl_sequence(n: int, seed: float = 0.5) -> List[float]:
        """
        Generate quasi-random numbers using golden ratio.

        Returns well-distributed sequence in [0, 1).
        """
        sequence = []
        state = seed
        for _ in range(n):
            state = (state + GoldenHash.INV_PHI) % 1
            sequence.append(round(state, 6))
        return sequence


def demo():
    """Demonstrate calculator functionality."""
    print("=" * 60)
    print("GOLDEN RATIO CALCULATOR DEMO")
    print("=" * 60)

    print(f"\n📐 φ = {PHI}")
    print(f"📐 1/φ = {1/PHI}")
    print(f"📐 φ² = {PHI**2}")

    print("\n" + "-" * 40)
    print("GOLDEN RECTANGLE (width=1920)")
    print("-" * 40)
    rect = GoldenRectangle.from_width(1920)
    for k, v in rect.items():
        print(f"  {k}: {v}")

    print("\n" + "-" * 40)
    print("FIBONACCI SEQUENCE (first 15)")
    print("-" * 40)
    fib = Fibonacci.sequence(15)
    print(f"  {fib}")

    print("\n" + "-" * 40)
    print("DESIGN SPACING SCALE (base=16)")
    print("-" * 40)
    scale = DesignScale.spacing_scale(16)
    for k, v in sorted(scale.items()):
        print(f"  {k}: {v}px")

    print("\n" + "-" * 40)
    print("TYPOGRAPHY SCALE (base=16)")
    print("-" * 40)
    type_scale = DesignScale.type_scale(16)
    for k, v in type_scale.items():
        print(f"  {k}: {v}px")

    print("\n" + "-" * 40)
    print("FIBONACCI RETRACEMENTS (high=200, low=100)")
    print("-" * 40)
    retracements = FibonacciTrading.retracements(200, 100)
    for level, price in retracements.items():
        print(f"  {level}: ${price}")

    print("\n" + "-" * 40)
    print("GOLDEN POCKET")
    print("-" * 40)
    pocket = FibonacciTrading.golden_pocket(200, 100)
    for k, v in pocket.items():
        print(f"  {k}: ${v}")

    print("\n" + "-" * 40)
    print("LAYOUT DIVISIONS (width=1200)")
    print("-" * 40)
    layout = DesignScale.layout_divisions(1200)
    for k, v in layout.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    demo()
