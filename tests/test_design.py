"""Tests for design scale functions."""

import pytest

from golden_ratio.constants import PHI
from golden_ratio.design import DesignScale


class TestDesignScale:
    """Test DesignScale class."""

    def test_spacing_scale_default(self):
        """Test default spacing scale."""
        scale = DesignScale.spacing_scale()
        assert scale["base"] == 16
        assert "lg1" in scale
        assert "sm1" in scale

    def test_spacing_scale_custom_base(self):
        """Test spacing scale with custom base."""
        scale = DesignScale.spacing_scale(base=8)
        assert scale["base"] == 8

    def test_spacing_scale_golden_ratio(self):
        """Test that spacing follows golden ratio."""
        scale = DesignScale.spacing_scale(base=16)
        assert abs(scale["lg1"] - 16 * PHI) < 0.01
        assert abs(scale["sm1"] - 16 / PHI) < 0.01

    def test_spacing_scale_levels(self):
        """Test number of levels in spacing scale."""
        scale = DesignScale.spacing_scale(n_larger=3, n_smaller=2)
        larger_keys = [k for k in scale if k.startswith("lg")]
        smaller_keys = [k for k in scale if k.startswith("sm")]
        assert len(larger_keys) == 3
        assert len(smaller_keys) == 2

    def test_type_scale_default(self):
        """Test default type scale."""
        scale = DesignScale.type_scale()
        assert scale["body"] == 16
        assert "h1" in scale
        assert "small" in scale
        assert "tiny" in scale

    def test_type_scale_headings(self):
        """Test type scale heading levels."""
        scale = DesignScale.type_scale(levels=6)
        for i in range(1, 7):
            assert f"h{i}" in scale

    def test_type_scale_ascending(self):
        """Test that heading sizes are ascending h6 to h1."""
        scale = DesignScale.type_scale(levels=6)
        sizes = [scale[f"h{i}"] for i in range(6, 0, -1)]
        for i in range(len(sizes) - 1):
            assert sizes[i] < sizes[i + 1]

    def test_layout_divisions(self):
        """Test layout divisions."""
        layout = DesignScale.layout_divisions(1000)
        assert layout["total"] == 1000
        assert abs(layout["main"] + layout["sidebar"] - 1000) < 0.01

    def test_layout_golden_ratio(self):
        """Test that layout follows golden ratio."""
        layout = DesignScale.layout_divisions(1000)
        ratio = layout["main"] / layout["sidebar"]
        assert abs(ratio - PHI) < 0.01

    def test_layout_percentages(self):
        """Test layout percentages sum to 100."""
        layout = DesignScale.layout_divisions(1200)
        total_percent = layout["main_percent"] + layout["sidebar_percent"]
        assert abs(total_percent - 100) < 0.01

    def test_line_height(self):
        """Test line height calculation."""
        lh = DesignScale.line_height(16)
        # Should be approximately 16 * PHI adjusted for line width
        assert lh > 16 * PHI * 0.9
        assert lh < 16 * PHI * 1.3

    def test_line_height_scales_with_font(self):
        """Test that line height scales with font size."""
        lh_16 = DesignScale.line_height(16)
        lh_20 = DesignScale.line_height(20)
        assert lh_20 > lh_16

    def test_modular_scale(self):
        """Test modular scale generation."""
        scale = DesignScale.modular_scale(16, PHI, steps=3)
        assert 0 in scale
        assert scale[0] == 16
        assert scale[1] > scale[0]
        assert scale[-1] < scale[0]

    def test_modular_scale_symmetry(self):
        """Test modular scale has equal positive and negative steps."""
        scale = DesignScale.modular_scale(10, PHI, steps=5)
        positive = [k for k in scale.keys() if k > 0]
        negative = [k for k in scale.keys() if k < 0]
        assert len(positive) == len(negative)
