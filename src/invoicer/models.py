from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

@dataclass
class InvoiceData:
    client_name: str
    client_address: str
    invoice_number: str
    invoice_date: date
    description: str
    unit_price: Decimal
    quantity: int
    total: Decimal = field(init=False)  # total will be calculated based on unit_price and quantity

    def __post_init__(self) -> None:
        # Calculate the total
        self.total = self.unit_price * Decimal(self.quantity)