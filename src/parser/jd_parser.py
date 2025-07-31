import re
from typing import List
from src.utils.logger import logger
from src.utils.exceptions import JDParsingError

from sklearn.feature_extraction.text import TfidfVectorizer


def clean_text(text: str) -> str:
    """Lowercase and remove non-alphanumeric characters."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_keywords_from_jd(jd_text: str, top_n: int = 20) -> List[str]:
    """
    Extracts the top N keywords from a job description using TF-IDF.

    Args:
        jd_text: The raw job description text.
        top_n: Number of keywords to return.

    Returns:
        List of top keywords.
    """
    logger.info("Starting JD parsing...")

    if not jd_text or not jd_text.strip():
        logger.error("Empty job description provided.")
        raise JDParsingError("Job description text is empty.")

    try:
        cleaned_text = clean_text(jd_text)

        # Use TF-IDF to extract keywords
        '''
        TF‑IDF stands for Term Frequency – Inverse Document Frequency.
        It’s a statistical method used in NLP to figure out which words in a document are important compared to other documents.
        '''
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([cleaned_text])

        keywords_scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
        sorted_keywords = sorted(keywords_scores, key=lambda x: -x[1])

        keywords = [kw for kw, score in sorted_keywords[:top_n]]

        logger.info(f"Extracted {len(keywords)} keywords from JD.")
        return keywords

    except Exception as e:
        logger.error(f"JD parsing failed: {e}")
        raise JDParsingError(str(e))
