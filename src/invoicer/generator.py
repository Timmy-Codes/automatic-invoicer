from docx import Document

class InvoiceGenerator:
    def __init__(self, template_path):
        self.template_path = template_path
        self.document = None

    def load_template(self):
        self.document = Document(self.template_path)