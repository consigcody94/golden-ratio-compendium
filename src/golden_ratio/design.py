"""
Golden ratio design scale utilities.

Generate typography scales, spacing systems, and layout proportions
based on the golden ratio for harmonious design.
"""

from typing import Dict

from golden_ratio.constants import PHI


class DesignScale:
    """Golden ratio design scale generator."""

    @staticmethod
    def spacing_scale(
        base: float = 16, n_larger: int = 5, n_smaller: int = 3
    ) -> Dict[str, float]:
        """Generate a spacing scale based on the golden ratio.

        Args:
            base: Base unit size (default 16px).
            n_larger: Number of sizes larger than base.
            n_smaller: Number of sizes smaller than base.

        Returns:
            Dictionary mapping size names to values.

        Example:
            >>> scale = DesignScale.spacing_scale(16)
            >>> print(scale['lg1'])  # 25.89
            >>> print(scale['sm1'])  # 9.89
        """
        sizes = {"base": base}

        for i in range(1, n_larger + 1):
            sizes[f"lg{i}"] = round(base * (PHI**i), 2)

        for i in range(1, n_smaller + 1):
            sizes[f"sm{i}"] = round(base / (PHI**i), 2)

        return sizes

    @staticmethod
    def type_scale(base: float = 16, levels: int = 6) -> Dict[str, float]:
        """Generate a typography scale based on the golden ratio.

        Args:
            base: Base font size (default 16px).
            levels: Number of heading levels.

        Returns:
            Dictionary mapping element names to font sizes.

        Example:
            >>> scale = DesignScale.type_scale(16)
            >>> print(scale['h1'])  # ~67.77
            >>> print(scale['body'])  # 16
        """
        scale = {"body": base}

        for i in range(1, levels + 1):
            size = base * (PHI**i)
            scale[f"h{levels - i + 1}"] = round(size, 2)

        scale["small"] = round(base / PHI, 2)
        scale["tiny"] = round(base / (PHI**2), 2)

        return scale

    @staticmethod
    def layout_divisions(total_width: float) -> Dict[str, float]:
        """Calculate golden ratio layout divisions.

        Divides a total width into main content and sidebar using
        the golden ratio. The main content receives the larger portion.

        Args:
            total_width: Total available width.

        Returns:
            Dictionary with layout dimensions and percentages.

        Example:
            >>> layout = DesignScale.layout_divisions(1200)
            >>> print(layout['main'])  # ~741.64
            >>> print(layout['sidebar'])  # ~458.36
        """
        main = total_width * PHI / (1 + PHI)
        sidebar = total_width / (1 + PHI)

        return {
            "total": total_width,
            "main": round(main, 2),
            "sidebar": round(sidebar, 2),
            "main_percent": round(100 * PHI / (1 + PHI), 2),
            "sidebar_percent": round(100 / (1 + PHI), 2),
        }

    @staticmethod
    def line_height(font_size: float, line_width: int = 65) -> float:
        """Calculate optimal line height using golden ratio principles.

        Based on Robert Bringhurst's recommendations, adjusted for
        golden ratio proportions.

        Args:
            font_size: Font size in pixels.
            line_width: Line width in characters (default 65).

        Returns:
            Recommended line height in pixels.
        """
        base_line_height = font_size * PHI
        width_adjustment = (line_width - 45) / 100
        return round(base_line_height * (1 + width_adjustment), 2)

    @staticmethod
    def modular_scale(base: float, ratio: float = PHI, steps: int = 10) -> Dict[int, float]:
        """Generate a modular scale with custom ratio.

        Args:
            base: Base value.
            ratio: Scale ratio (default PHI).
            steps: Number of steps above and below base.

        Returns:
            Dictionary mapping step numbers to values.
        """
        scale = {}
        for i in range(-steps, steps + 1):
            scale[i] = round(base * (ratio**i), 2)
        return scale
