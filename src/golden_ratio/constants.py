"""
Mathematical constants related to the golden ratio.
"""

import math

# The golden ratio: phi = (1 + sqrt(5)) / 2
PHI: float = (1 + math.sqrt(5)) / 2  # 1.6180339887498948482...

# The conjugate of phi: psi = (1 - sqrt(5)) / 2
PSI: float = (1 - math.sqrt(5)) / 2  # -0.6180339887498948482...

# The golden angle in radians (~137.5 degrees)
GOLDEN_ANGLE: float = math.pi * (3 - math.sqrt(5))  # ~2.399963 rad

# The golden angle in degrees
GOLDEN_ANGLE_DEGREES: float = 360 / (PHI**2)  # ~137.5077 degrees

# Inverse of phi (also equals phi - 1)
INV_PHI: float = (math.sqrt(5) - 1) / 2  # ~0.618
