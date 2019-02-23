import unittest
from MIME_Type import *

class TestFindExtension(unittest.TestCase):

    def test_no_extension(self):
        fn = 'no_extension'
        self.assertEqual(find_extension(fn), 'UNKNOWN')

    def test_html(self):
        fn = 'test.html'
        self.assertEqual(find_extension(fn), 'html')

    def test_png(self):
        fn = 'portrait.png'
        self.assertEqual(find_extension(fn), 'png')

    def test_txt(self):
        fn = 'doc.TXT'
        self.assertEqual(find_extension(fn), 'txt')

class TestFindMIMEType(unittest.TestCase):

    def test_unknown(self):
        ext = 'UNKNOWN'
        mime_dict = {'html': 'text/html', 'png': 'image/png'}
        self.assertEqual(find_mime_type(ext, mime_dict), 'UNKNOWN')

    def test_no_extension_found(self):
        ext = 'jpg'
        mime_dict = {'html': 'text/html', 'png': 'image/png'}
        self.assertEqual(find_mime_type(ext, mime_dict), 'UNKNOWN')

    def test_png(self):
        ext = 'png'
        mime_dict = {'html': 'text/html', 'png': 'image/png'}
        self.assertEqual(find_mime_type(ext, mime_dict), 'image/png')

if __name__ == '__main__':
    unittest.main()
