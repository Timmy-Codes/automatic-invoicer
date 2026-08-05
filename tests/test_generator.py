from pathlib import Path
import pytest
from invoicer.generator import InvoiceGenerator


def test_load_valid_template(sample_invoice_path: Path) -> None:
    # Arrange - what we need to set up for the test
    generator = InvoiceGenerator(sample_invoice_path)

    # Act - what we are testing
    generator.load_template()

    # Assert - what we expect to happen
    assert generator.document is not None

def test_save_loaded_template_creates_docx_file(tmp_path: Path, sample_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_invoice_path)
    generator.load_template()
    output_path = tmp_path / "output_invoice.docx"

    # Act
    generator.save(output_path)

    # Assert
    assert output_path.exists()
    # Ensure the file is not empty
    assert output_path.stat().st_size > 0

def test_save_without_loading_template_raises_runtime_error(tmp_path: Path, sample_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_invoice_path)
    output_path = tmp_path / "output_invoice.docx"

    # Act & Assert
    with pytest.raises(RuntimeError):
        generator.save(output_path)

def test_replace_placeholders_updates_document_text(sample_placeholder_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_placeholder_invoice_path)
    generator.load_template()
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd"
    }

    # Act
    generator.replace_placeholders(invoice_data)

    # Assert
    assert generator.document.paragraphs[0].text == "Hello Acme Pty Ltd"

def test_replace_placeholders_without_loaded_document_raises_runtime_error(sample_placeholder_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_placeholder_invoice_path)
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd"
    }

    # Act & Assert
    with pytest.raises(RuntimeError):
        generator.replace_placeholders(invoice_data)

def test_replace_multiple_placeholders_updates_document_text(sample_multiple_placeholder_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_multiple_placeholder_invoice_path)
    generator.load_template()
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd",
        "INVOICE_NUMBER": "INV-001",
        "AMOUNT": "$250.00",
    }

    # Act
    generator.replace_placeholders(invoice_data)

    # Assert
    assert generator.document.paragraphs[0].text == "Client Name: Acme Pty Ltd"
    assert generator.document.paragraphs[1].text == "Invoice Number: INV-001"
    assert generator.document.paragraphs[2].text == "Amount: $250.00"

def test_replace_placeholders_with_missing_placeholder_does_not_change_text(sample_multiple_placeholder_invoice_path: Path) -> None:
    # Arrange
    generator = InvoiceGenerator(sample_multiple_placeholder_invoice_path)
    generator.load_template()
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd",
        "AMOUNT": "$250.00",
    }

    # Act
    generator.replace_placeholders(invoice_data)

    # Assert
    assert generator.document.paragraphs[0].text == "Client Name: Acme Pty Ltd"
    assert generator.document.paragraphs[1].text == "Invoice Number: {{INVOICE_NUMBER}}"
    assert generator.document.paragraphs[2].text == "Amount: $250.00"