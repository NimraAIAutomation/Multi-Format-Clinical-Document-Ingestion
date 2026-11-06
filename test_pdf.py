from extractors.pdf_extractor import extract_pdf

file_path = "F:\Bracketltd\RAG\clinical_document_ingestion\diabetes.pdf"

result = extract_pdf(file_path)

print("METADATA:")
print(result["metadata"])

print("\nTOTAL PAGES:", len(result["pages"]))

print("\nFIRST PAGE TEXT:")
print(result["pages"][0]["text"][:1000])

print("\nPAGE-BY-PAGE INSPECTION")

for page in result["pages"][:10]:

    text = page["text"]

    print(
        f"Page {page['page_number']}: "
        f"{len(text)} characters"
    )