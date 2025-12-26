"""
Golden Ratio CLI Tool

A command-line interface for golden ratio calculations.
"""

import argparse
import sys
from typing import Optional

from golden_ratio import __version__
from golden_ratio.constants import PHI, GOLDEN_ANGLE_DEGREES
from golden_ratio.core import GoldenRatio, GoldenRectangle
from golden_ratio.fibonacci import Fibonacci, fib_fast_doubling, lucas_number
from golden_ratio.design import DesignScale
from golden_ratio.trading import FibonacciTrading


def print_header(title: str) -> None:
    """Print a formatted header."""
    print("=" * 60)
    print(title)
    print("=" * 60)


def print_section(title: str) -> None:
    """Print a section divider."""
    print()
    print("-" * 40)
    print(title)
    print("-" * 40)


def cmd_info(args: argparse.Namespace) -> None:
    """Display golden ratio information."""
    print_header("GOLDEN RATIO INFORMATION")
    print()
    print(f"  phi (φ)           = {PHI}")
    print(f"  1/phi             = {GoldenRatio.inverse_phi()}")
    print(f"  phi²              = {GoldenRatio.phi_power(2)}")
    print(f"  phi³              = {GoldenRatio.phi_power(3)}")
    print(f"  Golden angle      = {GOLDEN_ANGLE_DEGREES:.4f}°")
    print()
    print("Properties:")
    print("  φ² = φ + 1")
    print("  1/φ = φ - 1")
    print("  φ = [1; 1, 1, 1, ...] (continued fraction)")


def cmd_fibonacci(args: argparse.Namespace) -> None:
    """Generate Fibonacci sequence."""
    n = args.count
    print_header(f"FIBONACCI SEQUENCE (first {n})")
    print()

    fib = Fibonacci.sequence(n)
    print(f"  {fib}")

    if args.ratios:
        print_section("Ratio Convergence to φ")
        for i in range(2, min(n, 15)):
            ratio = fib[i] / fib[i - 1]
            error = abs(ratio - PHI)
            print(f"  F({i})/F({i-1}) = {fib[i]}/{fib[i-1]} = {ratio:.10f}, error = {error:.2e}")


def cmd_rectangle(args: argparse.Namespace) -> None:
    """Calculate golden rectangle dimensions."""
    print_header("GOLDEN RECTANGLE")
    print()

    if args.width:
        rect = GoldenRectangle.from_width(args.width)
        print(f"  Given width: {args.width}")
    else:
        rect = GoldenRectangle.from_height(args.height)
        print(f"  Given height: {args.height}")

    print()
    for key, value in rect.items():
        print(f"  {key}: {value}")


def cmd_scale(args: argparse.Namespace) -> None:
    """Generate design scales."""
    base = args.base
    print_header(f"DESIGN SCALES (base: {base}px)")

    print_section("Typography Scale")
    type_scale = DesignScale.type_scale(base)
    for name, size in type_scale.items():
        print(f"  {name:10}: {size}px")

    print_section("Spacing Scale")
    spacing = DesignScale.spacing_scale(base)
    for name, size in sorted(spacing.items()):
        print(f"  {name:10}: {size}px")

    print_section("Layout Divisions (width: 1200px)")
    layout = DesignScale.layout_divisions(1200)
    for key, value in layout.items():
        unit = "%" if "percent" in key else "px"
        print(f"  {key:18}: {value}{unit}")


def cmd_trading(args: argparse.Namespace) -> None:
    """Calculate Fibonacci trading levels."""
    high = args.high
    low = args.low
    is_uptrend = not args.downtrend

    print_header(f"FIBONACCI TRADING LEVELS (High: {high}, Low: {low})")

    print_section("Retracement Levels")
    retracements = FibonacciTrading.retracements(high, low, is_uptrend)
    for level, price in retracements.items():
        print(f"  {level:8}: ${price:.4f}")

    print_section("Extension Levels")
    extensions = FibonacciTrading.extensions(high, low, is_uptrend)
    for level, price in extensions.items():
        print(f"  {level:8}: ${price:.4f}")

    print_section("Golden Pocket")
    pocket = FibonacciTrading.golden_pocket(high, low, is_uptrend)
    for key, value in pocket.items():
        print(f"  {key:10}: ${value:.4f}")


def cmd_nth(args: argparse.Namespace) -> None:
    """Calculate nth Fibonacci/Lucas number."""
    n = args.n
    print_header(f"CALCULATING F({n}) AND L({n})")
    print()

    fib_n = fib_fast_doubling(n)
    lucas_n = lucas_number(n)

    digits_fib = len(str(fib_n))
    digits_lucas = len(str(lucas_n))

    print(f"  F({n}) = {fib_n if digits_fib <= 50 else f'({digits_fib} digits)'}")
    print(f"  L({n}) = {lucas_n if digits_lucas <= 50 else f'({digits_lucas} digits)'}")
    print()
    print(f"  F({n}) has {digits_fib} digits")
    print(f"  L({n}) has {digits_lucas} digits")

    if n > 1:
        fib_n1 = fib_fast_doubling(n + 1)
        ratio = fib_n1 / fib_n if fib_n > 0 else 0
        error = abs(ratio - PHI)
        print()
        print(f"  F({n+1})/F({n}) = {ratio:.15f}")
        print(f"  Error from φ  = {error:.2e}")


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="golden-ratio",
        description="Golden Ratio Calculator - A comprehensive toolkit for φ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  golden-ratio info                    Show golden ratio information
  golden-ratio fib 20                  First 20 Fibonacci numbers
  golden-ratio fib 20 --ratios         Include ratio convergence
  golden-ratio rect --width 1920       Golden rectangle from width
  golden-ratio scale --base 16         Design scales (typography, spacing)
  golden-ratio trading 200 100         Fibonacci retracement levels
  golden-ratio nth 100                 Calculate F(100) and L(100)
""",
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # info command
    info_parser = subparsers.add_parser("info", help="Display golden ratio information")
    info_parser.set_defaults(func=cmd_info)

    # fibonacci command
    fib_parser = subparsers.add_parser("fib", help="Generate Fibonacci sequence")
    fib_parser.add_argument("count", type=int, help="Number of Fibonacci numbers")
    fib_parser.add_argument(
        "--ratios", action="store_true", help="Show ratio convergence"
    )
    fib_parser.set_defaults(func=cmd_fibonacci)

    # rectangle command
    rect_parser = subparsers.add_parser("rect", help="Calculate golden rectangle")
    rect_group = rect_parser.add_mutually_exclusive_group(required=True)
    rect_group.add_argument("--width", type=float, help="Rectangle width")
    rect_group.add_argument("--height", type=float, help="Rectangle height")
    rect_parser.set_defaults(func=cmd_rectangle)

    # scale command
    scale_parser = subparsers.add_parser("scale", help="Generate design scales")
    scale_parser.add_argument(
        "--base", type=float, default=16, help="Base size in pixels (default: 16)"
    )
    scale_parser.set_defaults(func=cmd_scale)

    # trading command
    trading_parser = subparsers.add_parser("trading", help="Fibonacci trading levels")
    trading_parser.add_argument("high", type=float, help="Swing high price")
    trading_parser.add_argument("low", type=float, help="Swing low price")
    trading_parser.add_argument(
        "--downtrend", action="store_true", help="Calculate for downtrend"
    )
    trading_parser.set_defaults(func=cmd_trading)

    # nth command
    nth_parser = subparsers.add_parser("nth", help="Calculate nth Fibonacci/Lucas number")
    nth_parser.add_argument("n", type=int, help="Index of the number")
    nth_parser.set_defaults(func=cmd_nth)

    return parser


def main(args: Optional[list] = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.command is None:
        parser.print_help()
        return 0

    try:
        parsed_args.func(parsed_args)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
