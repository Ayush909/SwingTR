"""Stock data model."""

from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    price: float
    change_percent: float
    volume: int

    @classmethod
    def from_dict(cls, data):
        """Create a Stock instance from a dict."""
        return cls(
            symbol=data["symbol"],
            price=data["price"],
            change_percent=data["change_percent"],
            volume=data["volume"],
        )
