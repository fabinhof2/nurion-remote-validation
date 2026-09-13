import pathlib
import unittest


class Mission24BValidationTest(unittest.TestCase):
    def test_marker_file_exists(self):
        marker = pathlib.Path(__file__).with_name('mission24b.txt')
        self.assertIn('NURION Mission 24B merge validation.', marker.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
