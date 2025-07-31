import pytest
from src.services.score_service import process_resume_and_jd

def test_process_resume_and_jd(monkeypatch):
    # Patch inside score_service namespace where it is used
    monkeypatch.setattr("src.services.score_service.parse_resume", lambda *a, **k: ({"raw_text": "python sql"}, []))
    monkeypatch.setattr("src.services.score_service.extract_keywords_from_jd", lambda *a, **k: ["python", "sql", "tableau"])
    monkeypatch.setattr("src.services.score_service.compute_resume_score", lambda *a, **k: {
        "score": 66.67,
        "matched_keywords": ["python", "sql"],
        "missing_keywords": ["tableau"]
    })

    # Run service
    result = process_resume_and_jd("fake_path.pdf", "JD text", ["email"])

    assert result["score"] == 66.67
    assert "python" in result["matched_keywords"]
    assert "tableau" in result["missing_keywords"]
    assert result["missing_fields"] == []
