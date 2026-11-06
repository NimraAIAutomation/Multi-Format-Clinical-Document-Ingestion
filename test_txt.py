from extractors.txt_extractor import extract_txt

file_path = "sample_clinical.txt"

result = extract_txt(file_path)

print("METADATA:")
print(result["metadata"])

print("\nEXTRACTED TEXT:")
print(result["text"])
