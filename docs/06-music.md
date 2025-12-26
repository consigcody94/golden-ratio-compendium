# The Golden Ratio in Music and Acoustics

## Musical Structure

### Fibonacci in Composition

Some composers have structured works around Fibonacci numbers:

```
Bar numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
```

#### Béla Bartók — *Music for Strings, Percussion, and Celesta* (1936)

The first movement demonstrates clear Fibonacci structure:

| Event | Bar Number | Fibonacci |
|-------|------------|-----------|
| Opening | 1 | F(1) |
| First development | 21 | F(8) |
| Climax | 55 | F(10) |
| Return | 68 | 89-21 |
| End | 89 | F(11) |

The climax occurs at bar 55 of 89 total bars:
```
55/89 ≈ 0.618 (golden ratio!)
```

#### Mozart's Piano Sonatas (Claimed)

Analysis of K. 279 in C Major:
- Exposition: 38 bars
- Development + Recapitulation: 62 bars
- Ratio: 62/38 = 1.63 ≈ φ

However:
- Not all Mozart sonatas follow this pattern
- No documentation of Mozart's intent
- May be coincidental

### The Golden Section in Musical Form

A piece structured by the golden section:

```
|← 100% of composition →|
|← 61.8% →|← 38.2% →|
   First     Second
   Section   Section
```

Or recursively:
```
|← 100% →|
|← 61.8% →|← 38.2% →|
|← 38.2% →|← 23.6% →|← 14.6% →|← 23.6% →|
```

---

## Harmony and Intervals

### Fibonacci Ratios in Harmonics

The harmonic series and Fibonacci numbers share a connection through simple ratios:

| Interval | Ratio | Fibonacci Connection |
|----------|-------|---------------------|
| Unison | 1:1 | F(1):F(1) |
| Octave | 2:1 | F(3):F(1) |
| Fifth | 3:2 | F(4):F(3) |
| Fourth | 4:3 | — |
| Major sixth | 5:3 | F(5):F(4) |
| Minor third | 6:5 | — |
| Major third | 5:4 | F(5):— |

### The Golden Ratio as an Interval

The golden ratio (1.618:1) corresponds to approximately **833 cents** (between a minor and major sixth).

```python
import math

phi = (1 + math.sqrt(5)) / 2
cents = 1200 * math.log2(phi)
print(f"φ as interval: {cents:.1f} cents")  # ~833.1 cents
```

For comparison:
- Minor sixth: 800 cents
- Major sixth: 900 cents
- Golden interval: 833 cents

### Bohlen's 833 Cent Scale

Heinz Bohlen created a scale based on the golden ratio:
- Uses φ as the fundamental interval
- Creates unique timbres and harmonies
- Experimental/microtonal application

---

## Room Acoustics

### The Golden Ratio Room

Ideal room dimension ratios for even frequency response:

```
Height : Width : Length = 1 : 1.6 : 2.6
```

Or more precisely:
```
1 : φ : φ²
1 : 1.618 : 2.618
```

### Why It Works

Room modes (standing waves) occur at frequencies determined by dimensions:

```
f = c / (2 × dimension)
```

Where c = speed of sound (~343 m/s)

**Problem**: Identical dimensions create overlapping modes (boomy sound)

**Solution**: Golden ratio spreads modes evenly across frequency spectrum

### Room Mode Calculator

```python
def room_modes(length, width, height, c=343):
    """Calculate first 10 axial room modes"""
    modes = []
    for dim, name in [(length, 'L'), (width, 'W'), (height, 'H')]:
        for n in range(1, 11):
            freq = (n * c) / (2 * dim)
            modes.append((freq, name, n))
    return sorted(modes)

# Golden ratio room: 3m × 4.85m × 7.85m
modes = room_modes(7.85, 4.85, 3)
```

### Studio Design

Professional recording studios often use golden ratio proportions:
- Control rooms
- Live rooms
- Isolation booths

Benefits:
- Even bass response
- Reduced standing waves
- Natural decay characteristics

---

## Speaker Design

### Cabinet Proportions

Speaker cabinet golden ratio:
```
Height : Width : Depth = φ² : φ : 1
```

Or:
```
2.618 : 1.618 : 1
```

This minimizes internal standing waves and cabinet resonances.

### Driver Placement

Some designs place drivers at golden ratio positions:
```
┌─────────┐
│    ○    │ ← Tweeter at H × 0.618 from top
│         │
│    ○    │ ← Woofer at H × 0.382 from bottom
│         │
└─────────┘
```

### Port Tuning

Bass reflex port tuning sometimes uses Fibonacci-related calculations for optimal response.

---

## Instrument Design

### Violin Construction

Stradivari and other master luthiers may have used golden proportions:

| Measurement | Ratio to Body Length |
|-------------|---------------------|
| Body length | 1.0 |
| Upper bout | ~0.382 |
| Lower bout | ~0.618 |
| F-hole position | Golden section |

**Note**: Historical documentation is limited; some claims may be retroactive analysis.

### Guitar Design

Classical guitar body proportions often approximate φ:
- Body length to width
- Sound hole position
- Bridge placement

### Piano Soundboard

Some piano manufacturers use golden ratio in:
- Soundboard dimensions
- String scale design
- Hammer positioning

---

## Practical Applications

### Composition Technique

Using the golden section for climax placement:

```python
def golden_climax(total_duration):
    """Calculate climax point using golden section"""
    phi = (1 + 5**0.5) / 2
    climax_point = total_duration / phi
    return climax_point

# For a 5-minute piece
climax = golden_climax(300)  # 185.4 seconds ≈ 3:05
```

### Mix Engineering

Some engineers use golden proportions for:
- Reverb decay times
- Delay timing
- EQ curve relationships

### Album Sequencing

Track placement within an album:
- Strongest track at ~62% through the album
- Key transition at golden section

---

## Critical Analysis

### What's Verified

- Room acoustics benefit from non-uniform dimensions
- Golden ratio is *one* effective room proportion
- Some composers intentionally used Fibonacci structures

### What's Overstated

- Universal application in classical music
- All great instruments use φ
- The "perfect" proportion for everything

### Alternative Ratios

Other room ratios recommended by acousticians:

| Ratio | Name | Source |
|-------|------|--------|
| 1:1.14:1.39 | Bolt | Richard Bolt |
| 1:1.28:1.54 | Louden | M. M. Louden |
| 1:1.60:2.33 | Bonello | Oscar Bonello |
| 1:1.618:2.618 | Golden | φ-based |

All of these work well; the golden ratio isn't uniquely superior.

---

## Code: Musical Applications

### MIDI Note from Golden Ratio

```python
def phi_interval_midi(base_note=60):
    """Calculate MIDI note a golden interval above base"""
    phi = (1 + 5**0.5) / 2
    cents = 1200 * math.log2(phi)
    semitones = cents / 100
    return base_note + semitones

# Middle C + golden interval
note = phi_interval_midi(60)  # ~68.33 (between G#4 and A4)
```

### Fibonacci Rhythm Generator

```python
def fibonacci_rhythm(n_beats):
    """Generate rhythm pattern using Fibonacci durations"""
    fib = [1, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])

    pattern = []
    total = 0
    for duration in fib:
        if total + duration > n_beats:
            break
        pattern.append(duration)
        total += duration
    return pattern

rhythm = fibonacci_rhythm(32)
# [1, 1, 2, 3, 5, 8, 13] — fits in 33 beats
```

---

## Conclusion

The golden ratio has genuine applications in music and acoustics:

1. **Room design**: Spreads acoustic modes effectively
2. **Composition**: Provides structural framework
3. **Speaker design**: Reduces cabinet resonances

However, it's one tool among many. Other ratios work equally well in most cases. The golden ratio is mathematically elegant but not acoustically magical.

## References

1. Golden Number: "Music and the Fibonacci Sequence and Phi"
2. Lendvai, E. "Béla Bartók: An Analysis of His Music"
3. Everest, F. A. "Master Handbook of Acoustics"
4. Aural Exchange: "Golden Ratio in Acoustics"
