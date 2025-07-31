from typing import Dict, Any
from src.parser.resume_parser import parse_resume
from src.parser.jd_parser import extract_keywords_from_jd
from src.scorer.score_engine import compute_resume_score
from src.utils.logger import logger
from src.utils.exceptions import ResumeParsingError, JDParsingError, ScoringError

def process_resume_and_jd(file_path: str, jd_text: str, required_fields: list, static_info: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Orchestrates parsing, keyword extraction, and scoring.
    """
    logger.info("Starting ATS resume scoring process...")

    try:
        # Step 1: Parse resume
        resume_data, missing_fields = parse_resume(file_path, required_fields, static_info)
        logger.info(f"Resume parsed. Missing fields: {missing_fields}")

        # Step 2: Extract keywords from JD
        jd_keywords = extract_keywords_from_jd(jd_text)
        logger.info(f"Extracted JD keywords: {jd_keywords}")

        # Step 3: Score the resume
        score_result = compute_resume_score(resume_data, jd_keywords)

        return {
            "score": score_result["score"],
            "matched_keywords": score_result["matched_keywords"],
            "missing_keywords": score_result["missing_keywords"],
            "missing_fields": missing_fields
        }

    except (ResumeParsingError, JDParsingError, ScoringError) as e:
        logger.error(f"Processing failed: {e}")
        raise
