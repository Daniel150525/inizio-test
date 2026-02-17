import unittest
from app import get_results

class TestGetResult(unittest.TestCase):

    def test_results_length(self):
        keyword = "Python"
        results = get_results(keyword)
        self.assertEqual(len(results), 3)

    def test_results_structure(self):
        keyword = "Python"
        results = get_results(keyword)
        for item in results:
            self.assertIsInstance(item,dict)
            self.assertIn("title", item)    
            self.assertIn("url", item)    
        
    def test_keyword_in_title(self):
        keyword = "Python"
        results = get_results(keyword)
        for i, item in enumerate(results, start=1):
            self.assertIn(keyword, item["title"])
            self.assertIn(str(i), item["title"])

if __name__=="__main__":
    unittest.main()
    