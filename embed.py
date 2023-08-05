from sentence_transformers import SentenceTransformer
import streamlit as st

model = SentenceTransformer('all-MiniLM-L6-v2', device='cuda')

#Our sentences we like to encode
sentences = ['The quick brown fox jumps over the lazy dog.']

if st.button('run'):
    #Sentences are encoded by calling model.encode()
    sentence_embeddings = model.encode(sentences)

    #Print the embeddings
    for sentence, embedding in zip(sentences, sentence_embeddings):
        st.write("Sentence:", sentence)
        st.dataframe(embedding.tolist(), use_container_width=True, height=300)