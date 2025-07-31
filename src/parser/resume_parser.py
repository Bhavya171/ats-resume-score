import os
from typing import Dict, Any, List, Optional, Tuple
import pdfplumber, re
from pyresparser import ResumeParser

from src.utils.logger import logger
from src.utils.exceptions import ResumeParsingError, InvalidFileFormatError
from src.utils.file_validation import validate_resume_file  

# checking again because it is a good practice
def is_allowed_file(filename: str, allowed_exts={".pdf", ".docx"}) -> bool:
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_exts

def fallback_pdfplumber(file_path: str) -> Dict[str, Any]:
    """Fallback parser using pdfplumber + regex to extract basic fields."""
    fields = {}
    try:
        with pdfplumber.open(file_path) as pdf:
            text = '\n'.join((page.extract_text() or '') for page in pdf.pages)
    except Exception as e:
        raise ResumeParsingError(f"pdfplumber failed: {str(e)}")

    # Basic field extraction with regex
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone_match = re.search(r"(\+?\d[\d \-]{8,}\d)", text)

    fields["email"] = email_match.group(0) if email_match else None
    fields["phone"] = phone_match.group(0) if phone_match else None
    fields["raw_text"] = text
    return fields

def parse_resume(
    file_path: str,
    required_fields: List[str],
    static_info: Optional[Dict[str, Any]] = None,
) -> Tuple[Dict[str, Any], List[str]]:

    """
    Parses the resume, merges with static info, and identifies missing fields.
    Returns:
        - merged (dict): Field-value pairs
        - missing_fields (list): Fields still empty
    """
    logger.info(f"Starting parse for: {file_path}")

    if not is_allowed_file(file_path):
        logger.warning(f"Invalid file extension for: {file_path}")
        raise InvalidFileFormatError(f"Unsupported file type: {file_path}")

    validate_resume_file(file_path) 

    parsed = {}
    try:
        parsed = ResumeParser(file_path).get_extracted_data() or {}
        logger.info("pyresparser succeeded")
    except Exception as e:
        logger.warning(f"pyresparser failed: {e}")
        parsed = {}

    essentials_missing = [f for f in required_fields if not parsed.get(f)]
    if essentials_missing and file_path.lower().endswith('.pdf'):
        try:
            fallback = fallback_pdfplumber(file_path)
            for f in essentials_missing:
                if fallback.get(f):
                    parsed[f] = fallback[f]
            logger.info("Fallback parser merged missing fields.")
        except Exception as e:
            logger.error(f"Fallback also failed: {e}")

    merged = {}
    static_info = static_info or {}
    for field in required_fields:
        merged[field] = parsed.get(field) or static_info.get(field)

    missing_fields = [f for f in required_fields if not merged.get(f)]
    logger.info(f"Parsed Fields: {merged}")
    logger.info(f"Missing Fields: {missing_fields}")

    if not merged and missing_fields == required_fields:
        raise ResumeParsingError("Resume parsing completely failed.")

    return merged, missing_fields
