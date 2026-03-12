import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from query_generator import generate_queries
from embedding_matcher import match_jobs
from job_api import JoobleAPI

api = JoobleAPI()

st.set_page_config(page_title="AI Job Finder", layout="wide")

st.title("🤖 AI Job Finder")

st.write("Upload your resume and find matching jobs automatically.")

file = st.file_uploader("📄 Upload Resume", type=["pdf"])


if file:

    if st.button("🔍 Analyze Resume"):

        with st.spinner("Reading resume..."):

            text = extract_resume_text(file)

        skills = extract_skills(text)

        st.success("Skills extracted successfully!")

        st.subheader("🧠 Extracted Skills")
        st.write(skills)

        queries = generate_queries(skills)

        st.subheader("🔎 Generated Job Search Queries")

        for q in queries:
            st.write("•", q)

        all_jobs = []

        progress = st.progress(0)

        for i, q in enumerate(queries):

            jobs = api.search_jobs(q)

            all_jobs.extend(jobs)

            progress.progress((i+1)/len(queries))

        ranked = match_jobs(skills, all_jobs)

        st.subheader("🎯 Top Job Matches")

        for job, score in ranked[:10]:

            with st.container():

                st.markdown(f"### {job['title']}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write("🏢 Company:", job["company"])

                with col2:
                    st.write("📊 Match Score:", round(score,2))

                with col3:
                    st.link_button("Apply Now 🚀", job["link"])

                st.divider()