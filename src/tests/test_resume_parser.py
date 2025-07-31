import os
import pytest
from src.parser.resume_parser import parse_resume
from src.utils.exceptions import InvalidFileFormatError, ResumeParsingError

# Sample paths (you need to place a small PDF resume in tests/sample_data)
SAMPLE_RESUME_PDF = os.path.join(os.path.dirname(__file__), "sample_data", "C:\\Users\\bhave\\OneDrive\\Documents\\RESUME\\Resume BJ.pdf")
SAMPLE_FAKE_FILE = os.path.join(os.path.dirname(__file__), "sample_data", "fake.exe")

def test_invalid_file_format():
    with pytest.raises(InvalidFileFormatError):
        parse_resume(SAMPLE_FAKE_FILE, required_fields=["email", "phone"])

def test_missing_file():
    with pytest.raises(ResumeParsingError):
        parse_resume("nonexistent.pdf", required_fields=["email", "phone"])

def test_valid_resume_parsing():
    result, missing = parse_resume(SAMPLE_RESUME_PDF, required_fields=["email", "phone", "raw_text"])
    assert isinstance(result, dict)
    assert "raw_text" in result
