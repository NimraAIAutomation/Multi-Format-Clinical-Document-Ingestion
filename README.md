# Multi-Format Clinical Document Ingestion Pipeline

A Python-based document ingestion application built with Streamlit. It extracts, cleans, standardizes, and chunks clinical documents in multiple formats to prepare them for Retrieval-Augmented Generation (RAG).

## Features

- **Multi-format support:** PDF, DOCX, TXT, HTML, and scanned PDF/images.
- **PDF Extraction:** Uses PyMuPDF to extract text page by page.
- **DOCX Extraction:** Uses python-docx to extract paragraphs and tables.
- **HTML Extraction:** Uses BeautifulSoup to extract structured content.
- **TXT Extraction:** Extracts plain text and document metadata.
- **OCR:** Uses Tesseract and pytesseract for scanned documents and images.
- **Unified Pipeline:** Automatically identifies document formats and selects the appropriate extractor.
- **Standardization:** Converts extracted content into a common structured representation.
- **Text Cleaning:** Normalizes whitespace while preserving document structure.
- **Chunking:** Implements configurable fixed-size chunking with overlap.
- **Metadata Preservation:** Retains source information and available page or paragraph references.
- **Streamlit Interface:** Provides document uploads, processing controls, previews, and JSON downloads.

## Processing Workflow

Upload Document → Format Detection → Text Extraction → Standardization → Cleaning → Chunking → JSON Output

## Project Structure

```text
clinical_document_ingestion/
│
├── app.py
├── README.md
├── clean_test.py
├── test_chunking.py
├── test_detection.py
├── test_docx.py
├── test_html.py
├── test_ocr.py
├── test_pdf.py
├── test_pipeline.py
├── test_schema.py
├── test_txt.py
├── requirements.txt
├── .gitignore
│
├── extractors/
│   ├── pdf_extractor.py
│   ├── docx_extractor.py
│   ├── txt_extractor.py
│   ├── html_extractor.py
│   └── ocr_extractor.py
│
├── processing/
│   ├── pipeline.py
│   ├── schema.py
│   ├── cleaning.py
│   └── chunking.py
│
├── tests/
│
└── output/
```

## Installation

Clone the repository or download the project.

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Tesseract OCR Installation

Install Tesseract OCR separately.

The development environment used:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Configure the executable path in the OCR extractor if necessary.

## Run the Application

```bash
streamlit run app.py
```

## How to Use

1. Open the Streamlit application.
2. Upload one or multiple clinical documents.
3. Select the desired chunk size.
4. Configure chunk overlap.
5. Set the maximum number of chunks.
6. Click **Process Documents**.
7. Review extracted content and metadata.
8. Preview generated chunks.
9. Download the processed document as JSON.

## Chunking Configuration

| Parameter | Description |
|---|---|
| Chunk Size | Maximum characters in each chunk |
| Chunk Overlap | Characters repeated between consecutive chunks |
| Maximum Chunks | Maximum number of chunks included in output |

The maximum chunk setting limits the output; it does not divide the complete document into exactly that number of chunks.

## Testing

The pipeline was experimented with using:

- WHO Global Report on Diabetes (PDF)
- Clinical Assessment (DOCX)
- Sample Clinical Document (TXT)
- Sample Clinical Guidelines (HTML)
- Scanned PDF and image OCR experiments

The four main document formats were successfully tested for extraction, standardization, and cleaning.

## Limitations

- OCR processing can be slower than regular text extraction.
- OCR output may contain recognition errors, especially in clinical terminology and numerical values.
- Current chunking uses fixed character sizes rather than semantic boundaries.
- Maximum chunk limits may exclude later document content.
- The pipeline prepares documents for RAG but does not yet implement embeddings, vector storage, retrieval, or answer generation.

## Future Improvements

- Semantic and structure-aware chunking.
- Embedding generation.
- Vector database integration.
- Similarity-based document retrieval.
- RAG-based question answering.
- Improved OCR optimization and error handling.

## Technologies Used

Python | Streamlit | PyMuPDF | python-docx | BeautifulSoup | pytesseract | Tesseract OCR | Pandas | Pillow

## Project Goal

To develop a reusable clinical document ingestion pipeline that prepares multiple clinical document formats for downstream RAG applications.
