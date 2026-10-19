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

    @property
    def total(self) -> Decimal:
      # Calculate the total
      return self.unit_price * Decimal(self.quantity)