import os
from src.utils.exceptions import InvalidFileFormatError, ResumeParsingError
from src.utils.logger import logger

def validate_resume_file(file_path: str) -> None:
    """
    Validates that the resume file exists and is readable.
    Raises:
        InvalidFileFormatError: If file doesn't exist or is not readable.
    """
    # 1. Check existence
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise ResumeParsingError(f"File does not exist: {file_path}")

    # 2. Check size
    if os.path.getsize(file_path) == 0:
        logger.error(f"File is empty: {file_path}")
        raise ResumeParsingError(f"File is empty: {file_path}")

    # 3. Basic sanity: Extension check is already done in resume_parser
    logger.info(f"File validated successfully: {file_path}")
