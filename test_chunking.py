from processing.pipeline import extract_document, standardize_document
from processing.cleaning import clean_document
from processing.chunking import chunk_document

document = extract_document("diabetes.pdf")
document = standardize_document(document)
document = clean_document(document)

chunks = chunk_document(
    document,
    chunk_size=1000,
    overlap=200
)

print("Total chunks:", len(chunks))

for chunk in chunks[:3]:
    print("\nChunk ID:", chunk["chunk_id"])
    print("Length:", len(chunk["text"]))
    print("Metadata:", chunk["metadata"])
    print("Preview:", chunk["text"][:150])