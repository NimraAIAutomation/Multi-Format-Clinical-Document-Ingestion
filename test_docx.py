from extractors.docx_extractor import extract_docx

file_path = "F:\Bracketltd\RAG\clinical_document_ingestion\Clinical Assessment.docx"

result = extract_docx(file_path)

print("METADATA:")
print(result["metadata"])

print("\nPARAGRAPHS:")
for paragraph in result["paragraphs"]:
    print(paragraph)

print("\nTABLES:")
for table in result["tables"]:
    print(table)