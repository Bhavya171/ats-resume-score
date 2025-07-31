# ATS Resume Score Detector

An **ATS (Applicant Tracking System) Resume Scoring Tool** tailored for **Data Analyst** and **Data Scientist** roles.  
This project parses resumes, extracts relevant information, compares them against a given **job description (JD)**, and returns an **ATS score** along with **matched** and **missing keywords**.

---

## Features
- **Resume Parsing**
  - Extracts email, phone, skills, raw text from PDF/DOCX resumes
  - Primary parsing with [pyresparser](https://github.com/OmkarPathak/pyresparser)
  - Fallback extraction with [pdfplumber](https://github.com/jsvine/pdfplumber) + regex
- **Job Description Parsing**
  - Extracts important keywords using **TF-IDF** (via scikit-learn)
  - Handles soft skills, hard skills, and tools
- **Scoring Engine**
  - Compares JD keywords against parsed resume text
  - Outputs ATS score, matched keywords, and missing keywords
- **Logging & Exception Handling**
  - Centralized logging in `/logs`
  - Custom exception classes for parsing, scoring, and JD extraction errors
- **Automated Testing**
  - [pytest](https://docs.pytest.org/) test suite for all modules
  - Unit tests and end-to-end test for scoring pipeline
- **CLI Support**
  - Run from terminal:  
    ```bash
    python ats_score.py resume.pdf jd.txt
    ```

---

## Project Structure
ats_resume_score/
├── ats_score.py # CLI tool for scoring
├── logs/
│ └── app.log
├── src/
│ ├── parser/
│ │ ├── resume_parser.py
│ │ └── jd_parser.py
│ ├── scorer/
│ │ └── score_engine.py
│ ├── services/
│ │ └── score_service.py
│ └── utils/
│ ├── logger.py
│ ├── exceptions.py
│ └── file_validation.py
├── tests/
│ ├── test_resume_parser.py
│ ├── test_jd_parser.py
│ ├── test_score_engine.py
│ └── test_score_service.py
├── requirements.txt
└── README.md


---

## Installation

### 1 Clone Repository
```bash
git clone https://github.com/<your-username>/ats-resume-score.git
cd ats-resume-score
```
### 2 Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3 Install Requirements
```
pip install -r requirements.txt
```
## Usage
```
python ats_score.py resume.pdf jd.txt
```
## Running Tests
```
pytest -v
```
