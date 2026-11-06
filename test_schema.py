from processing.pipeline import (
    extract_document,
    standardize_document
)

files = [
    "diabetes.pdf",
    "Clinical Assessment.docx",
    "sample_clinical.txt",
    "sample_clinical.html"
]

for file_path in files:
    print("\n" + "=" * 40)

    extracted = extract_document(file_path)
    document = standardize_document(extracted)

    print("File:", file_path)
    print("Format:", document["source_format"])
    print("Content keys:", list(document["content"].keys()))