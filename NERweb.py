import spacy
import streamlit as st
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Set up Streamlit app
st.title("Data Entity Recognition")

# Get user input
text = st.text_area("Enter text", "")

# Process text with spaCy
doc = nlp(text)

# Display named entities
if doc.ents:
    html = displacy.render(doc, style="ent", jupyter=False)
    st.write(html, unsafe_allow_html=True)
else:
    st.write("No named entities found.")


