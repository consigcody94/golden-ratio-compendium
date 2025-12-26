"""Tests for golden ratio constants."""

import math
import pytest

from golden_ratio.constants import PHI, PSI, GOLDEN_ANGLE, GOLDEN_ANGLE_DEGREES, INV_PHI


class TestConstants:
    """Test mathematical constants."""

    def test_phi_value(self):
        """Test that PHI is correctly calculated."""
        expected = (1 + math.sqrt(5)) / 2
        assert abs(PHI - expected) < 1e-15

    def test_psi_value(self):
        """Test that PSI is correctly calculated."""
        expected = (1 - math.sqrt(5)) / 2
        assert abs(PSI - expected) < 1e-15

    def test_phi_squared_property(self):
        """Test that φ² = φ + 1."""
        assert abs(PHI * PHI - PHI - 1) < 1e-10

    def test_inverse_phi_property(self):
        """Test that 1/φ = φ - 1."""
        assert abs(1 / PHI - (PHI - 1)) < 1e-10

    def test_phi_psi_relationship(self):
        """Test that φ + ψ = 1."""
        assert abs(PHI + PSI - 1) < 1e-10

    def test_phi_psi_product(self):
        """Test that φ * ψ = -1."""
        assert abs(PHI * PSI + 1) < 1e-10

    def test_golden_angle_degrees(self):
        """Test golden angle in degrees is approximately 137.5."""
        assert abs(GOLDEN_ANGLE_DEGREES - 137.5077) < 0.01

    def test_golden_angle_radians(self):
        """Test golden angle in radians."""
        expected_rad = math.radians(GOLDEN_ANGLE_DEGREES)
        assert abs(GOLDEN_ANGLE - expected_rad) < 0.01

    def test_inv_phi(self):
        """Test inverse phi equals 1/PHI."""
        assert abs(INV_PHI - 1 / PHI) < 1e-10
