#!/usr/bin/env python3

import argparse
import os
from utils import run_command, get_skill_path

def recalc(args):
    """Recalculates all formulas in an .xlsx file."""
    xlsx_file = args.xlsx_file
    timeout = args.timeout
    script_path = os.path.join(get_skill_path('xlsx'), 'recalc.py')
    command = f"python3 {script_path} {xlsx_file} {timeout}"
    print(f"Running: {command}")
    run_command(command)

def main():
    parser = argparse.ArgumentParser(description="A command-line interface for the xlsx skill.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-parser for recalc
    parser_recalc = subparsers.add_parser("recalc", help="Recalculate all formulas in an .xlsx file.")
    parser_recalc.add_argument("xlsx_file", help="The .xlsx file to recalculate.")
    parser_recalc.add_argument("--timeout", type=int, default=30, help="The timeout in seconds for the recalculation.")
    parser_recalc.set_defaults(func=recalc)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
