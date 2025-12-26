"""
Fibonacci trading calculations.

Provides tools for calculating Fibonacci retracement and extension levels
commonly used in technical analysis of financial markets.
"""

from typing import Dict, List


class FibonacciTrading:
    """Fibonacci trading calculations for technical analysis."""

    RETRACEMENT_LEVELS: List[float] = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    EXTENSION_LEVELS: List[float] = [1.272, 1.618, 2.0, 2.618, 4.236]

    @staticmethod
    def retracements(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """Calculate Fibonacci retracement levels.

        Retracement levels are horizontal lines indicating where support
        and resistance are likely to occur during a price pullback.

        Args:
            high: Swing high price.
            low: Swing low price.
            is_uptrend: True for uptrend (retracing down from high),
                       False for downtrend (retracing up from low).

        Returns:
            Dictionary mapping level percentages to price levels.

        Example:
            >>> levels = FibonacciTrading.retracements(200, 100, is_uptrend=True)
            >>> print(levels['61.8%'])  # 138.2 (key support level)
        """
        diff = high - low
        levels = {}

        for level in FibonacciTrading.RETRACEMENT_LEVELS:
            if is_uptrend:
                price = high - (diff * level)
            else:
                price = low + (diff * level)
            levels[f"{level * 100:.1f}%"] = round(price, 4)

        return levels

    @staticmethod
    def extensions(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """Calculate Fibonacci extension levels.

        Extension levels are used to project potential price targets
        beyond the original move.

        Args:
            high: Swing high price.
            low: Swing low price.
            is_uptrend: True for uptrend, False for downtrend.

        Returns:
            Dictionary mapping extension percentages to price levels.

        Example:
            >>> levels = FibonacciTrading.extensions(200, 100, is_uptrend=True)
            >>> print(levels['161.8%'])  # 261.8 (common target)
        """
        diff = high - low
        levels = {}

        for level in FibonacciTrading.EXTENSION_LEVELS:
            if is_uptrend:
                price = low + (diff * level)
            else:
                price = high - (diff * level)
            levels[f"{level * 100:.1f}%"] = round(price, 4)

        return levels

    @staticmethod
    def golden_pocket(high: float, low: float, is_uptrend: bool = True) -> Dict[str, float]:
        """Calculate the golden pocket zone (61.8% - 65%).

        The golden pocket is a high-probability reversal zone where
        the 61.8% and 65% retracement levels converge.

        Args:
            high: Swing high price.
            low: Swing low price.
            is_uptrend: True for uptrend, False for downtrend.

        Returns:
            Dictionary with upper, lower, and midpoint of golden pocket.
        """
        diff = high - low

        if is_uptrend:
            upper = high - (diff * 0.618)
            lower = high - (diff * 0.65)
        else:
            lower = low + (diff * 0.618)
            upper = low + (diff * 0.65)

        return {
            "upper": round(upper, 4),
            "lower": round(lower, 4),
            "midpoint": round((upper + lower) / 2, 4),
        }

    @staticmethod
    def all_levels(high: float, low: float, is_uptrend: bool = True) -> Dict[str, Dict[str, float]]:
        """Calculate all Fibonacci levels at once.

        Args:
            high: Swing high price.
            low: Swing low price.
            is_uptrend: True for uptrend, False for downtrend.

        Returns:
            Dictionary containing retracements, extensions, and golden pocket.
        """
        return {
            "retracements": FibonacciTrading.retracements(high, low, is_uptrend),
            "extensions": FibonacciTrading.extensions(high, low, is_uptrend),
            "golden_pocket": FibonacciTrading.golden_pocket(high, low, is_uptrend),
        }
