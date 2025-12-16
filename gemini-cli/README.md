# Gemini CLI Tools

This directory contains a set of command-line interface (CLI) tools that provide a local interface to the document processing skills.

## Tools

- `gemini-pptx`: A tool for working with PowerPoint presentations.
- `gemini-docx`: A tool for working with Word documents.
- `gemini-xlsx`: A tool for working with Excel spreadsheets.
- `gemini-pdf`: A tool for working with PDF documents.

## Installation

To use these tools, you will need to install the following dependencies:

### System Dependencies

- **pandoc**: For converting `.docx` files to markdown.
  ```bash
  sudo apt-get install pandoc
  ```

- **poppler-utils**: For working with PDF files (`pdftotext`, `pdfimages`).
  ```bash
  sudo apt-get install poppler-utils
  ```

- **libreoffice**: For recalculating formulas in `.xlsx` files and converting documents to PDF.
  ```bash
  sudo apt-get install libreoffice
  ```

### Python Dependencies

You can install the required Python packages using pip:

```bash
pip install "markitdown[pptx]" defusedxml openpyxl
```

## Usage

Each tool provides a set of subcommands for different operations. You can get more information about each tool by running it with the `--help` flag:

```bash
./gemini_pptx.py --help
./gemini_docx.py --help
./gemini_xlsx.py --help
./gemini_pdf.py --help
```
