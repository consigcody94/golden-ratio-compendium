"""Tests for core golden ratio functions."""

import pytest

from golden_ratio.constants import PHI
from golden_ratio.core import GoldenRatio, GoldenRectangle


class TestGoldenRatio:
    """Test GoldenRatio class."""

    def test_phi(self):
        """Test phi() returns correct value."""
        assert abs(GoldenRatio.phi() - PHI) < 1e-15

    def test_inverse_phi(self):
        """Test inverse_phi() returns 1/PHI."""
        assert abs(GoldenRatio.inverse_phi() - 1 / PHI) < 1e-10

    def test_phi_power_positive(self):
        """Test phi_power with positive exponent."""
        assert abs(GoldenRatio.phi_power(2) - PHI * PHI) < 1e-10
        assert abs(GoldenRatio.phi_power(3) - PHI ** 3) < 1e-10

    def test_phi_power_negative(self):
        """Test phi_power with negative exponent."""
        assert abs(GoldenRatio.phi_power(-1) - 1 / PHI) < 1e-10
        assert abs(GoldenRatio.phi_power(-2) - 1 / (PHI * PHI)) < 1e-10

    def test_phi_power_zero(self):
        """Test phi_power with zero exponent."""
        assert GoldenRatio.phi_power(0) == 1.0

    def test_is_golden_ratio_true(self):
        """Test is_golden_ratio with values in golden ratio."""
        a = 161.8
        b = 100.0
        assert GoldenRatio.is_golden_ratio(a, b, tolerance=0.01)

    def test_is_golden_ratio_false(self):
        """Test is_golden_ratio with values not in golden ratio."""
        a = 200.0
        b = 100.0
        assert not GoldenRatio.is_golden_ratio(a, b, tolerance=0.01)

    def test_is_golden_ratio_zero_denominator(self):
        """Test is_golden_ratio with zero denominator."""
        assert not GoldenRatio.is_golden_ratio(100, 0)


class TestGoldenRectangle:
    """Test GoldenRectangle class."""

    def test_from_width(self):
        """Test creating rectangle from width."""
        result = GoldenRectangle.from_width(1618)
        assert result["width"] == 1618
        assert abs(result["height"] - 1000) < 1
        assert result["ratio"] == PHI

    def test_from_height(self):
        """Test creating rectangle from height."""
        result = GoldenRectangle.from_height(1000)
        assert result["height"] == 1000
        assert abs(result["width"] - 1618) < 1
        assert result["ratio"] == PHI

    def test_area_calculation(self):
        """Test area is correctly calculated."""
        result = GoldenRectangle.from_width(100)
        expected_area = 100 * (100 / PHI)
        assert abs(result["area"] - expected_area) < 0.01

    def test_subdivide(self):
        """Test golden rectangle subdivision."""
        width = 1618
        height = 1000
        subdivisions = GoldenRectangle.subdivide(width, height, 5)

        assert len(subdivisions) == 5
        for sub in subdivisions:
            assert sub["type"] == "square"
            assert "side" in sub
            assert "iteration" in sub

    def test_subdivide_iterations(self):
        """Test subdivision iteration numbers."""
        subdivisions = GoldenRectangle.subdivide(100, 61.8, 3)
        for i, sub in enumerate(subdivisions):
            assert sub["iteration"] == i
