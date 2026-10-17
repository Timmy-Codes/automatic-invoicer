from dataclasses import dataclass
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
    total: Decimal
