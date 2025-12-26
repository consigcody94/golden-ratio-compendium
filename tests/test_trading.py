"""Tests for Fibonacci trading functions."""

import pytest

from golden_ratio.trading import FibonacciTrading


class TestFibonacciTrading:
    """Test FibonacciTrading class."""

    def test_retracement_levels_exist(self):
        """Test that all retracement levels are present."""
        levels = FibonacciTrading.retracements(200, 100)
        expected_keys = ["0.0%", "23.6%", "38.2%", "50.0%", "61.8%", "78.6%", "100.0%"]
        for key in expected_keys:
            assert key in levels

    def test_retracement_uptrend(self):
        """Test retracement levels for uptrend."""
        levels = FibonacciTrading.retracements(200, 100, is_uptrend=True)
        # 0% should be at high
        assert levels["0.0%"] == 200
        # 100% should be at low
        assert levels["100.0%"] == 100
        # 50% should be midpoint
        assert levels["50.0%"] == 150

    def test_retracement_downtrend(self):
        """Test retracement levels for downtrend."""
        levels = FibonacciTrading.retracements(200, 100, is_uptrend=False)
        # 0% should be at low
        assert levels["0.0%"] == 100
        # 100% should be at high
        assert levels["100.0%"] == 200

    def test_retracement_618(self):
        """Test 61.8% retracement level."""
        levels = FibonacciTrading.retracements(200, 100, is_uptrend=True)
        # 61.8% retracement: 200 - (100 * 0.618) = 138.2
        assert abs(levels["61.8%"] - 138.2) < 0.01

    def test_extension_levels_exist(self):
        """Test that all extension levels are present."""
        levels = FibonacciTrading.extensions(200, 100)
        expected_keys = ["127.2%", "161.8%", "200.0%", "261.8%", "423.6%"]
        for key in expected_keys:
            assert key in levels

    def test_extension_uptrend(self):
        """Test extension levels for uptrend."""
        levels = FibonacciTrading.extensions(200, 100, is_uptrend=True)
        # 161.8% extension: 100 + (100 * 1.618) = 261.8
        assert abs(levels["161.8%"] - 261.8) < 0.01

    def test_extension_downtrend(self):
        """Test extension levels for downtrend."""
        levels = FibonacciTrading.extensions(200, 100, is_uptrend=False)
        # 161.8% extension downward: 200 - (100 * 1.618) = 38.2
        assert abs(levels["161.8%"] - 38.2) < 0.01

    def test_golden_pocket_uptrend(self):
        """Test golden pocket for uptrend."""
        pocket = FibonacciTrading.golden_pocket(200, 100, is_uptrend=True)
        assert "upper" in pocket
        assert "lower" in pocket
        assert "midpoint" in pocket
        # Upper should be 61.8%: 200 - 61.8 = 138.2
        assert abs(pocket["upper"] - 138.2) < 0.01
        # Lower should be 65%: 200 - 65 = 135
        assert abs(pocket["lower"] - 135) < 0.01

    def test_golden_pocket_downtrend(self):
        """Test golden pocket for downtrend."""
        pocket = FibonacciTrading.golden_pocket(200, 100, is_uptrend=False)
        # Lower should be at 61.8%: 100 + 61.8 = 161.8
        assert abs(pocket["lower"] - 161.8) < 0.01
        # Upper should be at 65%: 100 + 65 = 165
        assert abs(pocket["upper"] - 165) < 0.01

    def test_golden_pocket_midpoint(self):
        """Test golden pocket midpoint calculation."""
        pocket = FibonacciTrading.golden_pocket(200, 100)
        expected_midpoint = (pocket["upper"] + pocket["lower"]) / 2
        assert abs(pocket["midpoint"] - expected_midpoint) < 0.01

    def test_all_levels(self):
        """Test all_levels returns all categories."""
        result = FibonacciTrading.all_levels(200, 100)
        assert "retracements" in result
        assert "extensions" in result
        assert "golden_pocket" in result

    def test_all_levels_consistency(self):
        """Test that all_levels matches individual methods."""
        all_levels = FibonacciTrading.all_levels(200, 100, is_uptrend=True)

        retracements = FibonacciTrading.retracements(200, 100, is_uptrend=True)
        extensions = FibonacciTrading.extensions(200, 100, is_uptrend=True)
        golden_pocket = FibonacciTrading.golden_pocket(200, 100, is_uptrend=True)

        assert all_levels["retracements"] == retracements
        assert all_levels["extensions"] == extensions
        assert all_levels["golden_pocket"] == golden_pocket
