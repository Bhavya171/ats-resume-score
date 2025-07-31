from typing import Dict, List
from src.utils.logger import logger
from src.utils.exceptions import ScoringError

def compute_resume_score(resume_data: Dict[str, str], jd_keywords: List[str]) -> Dict[str, any]:
    """
    Compare resume against JD keywords and compute a match score.

    Args:
        resume_data: Parsed resume fields including 'raw_text'.
        jd_keywords: List of extracted keywords from the JD.

    Returns:
        dict: { score, matched_keywords, missing_keywords }
    """
    logger.info("Starting scoring process...")

    try:
        resume_text = (resume_data.get("raw_text") or "").lower()
        matched = [kw for kw in jd_keywords if kw.lower() in resume_text]
        missing = list(set(jd_keywords) - set(matched))

        # Basic score calculation: % of JD keywords present in resume
        score = round((len(matched) / len(jd_keywords) * 100), 2) if jd_keywords else 0

        result = {
            "score": score,
            "matched_keywords": matched,
            "missing_keywords": missing
        }

        logger.info(f"Scoring complete. Score: {score}%")
        return result

    except Exception as e:
        logger.error(f"Scoring failed: {e}")
        raise ScoringError(str(e))
