#!/usr/bin/env python3

import argparse
import os
from utils import run_command, get_skill_path

def extract_text(args):
    """Extracts text from a .docx file using pandoc."""
    docx_file = args.docx_file
    output_file = args.output_file
    track_changes = args.track_changes
    command = f"pandoc --track-changes={track_changes} {docx_file} -o {output_file}"
    print(f"Running: {command}")
    run_command(command)

def unpack(args):
    """Unpacks a .docx file into its XML components."""
    docx_file = args.docx_file
    output_dir = args.output_dir
    script_path = os.path.join(get_skill_path('docx'), 'ooxml/scripts/unpack.py')
    command = f"python3 {script_path} {docx_file} {output_dir}"
    print(f"Running: {command}")
    run_command(command)

def pack(args):
    """Packs a directory of XML components into a .docx file."""
    input_dir = args.input_dir
    output_file = args.output_file
    script_path = os.path.join(get_skill_path('docx'), 'ooxml/scripts/pack.py')
    command = f"python3 {script_path} {input_dir} {output_file}"
    print(f"Running: {command}")
    run_command(command)

def to_images(args):
    """Converts a .docx file to a series of images."""
    docx_file = args.docx_file
    output_prefix = args.output_prefix

    # Convert to PDF
    pdf_file = os.path.splitext(docx_file)[0] + ".pdf"
    soffice_command = f"soffice --headless --convert-to pdf {docx_file}"
    print(f"Running: {soffice_command}")
    run_command(soffice_command)

    # Convert PDF to images
    pdftoppm_command = f"pdftoppm -jpeg -r 150 {pdf_file} {output_prefix}"
    print(f"Running: {pdftoppm_command}")
    run_command(pdftoppm_command)

    print(f"Images saved with prefix: {output_prefix}")

def main():
    parser = argparse.ArgumentParser(description="A command-line interface for the docx skill.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-parser for extract-text
    parser_extract_text = subparsers.add_parser("extract-text", help="Extract text from a .docx file.")
    parser_extract_text.add_argument("docx_file", help="The .docx file to extract text from.")
    parser_extract_text.add_argument("output_file", help="The output markdown file.")
    parser_extract_text.add_argument("--track-changes", default="all", choices=["accept", "reject", "all"], help="How to handle tracked changes.")
    parser_extract_text.set_defaults(func=extract_text)

    # Sub-parser for unpack
    parser_unpack = subparsers.add_parser("unpack", help="Unpack a .docx file.")
    parser_unpack.add_argument("docx_file", help="The .docx file to unpack.")
    parser_unpack.add_argument("output_dir", help="The directory to unpack the files into.")
    parser_unpack.set_defaults(func=unpack)

    # Sub-parser for pack
    parser_pack = subparsers.add_parser("pack", help="Pack a directory into a .docx file.")
    parser_pack.add_argument("input_dir", help="The directory to pack.")
    parser_pack.add_argument("output_file", help="The output .docx file.")
    parser_pack.set_defaults(func=pack)

    # Sub-parser for to-images
    parser_to_images = subparsers.add_parser("to-images", help="Convert a .docx file to images.")
    parser_to_images.add_argument("docx_file", help="The .docx file to convert.")
    parser_to_images.add_argument("output_prefix", help="The prefix for the output image files.")
    parser_to_images.set_defaults(func=to_images)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
