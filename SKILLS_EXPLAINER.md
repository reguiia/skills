# Skills Explainer

This document provides an overview of the `pptx`, `docx`, `xlsx`, and `pdf` skills, which are designed to handle various document formats. Each skill offers a set of tools and workflows for creating, editing, and analyzing the corresponding file type. The provided CLI tools implement a subset of these capabilities.

## PPTX Skill

The `pptx` skill is designed for working with PowerPoint presentations. The CLI tool provides functionalities for:

- **Creating Presentations:** Users can create new presentations from scratch by providing a directory of HTML files, which are then converted to a `.pptx` file.
- **Editing Presentations:** The skill allows for the modification of existing presentations by unpacking the `.pptx` file, editing the underlying XML content, and then repacking it.
- **Analyzing Presentations:** Text can be extracted from presentations for analysis, and the skill provides access to the raw XML for examining comments, speaker notes, and other details.

## DOCX Skill

The `docx` skill is focused on Word documents. The CLI tool offers the following capabilities:

- **Document Editing:** The skill supports editing existing documents, including a "redlining" workflow for tracking changes, which is particularly useful for legal and collaborative work. The CLI provides tools to unpack and pack docx files for manual editing.
- **Text Extraction:** The CLI can convert `.docx` files to markdown, preserving tracked changes for review.

## XLSX Skill

The `xlsx` skill is designed for spreadsheet manipulation and data analysis. The CLI tool provides the following key feature:

- **Formula Recalculation:** The CLI tool can recalculate all formulas in a workbook using a provided script, ensuring that all values are up-to-date after any programmatic or manual changes.
- **Data Analysis:** For data-centric tasks, the underlying skill leverages the `pandas` library to read, analyze, and write spreadsheet data.

## PDF Skill

The `pdf` skill provides a comprehensive toolkit for handling PDF documents. The CLI tool's functionalities include:

- **Text and Table Extraction:** The skill can extract both text and tables from PDFs, making it useful for data extraction and analysis.
- **PDF Manipulation:** The CLI tool supports common PDF operations such as merging and splitting documents.
- **Form Filling:** The underlying skill also includes capabilities for filling out PDF forms.
