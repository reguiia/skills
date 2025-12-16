#!/usr/bin/env python3

import argparse
from utils import run_command

def extract_text(args):
    """Extracts text from a .pdf file."""
    pdf_file = args.pdf_file
    output_file = args.output_file
    layout = "-layout" if args.layout else ""
    command = f"pdftotext {layout} {pdf_file} {output_file}"
    print(f"Running: {command}")
    run_command(command)

def merge(args):
    """Merges multiple .pdf files into one."""
    pdf_files = " ".join(args.pdf_files)
    output_file = args.output_file
    command = f"qpdf --empty --pages {pdf_files} -- {output_file}"
    print(f"Running: {command}")
    run_command(command)

def split(args):
    """Splits a .pdf file into multiple files."""
    pdf_file = args.pdf_file
    output_prefix = args.output_prefix
    command = f"qpdf {pdf_file} --split-pages {output_prefix}%d.pdf"
    print(f"Running: {command}")
    run_command(command)

def extract_images(args):
    """Extracts images from a .pdf file."""
    pdf_file = args.pdf_file
    output_prefix = args.output_prefix
    command = f"pdfimages -j {pdf_file} {output_prefix}"
    print(f"Running: {command}")
    run_command(command)

def main():
    parser = argparse.ArgumentParser(description="A command-line interface for the pdf skill.")
    subparsers = parser.add_subparsers(dest="command", required=T)

    # Sub-parser for extract-text
    parser_extract_text = subparsers.add_parser("extract-text", help="Extract text from a .pdf file.")
    parser_extract_text.add_argument("pdf_file", help="The .pdf file to extract text from.")
    parser_extract_text.add_argument("output_file", help="The output text file.")
    parser_extract_text.add_argument("--layout", action="store_true", help="Preserve the layout of the original PDF.")
    parser_extract_text.set_defaults(func=extract_text)

    # Sub-parser for merge
    parser_merge = subparsers.add_parser("merge", help="Merge multiple .pdf files.")
    parser_merge.add_argument("output_file", help="The output .pdf file.")
    parser_merge.add_argument("pdf_files", nargs='+', help="The .pdf files to merge.")
    parser_merge.set_defaults(func=merge)

    # Sub-parser for split
    parser_split = subparsers.add_parser("split", help="Split a .pdf file.")
    parser_split.add_argument("pdf_file", help="The .pdf file to split.")
    parser_split.add_argument("output_prefix", help="The prefix for the output files.")
    parser_split.set_defaults(func=split)

    # Sub-parser for extract-images
    parser_extract_images = subparsers.add_parser("extract-images", help="Extract images from a .pdf file.")
    parser_extract_images.add_argument("pdf_file", help="The .pdf file to extract images from.")
    parser_extract_images.add_argument("output_prefix", help="The prefix for the output image files.")
    parser_extract_images.set_defaults(func=extract_images)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
