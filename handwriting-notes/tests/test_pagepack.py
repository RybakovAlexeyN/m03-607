import importlib.util
import tempfile
import unittest
from pathlib import Path

script = Path(__file__).parents[1] / "scripts" / "pagepack.py"
spec = importlib.util.spec_from_file_location("pagepack", script)
pagepack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pagepack)

class PagePackTests(unittest.TestCase):
    def test_lossless_russian_content(self):
        text = ("2.1. Три кита СЭД\n\nСЭД — система электронного документооборота.\n\n" * 15)
        for size in (80, 100, 250, 500, 1300):
            pages = pagepack.paginate(text, size)
            self.assertEqual("".join(pages), text)
            self.assertTrue(all(len(p) <= size for p in pages))
    def test_no_changes_to_punctuation(self):
        text = "Зачем? ТМЦ → СЭД, Workflow Management; «Дело».\n\nА → Б\n\n"
        self.assertEqual("".join(pagepack.paginate(text, 80)), text)
    def test_page_of_long_unbroken_words(self):
        text = "абв" * 123 + "\n"
        self.assertEqual("".join(pagepack.paginate(text, 81)), text)
    def test_empty_and_short_limit(self):
        with self.assertRaises(ValueError): pagepack.paginate("", 1300)
        with self.assertRaises(ValueError): pagepack.paginate("тест", 40)
    def test_utf8_read(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "my.txt"
            p.write_bytes(b"\xef\xbb\xbf" + "тест\r\n123".encode())
            self.assertEqual(pagepack.read_source(p), "тест\n123")
    def test_hashes(self):
        self.assertNotEqual(pagepack.hash_text("тест"), pagepack.hash_text("тест!"))

if __name__ == "__main__":
    unittest.main()
