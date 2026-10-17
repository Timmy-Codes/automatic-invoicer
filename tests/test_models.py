from datetime import date
from decimal import Decimal

from invoicer.models import InvoiceData


def test_create_invoice_data_object_with_valid_data() -> None:
    # Arrange
    client_name     = "Acme Pty Ltd"
    client_address  = "123 Example Street, Sydney NSW 2000"
    invoice_number  = "INV-001"
    invoice_date    = date(2026, 8, 9)
    description     = "Consulting services"
    unit_price      = Decimal("250.00")
    quantity        = 1
    total           = Decimal("250.00")

    # Act
    invoice_data = InvoiceData(
        client_name=client_name,
        client_address=client_address,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        description=description,
        unit_price=unit_price,
        quantity=quantity,
        total=total,
    )

    # Assert
    assert invoice_data.client_name == client_name
    assert invoice_data.client_address == client_address
    assert invoice_data.invoice_number == invoice_number
    assert invoice_data.invoice_date == invoice_date
    assert invoice_data.description == description
    assert invoice_data.unit_price == unit_price
    assert invoice_data.quantity == quantity
    assert invoice_data.total == total
