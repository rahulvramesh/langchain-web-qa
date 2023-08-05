# main function with search
from langchain.chains import VectorDBQAWithSourcesChain

# from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA,ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


import os

# from chromadb.utils import embedding_functions

# from sentence_transformers import SentenceTransformer
# default_ef = embedding_functions.DefaultEmbeddingFunction()

repo_id = "sentence-transformers/all-MiniLM-L6-v2"
hf = HuggingFaceHubEmbeddings(
    repo_id=repo_id,
    task="feature-extraction",
    huggingfacehub_api_token="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",
)

# Env Area
os.environ["OPENAI_API_KEY"] = "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"


def process_llm_response(llm_response):
    print(llm_response["result"])
    print("\n\nSources:")
    for source in llm_response["source_documents"]:
        print(source.metadata["source"])


def main():
    vectordb = Chroma(
        persist_directory="./db",
        collection_name="health",
        embedding_function=hf,
    )

    # retriever = vectordb.as_retriever()

    # docs = retriever.get_relevant_documents("H")

    # len(docs)

    retriever = vectordb.as_retriever(search_kwargs={"k": 10})
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), retriever.as_retriever(), memory=memory)


    # qa_chain = RetrievalQA.from_chain_type(
    #     llm=OpenAI(),
    #     chain_type="stuff",
    #     retriever=retriever,
    #     return_source_documents=True,
    #     verbose=True,
    # )

    query = "summarize 262 – AMA #49: Heart rate recovery, strength training, rucking, kidney function, and brain health"
    llm_response = qa(query)
    
    #print(llm_response)
    process_llm_response(llm_response)

    # embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # sentences = ["This is an example sentence", "Each sentence is converted"]

    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # embeddings = model.encode(sentences)
    # print(embeddings)

    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # vectordb = Chroma(persist_directory='./db', collection_name='health', embedding_function=embedding_functions['sentence_transformer'])

    # Load Embedding
    # embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # db3 = Chroma(persist_directory="./db",collection_name='health', embedding_function=embedding_function)

    # query = "What did the president say about Ketanji Brown Jackson"
    # docs = db3.similarity_search(query)
    # print(docs[0].page_content)

    # QA Chain
    # chain = VectorDBQAWithSourcesChain.from_llm(
    #     llm=OpenAI(temperature=0), vectorstore=store
    # )


if __name__ == "__main__":
    main()
