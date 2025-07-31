from src.services.score_service import process_resume_and_jd

if __name__ == "__main__":
    file_path = "C:\\Users\\bhave\\OneDrive\\Documents\\RESUME\\Resume BJ.pdf"
    jd_text = """
    We are seeking a motivated and curious Data Scientist to join our dynamic analytics team. As a starter at
ION, you will work closely with senior data scientists and business stakeholders to extract insights from
complex financial datasets and support the development of predictive models that enhance our products
and services.
Key Responsibilities
 Assist in collecting, cleaning, and preprocessing large volumes of structured and unstructured
data.
 Support exploratory data analysis to identify trends, patterns, and anomalies.
 Help build and validate predictive models using machine learning algorithms.
 Collaborate with cross-functional teams including software engineers, business analysts, and
domain experts.
 Contribute to creating data visualizations and reports to communicate findings clearly to
technical and non-technical audiences.
 Stay up to date with the latest data science techniques and tools relevant to financial services.

Preferred:
 Knowledge of financial markets or interest in financial technologies.
 Experience with data visualization tools (e.g., Tableau, Power BI, matplotlib, seaborn).
Understanding of cloud platforms (AWS, Azure, GCP) or big data technologies is a bonus.
Required Skills, Qualifications:
 Bachelor’s or Master’s degree in Computer Science, Statistics, Mathematics, Economics,
Engineering, or a related field.
 Basic understanding of statistics, machine learning, and data analysis techniques.
 Familiarity with programming languages such as Python or R.
 Experience with data manipulation and analysis libraries (e.g., pandas, numpy, scikit-learn).
 Exposure to SQL and database querying.
 Good problem-solving skills and attention to detail.
 Strong communication skills and the ability to work collaboratively in a team environment.
 Prior internship or project experience in data science or analytics is a plus.
    """
    
    required_fields = ["email", "phone", "raw_text"]
    result = process_resume_and_jd(file_path, jd_text, required_fields)

    print(f"\nATS Score: {result['score']}%")
    print(f"Matched Keywords: {result['matched_keywords']}")
    print(f"Missing Keywords: {result['missing_keywords']}")
    print(f"Missing Fields: {result['missing_fields']}")
