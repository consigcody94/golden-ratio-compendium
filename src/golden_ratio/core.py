"""
Core golden ratio calculations and utilities.
"""

from typing import Dict, List

from golden_ratio.constants import PHI


class GoldenRatio:
    """Golden ratio calculations and utilities."""

    @staticmethod
    def phi() -> float:
        """Return the golden ratio phi.

        Returns:
            The golden ratio (approximately 1.618033988749895).
        """
        return PHI

    @staticmethod
    def inverse_phi() -> float:
        """Return 1/phi (also equals phi - 1).

        Returns:
            The inverse of phi (approximately 0.618033988749895).
        """
        return 1 / PHI

    @staticmethod
    def phi_power(n: int) -> float:
        """Return phi raised to the power n.

        Args:
            n: The exponent.

        Returns:
            phi^n.
        """
        return PHI**n

    @staticmethod
    def is_golden_ratio(a: float, b: float, tolerance: float = 0.01) -> bool:
        """Check if two values are in golden ratio.

        Args:
            a: Larger value.
            b: Smaller value.
            tolerance: Acceptable deviation from phi.

        Returns:
            True if a/b is approximately equal to phi.
        """
        if b == 0:
            return False
        ratio = a / b
        return abs(ratio - PHI) < tolerance


class GoldenRectangle:
    """Golden rectangle calculations."""

    @staticmethod
    def from_width(width: float) -> Dict[str, float]:
        """Calculate golden rectangle dimensions from width.

        Args:
            width: The width of the rectangle.

        Returns:
            Dictionary with width, height, area, and ratio.
        """
        height = width / PHI
        return {
            "width": width,
            "height": round(height, 4),
            "area": round(width * height, 4),
            "ratio": PHI,
        }

    @staticmethod
    def from_height(height: float) -> Dict[str, float]:
        """Calculate golden rectangle dimensions from height.

        Args:
            height: The height of the rectangle.

        Returns:
            Dictionary with width, height, area, and ratio.
        """
        width = height * PHI
        return {
            "width": round(width, 4),
            "height": height,
            "area": round(width * height, 4),
            "ratio": PHI,
        }

    @staticmethod
    def subdivide(width: float, height: float, n: int = 5) -> List[Dict[str, float]]:
        """Recursively subdivide a golden rectangle.

        This method demonstrates how a golden rectangle can be subdivided
        into squares and smaller golden rectangles, which forms the basis
        of the golden spiral.

        Args:
            width: Rectangle width.
            height: Rectangle height.
            n: Number of subdivisions.

        Returns:
            List of squares with their properties.
        """
        subdivisions = []
        w, h = width, height

        for i in range(n):
            if w > h:
                subdivisions.append({"type": "square", "side": h, "iteration": i})
                w = w - h
            else:
                subdivisions.append({"type": "square", "side": w, "iteration": i})
                h = h - w

        return subdivisions
