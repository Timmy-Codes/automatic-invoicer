from pathlib import Path
from invoicer.generator import InvoiceGenerator


def test_load_valid_template():
    # Arrange - what we need to set up for the test
    template_path = Path(__file__).parent / "resources" / "sample_invoice.docx"
    generator = InvoiceGenerator(template_path)

    # Act - what we are testing
    generator.load_template()

    # Assert - what we expect to happen
    assert generator.document is not None