# Skills Explainer

This document provides an overview of the `pptx`, `docx`, `xlsx`, and `pdf` skills, which are designed to handle various document formats. Each skill offers a set of tools and workflows for creating, editing, and analyzing the corresponding file type.

## PPTX Skill

The `pptx` skill is designed for working with PowerPoint presentations. It provides functionalities for:

- **Creating Presentations:** Users can create new presentations from scratch by defining the content and layout in HTML and then converting it to a `.pptx` file.
- **Editing Presentations:** The skill allows for the modification of existing presentations by unpacking the `.pptx` file, editing the underlying XML content, and then repacking it.
- **Analyzing Presentations:** Text can be extracted from presentations for analysis, and the skill provides access to the raw XML for examining comments, speaker notes, and other details.

## DOCX Skill

The `docx` skill is focused on Word documents and offers the following capabilities:

- **Document Creation:** New `.docx` files can be created using a JavaScript-based approach, allowing for programmatic document generation.
- **Document Editing:** The skill supports editing existing documents, including a "redlining" workflow for tracking changes, which is particularly useful for legal and collaborative work.
- **Text Extraction:** Pandoc is used to convert `.docx` files to markdown, preserving tracked changes for review.

## XLSX Skill

The `xlsx` skill is designed for spreadsheet manipulation and data analysis, with a strong emphasis on preserving data integrity and formula functionality. Key features include:

- **Spreadsheet Creation and Editing:** The skill uses the `openpyxl` library to create and modify `.xlsx` files, allowing for the insertion of formulas, data, and formatting.
- **Data Analysis:** For data-centric tasks, the skill leverages the `pandas` library to read, analyze, and write spreadsheet data.
- **Formula Recalculation:** A critical feature is the ability to recalculate all formulas in a workbook using a provided script, ensuring that all values are up-to-date.

## PDF Skill

The `pdf` skill provides a comprehensive toolkit for handling PDF documents. Its functionalities include:

- **PDF Creation:** New PDFs can be generated from scratch using the `reportlab` library.
- **Text and Table Extraction:** The skill can extract both text and tables from PDFs, making it useful for data extraction and analysis.
- **PDF Manipulation:** Common PDF operations such as merging, splitting, rotating pages, and adding watermarks are supported.
- **Form Filling:** The skill also includes capabilities for filling out PDF forms.
