import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

st.title("ScrapeSense")
url =  st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website, please wait...")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height=300)
        
        
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to know")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            st.write("Please wait for a while as output depends on the content of page")
            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)