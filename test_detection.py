from processing.pipeline import extract_document

result = extract_document("diabetes.pdf")

print("Detected format:", result["metadata"]["format"])
print("Total pages:", result["metadata"]["page_count"])