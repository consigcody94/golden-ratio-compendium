//! Golden Ratio Utilities in Rust
//!
//! A comprehensive library for working with the golden ratio (φ)
//! and Fibonacci sequences in Rust.

/// The golden ratio φ = (1 + √5) / 2
pub const PHI: f64 = 1.618_033_988_749_895;

/// The conjugate of φ: ψ = (1 - √5) / 2
pub const PSI: f64 = -0.618_033_988_749_895;

/// The golden angle in radians (~137.5°)
pub const GOLDEN_ANGLE: f64 = 2.399_963_229_728_653;

/// Golden ratio calculations
pub mod golden {
    use super::PHI;

    /// Calculate the inverse of φ (also equals φ - 1)
    pub fn inverse_phi() -> f64 {
        1.0 / PHI
    }

    /// Calculate φ raised to power n
    pub fn phi_power(n: i32) -> f64 {
        PHI.powi(n)
    }

    /// Check if two values are in golden ratio
    pub fn is_golden_ratio(a: f64, b: f64, tolerance: f64) -> bool {
        if b == 0.0 {
            return false;
        }
        (a / b - PHI).abs() < tolerance
    }

    /// Calculate the golden rectangle dimensions from width
    pub fn rectangle_from_width(width: f64) -> (f64, f64) {
        (width, width / PHI)
    }

    /// Calculate the golden rectangle dimensions from height
    pub fn rectangle_from_height(height: f64) -> (f64, f64) {
        (height * PHI, height)
    }

    /// Calculate layout divisions (main content, sidebar)
    pub fn layout_divisions(total_width: f64) -> (f64, f64) {
        let main = total_width * PHI / (1.0 + PHI);
        let sidebar = total_width / (1.0 + PHI);
        (main, sidebar)
    }
}

/// Fibonacci sequence implementations
pub mod fibonacci {
    use super::{PHI, PSI};

    /// Generate first n Fibonacci numbers
    pub fn sequence(n: usize) -> Vec<u64> {
        if n == 0 {
            return vec![];
        }
        if n == 1 {
            return vec![1];
        }

        let mut fib = Vec::with_capacity(n);
        fib.push(1);
        fib.push(1);

        for i in 2..n {
            let next = fib[i - 1] + fib[i - 2];
            fib.push(next);
        }

        fib
    }

    /// Calculate nth Fibonacci number iteratively
    pub fn nth(n: u32) -> u64 {
        if n <= 1 {
            return n as u64;
        }

        let mut a: u64 = 0;
        let mut b: u64 = 1;

        for _ in 2..=n {
            let temp = a + b;
            a = b;
            b = temp;
        }

        b
    }

    /// Calculate nth Fibonacci using Binet's formula
    /// Note: Loses precision for n > ~70
    pub fn nth_binet(n: u32) -> u64 {
        let n_f64 = n as f64;
        let result = (PHI.powf(n_f64) - PSI.powf(n_f64)) / 5.0_f64.sqrt();
        result.round() as u64
    }

    /// Calculate ratio of consecutive Fibonacci numbers
    pub fn ratio_at(n: u32) -> f64 {
        if n == 0 {
            return f64::NAN;
        }
        let f_n = nth(n) as f64;
        let f_n_minus_1 = nth(n - 1) as f64;

        if f_n_minus_1 == 0.0 {
            return f64::INFINITY;
        }

        f_n / f_n_minus_1
    }

    /// Check if a number is a Fibonacci number
    pub fn is_fibonacci(n: u64) -> bool {
        // A number is Fibonacci if one of 5n² + 4 or 5n² - 4 is a perfect square
        let test1 = 5 * n * n + 4;
        let test2 = 5 * n * n - 4;

        is_perfect_square(test1) || is_perfect_square(test2)
    }

    fn is_perfect_square(n: u64) -> bool {
        let sqrt = (n as f64).sqrt() as u64;
        sqrt * sqrt == n
    }

    /// Generator for Fibonacci numbers
    pub struct FibonacciIterator {
        current: u64,
        next: u64,
    }

    impl FibonacciIterator {
        pub fn new() -> Self {
            FibonacciIterator {
                current: 0,
                next: 1,
            }
        }
    }

    impl Default for FibonacciIterator {
        fn default() -> Self {
            Self::new()
        }
    }

    impl Iterator for FibonacciIterator {
        type Item = u64;

        fn next(&mut self) -> Option<Self::Item> {
            let result = self.current;
            self.current = self.next;
            self.next = result + self.next;
            Some(result)
        }
    }
}

/// Design scale utilities
pub mod design {
    use super::PHI;

    /// Generate a type scale based on golden ratio
    pub fn type_scale(base: f64, levels: usize) -> Vec<f64> {
        let mut scale = Vec::with_capacity(levels * 2 + 1);

        // Smaller sizes
        for i in (1..=levels).rev() {
            scale.push(base / PHI.powi(i as i32));
        }

        // Base
        scale.push(base);

        // Larger sizes
        for i in 1..=levels {
            scale.push(base * PHI.powi(i as i32));
        }

        scale
    }

    /// Generate a spacing scale
    pub fn spacing_scale(base: f64) -> Vec<f64> {
        vec![
            (base / PHI.powi(3)).round(),
            (base / PHI.powi(2)).round(),
            (base / PHI).round(),
            base,
            (base * PHI).round(),
            (base * PHI.powi(2)).round(),
            (base * PHI.powi(3)).round(),
            (base * PHI.powi(4)).round(),
            (base * PHI.powi(5)).round(),
        ]
    }

    /// Calculate optimal line height
    pub fn line_height(font_size: f64) -> f64 {
        font_size * PHI
    }
}

/// Fibonacci retracement for trading
pub mod trading {
    /// Fibonacci retracement levels
    pub const RETRACEMENT_LEVELS: [f64; 7] = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0];

    /// Fibonacci extension levels
    pub const EXTENSION_LEVELS: [f64; 5] = [1.272, 1.618, 2.0, 2.618, 4.236];

    /// Calculate retracement levels
    pub fn retracements(high: f64, low: f64, is_uptrend: bool) -> Vec<(String, f64)> {
        let diff = high - low;
        RETRACEMENT_LEVELS
            .iter()
            .map(|&level| {
                let price = if is_uptrend {
                    high - diff * level
                } else {
                    low + diff * level
                };
                (format!("{:.1}%", level * 100.0), price)
            })
            .collect()
    }

    /// Calculate extension levels
    pub fn extensions(high: f64, low: f64, is_uptrend: bool) -> Vec<(String, f64)> {
        let diff = high - low;
        EXTENSION_LEVELS
            .iter()
            .map(|&level| {
                let price = if is_uptrend {
                    low + diff * level
                } else {
                    high - diff * level
                };
                (format!("{:.1}%", level * 100.0), price)
            })
            .collect()
    }

    /// Calculate golden pocket zone (61.8% - 65%)
    pub fn golden_pocket(high: f64, low: f64, is_uptrend: bool) -> (f64, f64) {
        let diff = high - low;
        if is_uptrend {
            (high - diff * 0.618, high - diff * 0.65)
        } else {
            (low + diff * 0.618, low + diff * 0.65)
        }
    }
}

/// Phyllotaxis pattern generation
pub mod phyllotaxis {
    use super::GOLDEN_ANGLE;

    /// Generate sunflower seed pattern points
    pub fn sunflower_pattern(n_points: usize, scale: f64) -> Vec<(f64, f64)> {
        (0..n_points)
            .map(|i| {
                let r = scale * (i as f64).sqrt();
                let theta = (i as f64) * GOLDEN_ANGLE;
                (r * theta.cos(), r * theta.sin())
            })
            .collect()
    }

    /// Generate golden spiral points
    pub fn golden_spiral(n_points: usize, growth: f64) -> Vec<(f64, f64)> {
        use std::f64::consts::PI;

        (0..n_points)
            .map(|i| {
                let angle = (i as f64) * 0.1;
                let r = growth.powf(angle / (2.0 * PI));
                (r * angle.cos(), r * angle.sin())
            })
            .collect()
    }
}

/// Golden section search algorithm
pub mod optimization {
    use super::PHI;

    /// Find minimum of unimodal function using golden section search
    pub fn golden_section_search<F>(f: F, mut a: f64, mut b: f64, tolerance: f64) -> f64
    where
        F: Fn(f64) -> f64,
    {
        let resphi = 2.0 - PHI; // 1/φ ≈ 0.618

        let mut x1 = a + resphi * (b - a);
        let mut x2 = b - resphi * (b - a);
        let mut f1 = f(x1);
        let mut f2 = f(x2);

        while (b - a).abs() > tolerance {
            if f1 < f2 {
                b = x2;
                x2 = x1;
                f2 = f1;
                x1 = a + resphi * (b - a);
                f1 = f(x1);
            } else {
                a = x1;
                x1 = x2;
                f1 = f2;
                x2 = b - resphi * (b - a);
                f2 = f(x2);
            }
        }

        (a + b) / 2.0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_phi_properties() {
        // φ² = φ + 1
        assert!((PHI * PHI - PHI - 1.0).abs() < 1e-10);

        // 1/φ = φ - 1
        assert!((1.0 / PHI - (PHI - 1.0)).abs() < 1e-10);
    }

    #[test]
    fn test_fibonacci_sequence() {
        let fib = fibonacci::sequence(10);
        assert_eq!(fib, vec![1, 1, 2, 3, 5, 8, 13, 21, 34, 55]);
    }

    #[test]
    fn test_fibonacci_nth() {
        assert_eq!(fibonacci::nth(1), 1);
        assert_eq!(fibonacci::nth(10), 55);
        assert_eq!(fibonacci::nth(20), 6765);
    }

    #[test]
    fn test_is_fibonacci() {
        assert!(fibonacci::is_fibonacci(0));
        assert!(fibonacci::is_fibonacci(1));
        assert!(fibonacci::is_fibonacci(13));
        assert!(fibonacci::is_fibonacci(144));
        assert!(!fibonacci::is_fibonacci(4));
        assert!(!fibonacci::is_fibonacci(100));
    }

    #[test]
    fn test_fibonacci_ratio_converges() {
        let ratio = fibonacci::ratio_at(20);
        assert!((ratio - PHI).abs() < 1e-8);
    }

    #[test]
    fn test_golden_rectangle() {
        let (w, h) = golden::rectangle_from_width(161.8);
        assert!((h - 100.0).abs() < 0.1);
    }

    #[test]
    fn test_golden_section_search() {
        // Find minimum of (x-2)²
        let f = |x: f64| (x - 2.0).powi(2);
        let min = optimization::golden_section_search(f, 0.0, 5.0, 1e-6);
        assert!((min - 2.0).abs() < 1e-5);
    }
}

fn main() {
    println!("=".repeat(60));
    println!("GOLDEN RATIO UTILITIES - RUST");
    println!("=".repeat(60));

    println!("\nConstants:");
    println!("  φ = {}", PHI);
    println!("  1/φ = {}", golden::inverse_phi());
    println!("  φ² = {}", golden::phi_power(2));

    println!("\nFibonacci sequence (first 15):");
    let fib = fibonacci::sequence(15);
    println!("  {:?}", fib);

    println!("\nFibonacci ratios converging to φ:");
    for n in 5..=12 {
        let ratio = fibonacci::ratio_at(n);
        let error = (ratio - PHI).abs();
        println!("  F({})/F({}) = {:.10}, error = {:.2e}", n, n - 1, ratio, error);
    }

    println!("\nType scale (base: 16px):");
    let scale = design::type_scale(16.0, 4);
    for (i, size) in scale.iter().enumerate() {
        let level = i as i32 - 4;
        println!("  level {:+}: {:.2}px", level, size);
    }

    println!("\nFibonacci retracements (high: 200, low: 100):");
    let retracements = trading::retracements(200.0, 100.0, true);
    for (level, price) in retracements {
        println!("  {}: ${:.2}", level, price);
    }

    println!("\nGolden pocket:");
    let (upper, lower) = trading::golden_pocket(200.0, 100.0, true);
    println!("  Upper: ${:.2}", upper);
    println!("  Lower: ${:.2}", lower);

    println!("\nGolden section search - find min of (x-3)²:");
    let f = |x: f64| (x - 3.0).powi(2);
    let min = optimization::golden_section_search(f, 0.0, 10.0, 1e-6);
    println!("  Minimum at x = {:.6}", min);
}
