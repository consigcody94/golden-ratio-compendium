"""
Phyllotaxis pattern generation.

Generate natural patterns based on the golden angle, including
sunflower seed arrangements and golden spirals.
"""

import math
from typing import List, Tuple

from golden_ratio.constants import GOLDEN_ANGLE, PHI


class Phyllotaxis:
    """Phyllotaxis (plant growth pattern) generation."""

    @staticmethod
    def sunflower_pattern(n_points: int, c: float = 2.0) -> List[Tuple[float, float]]:
        """Generate sunflower seed pattern points.

        Uses the Vogel model to create a sunflower-like spiral pattern
        where each successive point is rotated by the golden angle.

        Args:
            n_points: Number of points to generate.
            c: Scaling constant controlling spacing.

        Returns:
            List of (x, y) coordinate tuples.

        Example:
            >>> points = Phyllotaxis.sunflower_pattern(100)
            >>> # Plot points to see the sunflower pattern
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
    def golden_spiral_points(
        n_points: int = 100, growth: float = PHI
    ) -> List[Tuple[float, float]]:
        """Generate points along a golden spiral.

        The golden spiral is a logarithmic spiral that grows by a factor
        of phi for every quarter turn (90 degrees).

        Args:
            n_points: Number of points to generate.
            growth: Growth factor per full rotation (default phi).

        Returns:
            List of (x, y) coordinate tuples.
        """
        points = []
        for i in range(n_points):
            angle = i * 0.1
            r = growth ** (angle / (2 * math.pi))
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append((round(x, 4), round(y, 4)))
        return points

    @staticmethod
    def fermat_spiral(n_points: int, scale: float = 1.0) -> List[Tuple[float, float]]:
        """Generate a Fermat spiral pattern.

        The Fermat spiral is a parabolic spiral where r^2 = a^2 * theta.
        Combined with the golden angle, it produces optimal packing.

        Args:
            n_points: Number of points.
            scale: Scale factor.

        Returns:
            List of (x, y) coordinate tuples.
        """
        points = []
        for i in range(n_points):
            theta = i * GOLDEN_ANGLE
            r = scale * math.sqrt(theta)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((round(x, 4), round(y, 4)))
        return points

    @staticmethod
    def daisy_pattern(n_florets: int, inner_radius: float = 1.0) -> List[Tuple[float, float]]:
        """Generate a daisy-like flower pattern.

        Creates a pattern similar to the arrangement of florets
        in a daisy or sunflower head.

        Args:
            n_florets: Number of florets to generate.
            inner_radius: Radius of the innermost floret.

        Returns:
            List of (x, y) coordinate tuples.
        """
        points = []
        for i in range(1, n_florets + 1):
            theta = i * GOLDEN_ANGLE
            r = inner_radius * math.sqrt(i)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((round(x, 4), round(y, 4)))
        return points
