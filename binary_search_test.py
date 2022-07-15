import unittest
from binary_search import *

class TestCardSearch(unittest.TestCase):
        
    def test_emptyList(self):
        self.assertEqual(locate_card(1,[]),-1)        
    
    def test_occureAtFirst(self):
        self.assertEqual(locate_card(5,[5,4,3,2,1]),0)
    
    def test_occureAtLast(self):
        lst = [5,4,3,2,1]
        n = len(lst)
        self.assertEqual(locate_card(1,lst),n-1)
        
    def test_singleElement(self):
        self.assertEqual(locate_card(4,[4]),0)       
        
    def test_isInList(self):
        self.assertEqual(locate_card(2,[5,4,3,2,1]),3)
    
    def test_isNotinList(self):
        self.assertEqual(locate_card(8,[5,4,3,2,1]),-1)
        
    def test_repeatElements(self):
        self.assertEqual(locate_card(1,[5,5,4,4,3,2,1]),6)
    
    def test_repeatQuery(self):
        self.assertEqual(locate_card(1,[5,5,4,3,2,1,1]),5) #return 1st occurence
        
if __name__ == '__main__':
    unittest.main()
    
    
    