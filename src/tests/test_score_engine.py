import pytest
from src.scorer.score_engine import compute_resume_score

def test_scoring_basic():
    resume_data = {"raw_text": "Python SQL Tableau Excel"}
    jd_keywords = ["python", "sql", "tableau", "power bi"]

    result = compute_resume_score(resume_data, jd_keywords)
    
    assert "score" in result
    assert isinstance(result["score"], float)
    assert "matched_keywords" in result
    assert isinstance(result["matched_keywords"], list)
    assert "missing_keywords" in result
    assert isinstance(result["missing_keywords"], list)
    assert result["score"] > 0  # Should find matches
