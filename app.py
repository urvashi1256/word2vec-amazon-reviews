import streamlit as st
import gensim
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    return gensim.models.Word2Vec.load("./word2vec-amazon-cell-accessories-reviews-short.model")

model = load_model()

st.title("📱 Amazon Reviews Word2Vec")
st.write("Enter a word to find similar words from cell phone reviews:")

word = st.text_input("Word", value="good")
topn = st.slider("Number of similar words", 5, 20, 10)

if st.button("Find Similar Words") and word:
    if word in model.wv:
        sims = model.wv.most_similar(word, topn=topn)
        st.subheader(f"Similar to '{word}':")
        for w, score in sims:
            st.write(f"**{w}** ({score:.3f})")
    else:
        st.error(f"'{word}' not in vocabulary")
