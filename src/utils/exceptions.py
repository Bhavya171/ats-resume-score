class ResumeParsingError(Exception):
    """Raised when resume parsing fails completely."""
    pass

class InvalidFileFormatError(Exception):
    """Raised for unsupported file types (e.g., .exe or .png)."""
    pass

class JDParsingError(Exception):
    """Raised when job description parsing fails."""
    pass

class ScoringError(Exception):
    """Raised when resume scoring encounters issues."""
    pass
