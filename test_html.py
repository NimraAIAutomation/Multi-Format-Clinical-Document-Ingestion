
from extractors.html_extractor import extract_html

file_path = "sample_clinical.html"

result = extract_html(file_path)

print("METADATA:")
print(result["metadata"])

print("\nSTRUCTURED CONTENT:")

for item in result["content"]:
    print(item)

print("\nFULL TEXT:")
print(result["text"])
