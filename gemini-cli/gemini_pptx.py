#!/usr/bin/env python3

import argparse
import os
from utils import run_command, get_skill_path

def extract_text(args):
    """Extracts text from a .pptx file."""
    pptx_file = args.pptx_file
    command = f"python3 -m markitdown {pptx_file}"
    print(f"Running: {command}")
    run_command(command)

def unpack(args):
    """Unpacks a .pptx file into its XML components."""
    pptx_file = args.pptx_file
    output_dir = args.output_dir
    script_path = os.path.join(get_skill_path('pptx'), 'ooxml/scripts/unpack.py')
    command = f"python3 {script_path} {pptx_file} {output_dir}"
    print(f"Running: {command}")
    run_command(command)

def pack(args):
    """Packs a directory of XML components into a .pptx file."""
    input_dir = args.input_dir
    output_file = args.output_file
    script_path = os.path.join(get_skill_path('pptx'), 'ooxml/scripts/pack.py')
    command = f"python3 {script_path} {input_dir} {output_file}"
    print(f"Running: {command}")
    run_command(command)

def thumbnails(args):
    """Generates thumbnails for a .pptx file."""
    pptx_file = args.pptx_file
    output_prefix = args.output_prefix if args.output_prefix else ''
    cols = args.cols
    script_path = os.path.join(get_skill_path('pptx'), 'scripts/thumbnail.py')
    command = f"python3 {script_path} {pptx_file} {output_prefix} --cols {cols}"
    print(f"Running: {command}")
    run_command(command)

def main():
    parser = argparse.ArgumentParser(description="A command-line interface for the pptx skill.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-parser for extract-text
    parser_extract_text = subparsers.add_parser("extract-text", help="Extract text from a .pptx file.")
    parser_extract_text.add_argument("pptx_file", help="The .pptx file to extract text from.")
    parser_extract_text.set_defaults(func=extract_text)

    # Sub-parser for unpack
    parser_unpack = subparsers.add_parser("unpack", help="Unpack a .pptx file.")
    parser_unpack.add_argument("pptx_file", help="The .pptx file to unpack.")
    parser_unpack.add_argument("output_dir", help="The directory to unpack the files into.")
    parser_unpack.set_defaults(func=unpack)

    # Sub-parser for pack
    parser_pack = subparsers.add_parser("pack", help="Pack a directory into a .pptx file.")
    parser_pack.add_argument("input_dir", help="The directory to pack.")
    parser_pack.add_argument("output_file", help="The output .pptx file.")
    parser_pack.set_defaults(func=pack)

    # Sub-parser for thumbnails
    parser_thumbnails = subparsers.add_parser("thumbnails", help="Generate thumbnails for a .pptx file.")
    parser_thumbnails.add_argument("pptx_file", help="The .pptx file to generate thumbnails for.")
    parser_thumbnails.add_argument("output_prefix", nargs='?', help="The output prefix for the thumbnail files.")
    parser_thumbnails.add_argument("--cols", type=int, default=5, help="Number of columns in the thumbnail grid.")
    parser_thumbnails.set_defaults(func=thumbnails)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
