import streamlit as st

st.set_page_config(page_title="Resume Relevance Checker", layout="wide")

st.title("📄 Automated Resume Relevance Check System")

st.write("Upload a resume and paste a job description to evaluate relevance.")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")

if st.button("Evaluate"):
    if resume_file and jd_text.strip():
        st.success("✅ Processing... (LLM pipeline will run here)")
        # TODO: Integrate resume_parser, jd_parser, scorer
        st.write("🔎 Sample Output:")
        st.write("- Relevance Score: 78/100")
        st.write("- Matched Skills: Python, SQL, Machine Learning")
        st.write("- Missing Skills: AWS, Docker")
    else:
        st.error("Please upload a resume and provide a job description.")
