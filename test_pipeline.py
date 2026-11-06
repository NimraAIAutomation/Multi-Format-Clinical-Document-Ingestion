
from processing.pipeline import extract_document

files = [
    "diabetes.pdf",
    "Clinical Assessment.docx",
    "sample_clinical.txt",
    "sample_clinical.html",
    "sample_clinical.png"
]

for file in files:

    print("\n" + "=" * 50)
    print("PROCESSING:", file)

    try:
        result = extract_document(file)

        print("FORMAT:", result["metadata"]["format"])
        print("METADATA:", result["metadata"])

    except Exception as error:
        print("ERROR:", error)
