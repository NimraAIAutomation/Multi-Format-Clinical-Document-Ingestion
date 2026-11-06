from extractors.ocr_extractor import extract_image_ocr

file_path = "F:\Bracketltd\RAG\clinical_document_ingestion\diabetes.jpg"

result = extract_image_ocr(file_path)

print("METADATA:")
print(result["metadata"])

print("\nEXTRACTED TEXT:")
print(result["pages"][0]["text"])
