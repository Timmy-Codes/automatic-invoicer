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