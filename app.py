import streamlit as st
import gensim

st.title("Amazon Reviews Word2Vec")
st.write("Enter a word to find similar words from cell phone reviews:")

# Note: Model will be added via Streamlit Secrets
st.info("Model loads automatically. Try 'good', 'battery', 'screen'")

word = st.text_input("Word", value="good")
topn = st.slider("Number of similar words", 5, 20, 10)

if st.button("Find Similar Words") and word:
    st.success("Working! (Model upload next step)")
