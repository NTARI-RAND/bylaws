import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKOUT = Path(__file__).resolve().parent
SUITE = CHECKOUT / "bylaws-conformance-suite.py"


class ConformanceCLITests(unittest.TestCase):
    def run_suite(self, directory, *args):
        result = subprocess.run(
            [sys.executable, str(SUITE), *args],
            cwd=directory,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("RESULT: all checks PASS", result.stdout)
        return result.stdout

    def test_default_document_is_found_outside_the_checkout(self):
        expected = self.run_suite(CHECKOUT)
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(self.run_suite(directory), expected)

    def test_explicit_relative_document_is_found_from_the_callers_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            copy_dir = Path(directory) / "copy"
            copy_dir.mkdir()
            for source in CHECKOUT.glob("P1-001_Bylaws_v1.0*.md"):
                destination = source.name.replace("P1-001", "Copy", 1)
                shutil.copyfile(source, copy_dir / destination)
            shutil.copytree(CHECKOUT / "Historical Docs", copy_dir / "Historical Docs")

            output = self.run_suite(directory, "--doc", "copy/Copy_Bylaws_v1.0.md")
            self.assertIn("Bylaws conformance: Copy_Bylaws_v1.0.md", output)


if __name__ == "__main__":
    unittest.main()
