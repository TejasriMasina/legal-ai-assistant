# app.py
import streamlit as st
from search_engine import search_similar_cases

st.set_page_config(page_title="Legal Case Recommender")

st.title("🔍 Legal Case Recommendation System")
st.markdown("Search past similar cases based on a query.")

query = st.text_area("Enter a legal query or case summary")

if st.button("Search") and query.strip():
    with st.spinner("Searching..."):
        results = search_similar_cases(query)
    for res in results:
        st.subheader(res["case_name"])
        st.write(f"**Court:** {res['court']} | **Date:** {res['date_filed']}")
        st.write(res["summary"])
        st.markdown("---")
