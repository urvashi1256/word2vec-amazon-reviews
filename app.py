import streamlit as st
import gensim
import os

st.title("Amazon Reviews Word2Vec")

# DEBUG: Show files
st.write("**Files in repo:**")
for file in os.listdir("."):
    st.write(f"- {file} ({os.path.getsize(file)/1000000:.1f}MB)" if os.path.isfile(file) else f"- {file}/")

# Try to load model
try:
    model = gensim.models.Word2Vec.load("word2vec-amazon-cell-accessories-reviews-short.model")
    st.success("✅ Model loaded!")
    st.write(f"Vocab size: {len(model.wv)} words")
except Exception as e:
    st.error(f"❌ Model error: {str(e)}")
    st.stop()

word = st.text_input("Word", value="good")
topn = st.slider("Number of similar words", 5, 20, 10)

if st.button("Find Similar Words") and word:
    if word in model.wv:
        sims = model.wv.most_similar(word, topn=topn)
        st.subheader(f"Similar to '{word}':")
        for w, score in sims:
            st.write(f"{w} ({score:.3f})")
    else:
        st.error(f"'{word}' not in vocabulary")
