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

#### Windows
- **Pandoc**: Go to the [Pandoc installation page](https://pandoc.org/installing.html), download the installer for Windows (`.msi`), and run it.
- **LibreOffice**: Go to the [LibreOffice download page](https://www.libreoffice.org/download/download-libreoffice/) and download the main installer. Run it and follow the on-screen instructions.
- **Poppler**: Follow this [step-by-step guide to install Poppler on Windows](https://blog.alivate.com.au/poppler-windows/).
- **qpdf**: Download the latest `.exe` installer from the [qpdf GitHub releases page](https://github.com/qpdf/qpdf/releases).

#### macOS (using Homebrew)
```bash
brew install pandoc poppler libreoffice qpdf
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update && sudo apt-get install -y pandoc poppler-utils libreoffice qpdf
```

### Python Dependencies

You can install the required Python packages using pip:

```bash
pip install "markitdown[pptx]" defusedxml openpyxl
```

## Usage

Each tool provides a set of subcommands for different operations. You can get more information about each tool by running it with the `--help` flag:

```bash
python3 gemini_pptx.py --help
python3 gemini_docx.py --help
python3 gemini_xlsx.py --help
python3 gemini_pdf.py --help
```

### Creating a new Presentation

To create a new presentation, you first need to create a directory of HTML files, where each file represents a single slide. Then, you can use the `create` command:

```bash
python3 gemini_pptx.py create <html_directory> <output_file.pptx>
```
