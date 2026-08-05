from pathlib import Path
import pytest
from invoicer.generator import InvoiceGenerator


def test_load_valid_template() -> None:
    # Arrange - what we need to set up for the test
    template_path = Path(__file__).parent / "resources" / "sample_invoice.docx"
    generator = InvoiceGenerator(template_path)

    # Act - what we are testing
    generator.load_template()

    # Assert - what we expect to happen
    assert generator.document is not None

def test_save_loaded_template_creates_docx_file(tmp_path: Path) -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" / "sample_invoice.docx"
    generator = InvoiceGenerator(template_path)
    generator.load_template()
    output_path = tmp_path / "output_invoice.docx"

    # Act
    generator.save(output_path)

    # Assert
    assert output_path.exists()
    # Ensure the file is not empty
    assert output_path.stat().st_size > 0

def test_save_without_loading_template_raises_runtime_error(tmp_path: Path) -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" /"sample_invoice.docx"
    generator = InvoiceGenerator(template_path)
    output_path = tmp_path / "output_invoice.docx"

    # Act & Assert
    with pytest.raises(RuntimeError):
        generator.save(output_path)

def test_replace_placeholders_updates_document_text() -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" / "sample_placeholder_invoice.docx"
    generator = InvoiceGenerator(template_path)
    generator.load_template()
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd"
    }

    # Act
    generator.replace_placeholders(invoice_data)

    # Assert
    assert generator.document.paragraphs[0].text == "Hello Acme Pty Ltd"

def test_replace_placeholders_without_loaded_document_raises_runtime_error() -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" / "sample_placeholder_invoice.docx"
    generator = InvoiceGenerator(template_path)
    invoice_data = {
        "CLIENT_NAME": "Acme Pty Ltd"
    }

    # Act & Assert
    with pytest.raises(RuntimeError):
        generator.replace_placeholders(invoice_data)

def test_replace_multiple_placeholders_updates_document_text() -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" / "sample_multiple_placeholder_invoice.docx"
    generator = InvoiceGenerator(template_path)
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

def test_replace_placeholders_with_missing_placeholder_does_not_change_text() -> None:
    # Arrange
    template_path = Path(__file__).parent / "resources" / "sample_multiple_placeholder_invoice.docx"
    generator = InvoiceGenerator(template_path)
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