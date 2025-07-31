import pytest
from src.parser.jd_parser import extract_keywords_from_jd
from src.utils.exceptions import JDParsingError

def test_empty_jd():
    with pytest.raises(JDParsingError):
        extract_keywords_from_jd("")

def test_valid_jd():
    jd_text = "We need a Data Analyst with Python, SQL, and Tableau experience."
    keywords = extract_keywords_from_jd(jd_text, top_n=5)
    assert isinstance(keywords, list)
    assert "python" in keywords or "sql" in keywords
