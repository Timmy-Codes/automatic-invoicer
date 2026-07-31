from pathlib import Path
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
