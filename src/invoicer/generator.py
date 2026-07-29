from docx import Document


class InvoiceGenerator:
    """
    Generate invoices from a Word template.

    Args:
        template_path: Path to the DOCX invoice template.
    """
    def __init__(self, template_path: str):
        self.template_path = template_path
        self.document = None

    def load_template(self) -> None:
        """Load the configured DOCX Word template into memory."""
        self.document = Document(self.template_path)

    def save(self, output_path: str) -> None:
        """
        Saves the generated DOCX invoice to a specified location.

        Args:
           output_path: Path to save the DOCX generated invoice.
        Raises:
            RuntimeError: if no template is loaded.
        """
        if self.document is None:
            raise RuntimeError("Cannot save invoice because no template has been loaded.")

        self.document.save(output_path)