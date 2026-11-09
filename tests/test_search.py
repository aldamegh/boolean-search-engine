import unittest
import tempfile
from pathlib import Path
from search_engine import create_index, boolean_search, load_dataset

class BooleanSearchTests(unittest.TestCase):
    def setUp(self):
        self.index = create_index(["apple tv apple", "samsung tv", "sony tv", "apple samsung", ""])
    def test_unique_postings(self): self.assertEqual(self.index['apple'],[0,3])
    def test_or(self): self.assertEqual(boolean_search('apple sony',self.index),[0,2,3])
    def test_and(self): self.assertEqual(boolean_search('apple&tv',self.index),[0])
    def test_precedence(self): self.assertEqual(boolean_search('samsung sony&tv',self.index),[1,2,3])
    def test_other_precedence(self): self.assertEqual(boolean_search('samsung&sony tv',self.index),[0,1,2])
    def test_and_spaces(self): self.assertEqual(boolean_search('apple & tv',self.index),[0])
    def test_case(self): self.assertEqual(boolean_search('APPLE',self.index),[0,3])
    def test_unknown(self): self.assertEqual(boolean_search('missing&apple',self.index),[])
    def test_empty(self): self.assertEqual(boolean_search(' ',self.index),[])
    def test_malformed(self):
        for query in ['&apple','apple&','apple&&tv']:
            with self.assertRaises(ValueError): boolean_search(query,self.index)
    def test_empty_index(self): self.assertEqual(boolean_search('apple',create_index([])),[])
    def test_jsonl(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'synthetic.jsonl';p.write_text('{"short_description":"synthetic text"}\n',encoding='utf-8')
            self.assertEqual(load_dataset(p),['synthetic text'])

if __name__ == '__main__': unittest.main()
