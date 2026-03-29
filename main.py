#!/usr/bin/env python3
"""Main CLI entry point for SwingTR stock analysis tool."""

from services.stock_service import fetch_all_stocks


def display_stocks(stocks):
    """Display stock data in a formatted table."""
    header = f"{'SYMBOL':<15} {'PRICE':>10} {'CHANGE %':>10} {'VOLUME':>15}"
    separator = "-" * len(header)

    print(f"\n{'SwingTR - NIFTY 50 Stock Scanner':^{len(header)}}")
    print(separator)
    print(header)
    print(separator)

    for stock in stocks:
        change_str = f"{stock.change_percent:+.2f}%"
        volume_str = f"{stock.volume:,}"
        print(f"{stock.symbol:<15} {stock.price:>10.2f} {change_str:>10} {volume_str:>15}")

    print(separator)
    print(f"Total: {len(stocks)} stocks")


def main():
    print("SwingTR - Stock Analysis CLI for Swing Trading\n")
    stocks = fetch_all_stocks()
    if stocks:
        display_stocks(stocks)
    else:
        print("No stock data available.")


if __name__ == "__main__":
    main()
