import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import subprocess

# Add gemini-cli to the python path to import the scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gemini_pptx
import gemini_docx
import gemini_xlsx
import gemini_pdf
import utils

class TestGeminiCLI(unittest.TestCase):

    @patch('gemini_pptx.run_command')
    def test_gemini_pptx_extract_text(self, mock_run_command):
        args = MagicMock()
        args.pptx_file = 'test.pptx'
        gemini_pptx.extract_text(args)
        mock_run_command.assert_called_once_with('python3 -m markitdown test.pptx')

    @patch('gemini_pptx.run_command')
    def test_gemini_pptx_unpack(self, mock_run_command):
        args = MagicMock()
        args.pptx_file = 'test.pptx'
        args.output_dir = 'output'
        gemini_pptx.unpack(args)
        self.assertTrue(mock_run_command.call_args[0][0].endswith('unpack.py test.pptx output'))

    @patch('gemini_pptx.run_command')
    @patch('os.listdir')
    def test_gemini_pptx_create(self, mock_listdir, mock_run_command):
        mock_listdir.return_value = ['slide2.html', 'slide1.html', 'style.css']
        args = MagicMock()
        args.input_dir = 'html_slides'
        args.output_file = 'presentation.pptx'

        gemini_pptx.create(args)

        script_path = os.path.join(gemini_pptx.get_skill_path('pptx'), 'scripts/html2pptx.js')
        expected_command = f"node {script_path} presentation.pptx html_slides/slide1.html html_slides/slide2.html"
        mock_run_command.assert_called_once_with(expected_command)

    @patch('gemini_docx.run_command')
    def test_gemini_docx_extract_text(self, mock_run_command):
        args = MagicMock()
        args.docx_file = 'test.docx'
        args.output_file = 'output.md'
        args.track_changes = 'all'
        gemini_docx.extract_text(args)
        mock_run_command.assert_called_once_with('pandoc --track-changes=all test.docx -o output.md')

    @patch('gemini_xlsx.run_command')
    def test_gemini_xlsx_recalc(self, mock_run_command):
        args = MagicMock()
        args.xlsx_file = 'test.xlsx'
        args.timeout = 30
        gemini_xlsx.recalc(args)
        self.assertTrue(mock_run_command.call_args[0][0].endswith('recalc.py test.xlsx 30'))

    @patch('gemini_pdf.run_command')
    def test_gemini_pdf_extract_text(self, mock_run_command):
        args = MagicMock()
        args.pdf_file = 'test.pdf'
        args.output_file = 'output.txt'
        args.layout = True
        gemini_pdf.extract_text(args)
        mock_run_command.assert_called_once_with('pdftotext -layout test.pdf output.txt')

    @patch('subprocess.Popen')
    def test_run_command_security(self, mock_popen):
        # Test that the command is split correctly and shell=True is not used
        mock_process = MagicMock()
        mock_process.stdout.readline.return_value = ''
        mock_process.wait.return_value = 0
        mock_popen.return_value = mock_process

        utils.run_command('ls -l /tmp')
        mock_popen.assert_called_once_with(['ls', '-l', '/tmp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


if __name__ == '__main__':
    unittest.main()
