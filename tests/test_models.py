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
    expected_total  = Decimal("250.00")

    # Act
    invoice_data = InvoiceData(
        client_name=client_name,
        client_address=client_address,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        description=description,
        unit_price=unit_price,
        quantity=quantity,
    )

    # Assert
    assert invoice_data.client_name == client_name
    assert invoice_data.client_address == client_address
    assert invoice_data.invoice_number == invoice_number
    assert invoice_data.invoice_date == invoice_date
    assert invoice_data.description == description
    assert invoice_data.unit_price == unit_price
    assert invoice_data.quantity == quantity
    assert invoice_data.total == expected_total


def test_invoice_total_is_calculated_from_unit_price_and_quantity() -> None:
    # Arrange
    client_name     = "Acme Pty Ltd"
    client_address  = "123 Example Street, Sydney NSW 2000"
    invoice_number  = "INV-002"
    invoice_date    = date(2026, 8, 9)
    description     = "Consulting services"
    unit_price      = Decimal("125.50")
    quantity        = 4
    expected_total  = Decimal("502.00")

    # Act
    invoice = InvoiceData(
        client_name=client_name,
        client_address=client_address,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        description=description,
        unit_price=unit_price,
        quantity=quantity,
    )

    # Assert
    assert invoice.total == expected_total


def test_invoice_total_calculation_preserves_decimal_precision() -> None:
    # Arrange
    client_name     = "Acme Pty Ltd"
    client_address  = "123 Example Street, Sydney NSW 2000"
    invoice_number  = "INV-003"
    invoice_date    = date(2026, 8, 9)
    description     = "Consulting services"
    unit_price      = Decimal("19.99")
    quantity        = 3
    expected_total  = Decimal("59.97")

    # Act
    invoice = InvoiceData(
        client_name=client_name,
        client_address=client_address,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        description=description,
        unit_price=unit_price,
        quantity=quantity,
    )

    # Assert
    assert invoice.total == expected_total