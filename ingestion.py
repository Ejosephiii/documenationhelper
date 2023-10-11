import os
from langchain.document_loaders import ReadTheDocsLoader


def ingest_docs()->None:
    loader = ReadTheDocsLoader(path="langchain-docs/api.python.langchain.com/en/latest", encoding="ISO-8859-1")



    raw_documents = loader.load()

if __name__ == "__main__":
    ingest_docs()