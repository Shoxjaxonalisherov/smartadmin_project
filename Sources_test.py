import unittest
from Sources import *
class AnyText(unittest.TestCase):
    def test_function_returns_text(self):
        result = gazeta_image()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

    def test_function_returns_text1(self):
        result = gazeta_news_text()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

    def test_function_returns_text2(self):
        result = gazeta_news_header()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

    def test_function_returns_text3(self):
        result = ria_news_header()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

    def test_function_returns_text4(self):
        result = ria_news_text()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

    def test_function_returns_text1(self):
        result = ria_news_image()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()