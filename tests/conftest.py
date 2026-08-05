from pathlib import Path
import pytest

RESOURCE_DIR = Path(__file__).parent / "resources"

@pytest.fixture
def sample_invoice_path() -> Path:
    """Fixture to provide the path to a sample invoice template."""
    return RESOURCE_DIR / "sample_invoice.docx"

@pytest.fixture
def sample_placeholder_invoice_path() -> Path:
    """Fixture to provide the path to a sample placeholder invoice template."""
    return RESOURCE_DIR / "sample_placeholder_invoice.docx"

@pytest.fixture
def sample_multiple_placeholder_invoice_path() -> Path:
    """Fixture to provide the path to a sample multiple placeholder invoice template."""
    return RESOURCE_DIR / "sample_multiple_placeholder_invoice.docx"
