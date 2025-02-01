import sys
import os
import streamlit as st

# Add the parent directory (project root) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mistral_integration import generate_answer
from cortex_search import query_cortex_search # import backend modules

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# List all files and folders in the current directory
print("Files and folders in working directory:", os.listdir(os.getcwd()))

# Set the title of the app
st.title("AskDocs AI: Intelligent Knowledge Assistant")

# Upload documents
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv"])
if uploaded_file:
    st.success("File uploaded successfully!")

# Query input
query = st.text_input("Ask a question:")
if query:
    with st.spinner("Searching..."):
        # Step 1: Retrieve relevant content
        results = query_cortex_search(query)
        st.subheader("Retrieved Content")
        for result in results:
            st.write(result[0])

        # Step 2: Generate an answer
        if results:
            context = " ".join([r[0] for r in results])
            answer = generate_answer(f"Context: {context}\nQuestion: {query}")
            st.subheader("Generated Answer")
            st.write(answer)
