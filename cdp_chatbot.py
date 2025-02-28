import requests
from bs4 import BeautifulSoup
import streamlit as st
import re

def fetch_documentation(url):
    """Fetches and parses documentation from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text content (adjust based on document structure)
        text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text_content
    except requests.exceptions.RequestException as e:
        return f"Error fetching documentation: {e}"

def build_index(documentation):
    """Builds a simple keyword index."""
    index = {}
    for cdp, doc in documentation.items():
        if isinstance(doc, str): #check if doc is a string.
            words = re.findall(r'\w+', doc.lower()) #find all words
            for word in words:
                if word not in index:
                    index[word] = {}
                if cdp not in index[word]:
                    index[word][cdp] = []
                index[word][cdp].append(doc)

    return index

def get_response(question, index, documentation):
    """Retrieves and formats a response based on the question."""
    question = re.findall(r'\w+', question.lower())
    relevant_docs = {}
    for word in question:
        if word in index:
            for cdp, docs in index[word].items():
                if cdp not in relevant_docs:
                    relevant_docs[cdp] = []
                relevant_docs[cdp].extend(docs)

    if not relevant_docs:
        return "Sorry, I couldn't find relevant information."

    response = ""
    for cdp, docs in relevant_docs.items():
        if docs:
            response += f"**{cdp.capitalize()}:**\n"
            #simple method, return the first relevant doc.
            response += docs[0][0:500] + "...\n\n" #truncate to 500 chars

    return response

# Streamlit app
st.title("CDP Support Chatbot")

@st.cache_data
def load_data():
    """Loads documentation and builds the index."""
    segment_url = "https://segment.com/docs/?ref=nav"
    mparticle_url = "https://docs.mparticle.com/"
    lytics_url = "https://docs.lytics.com/"
    zeotap_url = "https://docs.zeotap.com/home/en-us/"

    segment_docs = fetch_documentation(segment_url)
    mparticle_docs = fetch_documentation(mparticle_url)
    lytics_docs = fetch_documentation(lytics_url)
    zeotap_docs = fetch_documentation(zeotap_url)

    documentation = {
        "segment": segment_docs,
        "mparticle": mparticle_docs,
        "lytics": lytics_docs,
        "zeotap": zeotap_docs,
    }

    index = build_index(documentation)
    return index, documentation

index, documentation = load_data()

question = st.text_input("Ask a question about Segment, mParticle, Lytics, or Zeotap:")

if question:
    response = get_response(question, index, documentation)
    st.write(response)
    
    