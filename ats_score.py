import argparse
from src.services.score_service import process_resume_and_jd

def main():
    parser = argparse.ArgumentParser(description="ATS Resume Score Detector")
    parser.add_argument("resume", help="Path to the resume file (.pdf or .docx)")
    parser.add_argument("jobdesc", help="Path to the job description text file")
    args = parser.parse_args()

    # Read the job description text file
    with open(args.jobdesc, "r", encoding="utf-8") as f:
        jd_text = f.read()

    required_fields = ["email", "phone", "raw_text"]

    try:
        result = process_resume_and_jd(args.resume, jd_text, required_fields)
        print("\n=== ATS Resume Score ===")
        print(f"Score: {result['score']}%")
        print(f"Matched Keywords: {result['matched_keywords']}")
        print(f"Missing Keywords: {result['missing_keywords']}")
        print(f"Missing Fields: {result['missing_fields']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
