# Real-World Golden Ratio Applications

Practical examples and code snippets for applying the golden ratio in various domains.

---

## Web Design

### CSS Golden Layout

```css
/* Golden ratio two-column layout */
.golden-container {
  display: flex;
  gap: 1rem;
}

.main-content {
  flex: 1.618; /* φ */
}

.sidebar {
  flex: 1;
}

/* Alternative using percentages */
.main-content-pct { width: 61.8%; }
.sidebar-pct { width: 38.2%; }
```

### CSS Grid with Golden Proportions

```css
.golden-grid {
  display: grid;
  grid-template-columns: 1fr 1.618fr;
  grid-template-rows: 1fr 1.618fr;
  gap: 1rem;
}

/* Named areas */
.golden-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main";
  grid-template-columns: 1fr 1.618fr;
  grid-template-rows: auto 1fr;
}
```

### Responsive Golden Breakpoints

```scss
// Golden ratio breakpoints
$phi: 1.618;
$base-width: 320px;

$breakpoints: (
  'sm': $base-width * $phi,        // 518px
  'md': $base-width * ($phi * $phi), // 838px
  'lg': $base-width * ($phi * $phi * $phi), // 1356px
);
```

---

## Typography

### Golden Type Scale

```javascript
// Generate type scale
const phi = 1.618;
const baseSize = 16;

const typeScale = {
  tiny: baseSize / phi / phi,   // 6.1px
  small: baseSize / phi,        // 9.9px
  body: baseSize,               // 16px
  h4: baseSize * phi,           // 25.9px
  h3: baseSize * phi * phi,     // 41.9px
  h2: baseSize * phi ** 3,      // 67.8px
  h1: baseSize * phi ** 4,      // 109.7px
};
```

### Line Height and Measure

```css
:root {
  --phi: 1.618;
  --base-font: 16px;

  /* Golden line height */
  --line-height: calc(var(--base-font) * var(--phi)); /* 25.9px */

  /* Optimal line length (45-75 characters) */
  --measure: 65ch;
}

body {
  font-size: var(--base-font);
  line-height: var(--phi);
}

p {
  max-width: var(--measure);
}
```

---

## UI Components

### Button Sizing

```javascript
const phi = 1.618;
const baseHeight = 40;

const buttonSizes = {
  sm: baseHeight / phi,      // 24.7px
  md: baseHeight,            // 40px
  lg: baseHeight * phi,      // 64.7px
  xl: baseHeight * phi ** 2, // 104.7px
};

// Horizontal padding
const paddingRatio = phi;
const buttonPadding = {
  sm: { x: 16, y: 8 },        // 16/8 ≈ 2 (close to φ)
  md: { x: 24, y: 12 },
  lg: { x: 32, y: 16 },
};
```

### Card Proportions

```css
.golden-card {
  aspect-ratio: 1.618 / 1;
  padding: calc(1rem * 0.618) 1rem;
}

.golden-card--vertical {
  aspect-ratio: 1 / 1.618;
}
```

### Icon Grid

```css
.icon-grid {
  /* Icons at golden ratio sizes */
  --icon-sm: 16px;
  --icon-md: 26px;  /* 16 × φ */
  --icon-lg: 42px;  /* 26 × φ */
  --icon-xl: 68px;  /* 42 × φ */
}
```

---

## Photography / Image Processing

### Golden Crop in Python

```python
from PIL import Image

def golden_crop(image_path, orientation='horizontal'):
    """Crop image to golden rectangle proportions."""
    img = Image.open(image_path)
    width, height = img.size
    phi = 1.618

    if orientation == 'horizontal':
        new_height = width / phi
        if new_height <= height:
            # Crop vertically
            top = (height - new_height) / 2
            box = (0, top, width, top + new_height)
        else:
            # Crop horizontally
            new_width = height * phi
            left = (width - new_width) / 2
            box = (left, 0, left + new_width, height)
    else:
        new_width = height / phi
        if new_width <= width:
            left = (width - new_width) / 2
            box = (left, 0, left + new_width, height)
        else:
            new_height = width * phi
            top = (height - new_height) / 2
            box = (0, top, width, top + new_height)

    return img.crop(box)
```

### Golden Spiral Overlay

```python
import matplotlib.pyplot as plt
import numpy as np

def create_golden_overlay(width, height):
    """Create golden spiral overlay for image composition."""
    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)

    phi = (1 + np.sqrt(5)) / 2

    # Generate spiral
    theta = np.linspace(0, 4 * np.pi, 1000)
    r = phi ** (theta / (2 * np.pi))

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Scale to fit image
    scale = min(width, height) / (2 * max(r))
    x = x * scale + width / 2
    y = y * scale + height / 2

    ax.plot(x, y, 'r-', linewidth=2, alpha=0.7)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')

    return fig
```

---

## Financial Trading

### Fibonacci Retracement Strategy

```python
def analyze_retracement(high, low, current_price, trend='up'):
    """Analyze price position relative to Fibonacci levels."""
    levels = {
        '0.0%': 0.0,
        '23.6%': 0.236,
        '38.2%': 0.382,
        '50.0%': 0.500,
        '61.8%': 0.618,
        '78.6%': 0.786,
        '100.0%': 1.0
    }

    diff = high - low

    analysis = {
        'levels': {},
        'nearest_support': None,
        'nearest_resistance': None,
        'in_golden_pocket': False
    }

    if trend == 'up':
        for name, pct in levels.items():
            price = high - diff * pct
            analysis['levels'][name] = round(price, 4)

            if price < current_price and (analysis['nearest_support'] is None or
                    price > analysis['levels'][analysis['nearest_support']]):
                analysis['nearest_support'] = name

            if price > current_price and (analysis['nearest_resistance'] is None or
                    price < analysis['levels'][analysis['nearest_resistance']]):
                analysis['nearest_resistance'] = name

        # Check golden pocket (61.8% - 65%)
        pocket_upper = high - diff * 0.618
        pocket_lower = high - diff * 0.65
        analysis['in_golden_pocket'] = pocket_lower <= current_price <= pocket_upper

    return analysis


# Example usage
result = analyze_retracement(
    high=200,
    low=100,
    current_price=140,
    trend='up'
)
print(f"Levels: {result['levels']}")
print(f"Nearest support: {result['nearest_support']}")
print(f"In golden pocket: {result['in_golden_pocket']}")
```

---

## Room Acoustics

### Golden Ratio Room Calculator

```python
def ideal_room_dimensions(height):
    """
    Calculate ideal room dimensions using golden ratio.

    Returns (height, width, length) in the ratio 1 : φ : φ²
    """
    phi = 1.618

    return {
        'height': height,
        'width': round(height * phi, 2),
        'length': round(height * phi ** 2, 2),
        'ratio': f"1 : {phi:.3f} : {phi**2:.3f}",
        'volume': round(height * (height * phi) * (height * phi ** 2), 2)
    }


# Example: 3 meter ceiling height
room = ideal_room_dimensions(3.0)
print(f"Height: {room['height']}m")
print(f"Width: {room['width']}m")
print(f"Length: {room['length']}m")
print(f"Ratio: {room['ratio']}")
```

### Speaker Placement

```python
def speaker_placement(room_length, room_width):
    """Calculate speaker positions using golden ratio."""
    phi = 1.618

    # Speaker distance from front wall
    distance_from_front = room_length / (phi ** 2)

    # Speaker distance from side walls
    distance_from_side = room_width / (phi ** 2)

    # Listening position
    listening_distance = room_length / phi

    return {
        'speaker_from_front': round(distance_from_front, 2),
        'speaker_from_side': round(distance_from_side, 2),
        'listening_position': round(listening_distance, 2),
        'speaker_separation': round(room_width - 2 * distance_from_side, 2)
    }
```

---

## Logo Design

### Golden Circle Construction

```python
import matplotlib.pyplot as plt
import numpy as np

def draw_golden_circles(ax, base_radius=1, n_circles=5):
    """Draw concentric circles at golden ratio intervals."""
    phi = 1.618

    colors = plt.cm.viridis(np.linspace(0, 1, n_circles))

    for i in range(n_circles):
        radius = base_radius * (phi ** i)
        circle = plt.Circle(
            (0, 0), radius,
            fill=False,
            color=colors[i],
            linewidth=2
        )
        ax.add_patch(circle)
        ax.annotate(
            f'r={radius:.2f}',
            (radius * 0.7, radius * 0.7),
            fontsize=8
        )

    ax.set_xlim(-radius * 1.2, radius * 1.2)
    ax.set_ylim(-radius * 1.2, radius * 1.2)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    return ax


# Usage
fig, ax = plt.subplots(figsize=(10, 10))
draw_golden_circles(ax, base_radius=10, n_circles=6)
plt.title('Golden Ratio Circle Construction')
plt.show()
```

---

## Animation

### Golden Ratio Easing Function

```javascript
// Custom easing based on golden ratio
function goldenEase(t) {
  const phi = 1.618;
  return Math.pow(t, phi) / (Math.pow(t, phi) + Math.pow(1 - t, phi));
}

// Usage with CSS custom timing function approximation
const goldenBezier = 'cubic-bezier(0.4, 0, 0.2, 1)';
```

### Staggered Animation Timing

```javascript
const phi = 1.618;
const baseDelay = 100; // ms

function getStaggerDelay(index) {
  // Each element appears with golden ratio timing
  return baseDelay * Math.pow(phi, index * 0.5);
}

// Apply to elements
elements.forEach((el, i) => {
  el.style.animationDelay = `${getStaggerDelay(i)}ms`;
});
```

---

## Data Visualization

### Golden Spiral Chart

```python
import matplotlib.pyplot as plt
import numpy as np

def golden_spiral_chart(data, labels):
    """Create a chart based on golden spiral proportions."""
    phi = (1 + np.sqrt(5)) / 2

    fig, ax = plt.subplots(figsize=(12, 8))

    # Spiral parameters
    theta = np.linspace(0, 4 * np.pi, 1000)
    r = phi ** (theta / (2 * np.pi))

    # Plot spiral
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, 'b-', alpha=0.3, linewidth=1)

    # Place data points along spiral
    n_points = len(data)
    indices = np.linspace(0, len(theta) - 1, n_points, dtype=int)

    sizes = np.array(data) * 100  # Scale for visibility

    for i, (idx, label, size) in enumerate(zip(indices, labels, sizes)):
        ax.scatter(x[idx], y[idx], s=size, alpha=0.7, zorder=5)
        ax.annotate(label, (x[idx], y[idx]), fontsize=8)

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Data on Golden Spiral')

    return fig
```

---

## Quick Reference

### Common Calculations

```python
phi = 1.618033988749895

# Golden rectangle
height = width / phi
width = height * phi

# Layout proportions
main_content = total * 0.618
sidebar = total * 0.382

# Type scale
next_size = current_size * phi
previous_size = current_size / phi

# Fibonacci retracement
level_38 = high - (high - low) * 0.382
level_62 = high - (high - low) * 0.618

# Golden pocket
pocket_top = high - (high - low) * 0.618
pocket_bottom = high - (high - low) * 0.65
```

### Key Ratios

| Ratio | Value | Use |
|-------|-------|-----|
| φ | 1.618 | Layout, scaling |
| 1/φ | 0.618 | Inverse proportions |
| φ² | 2.618 | Extended proportions |
| 38.2% | 0.382 | Retracement, secondary |
| 61.8% | 0.618 | Primary division |
| 23.6% | 0.236 | Minor division |
