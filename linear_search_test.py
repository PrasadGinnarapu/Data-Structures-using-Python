import unittest
from linear_search import *

class TestCardSearch(unittest.TestCase):
        
    def test_emptyList(self):
        self.assertEqual(locate_card(1,[]),-1)
    
    def test_occureAtFirst(self):
        self.assertEqual(locate_card(1,[1,2,3,4,5]),0)
    
    def test_occureAtLast(self):
        lst = [1,2,3,4,5]
        n = len([1,2,3,4,5])
        self.assertEqual(locate_card(5,lst),n-1)
        
    def test_singleElement(self):
        self.assertEqual(locate_card(4,[4]),0)
        
    def test_isInList(self):
        self.assertEqual(locate_card(4,[1,2,3,4]),3)
    
    def test_isNotinList(self):
        self.assertEqual(locate_card(8,[1,2,3,4]),-1)
        
    def test_repeatElements(self):
        self.assertEqual(locate_card(1,[1,2,3,3,4,4]),0)
    
    def test_repeatQuery(self):
        self.assertEqual(locate_card(1,[1,1,2,3,3,4,4]),0) #return 1st occurence
        
if __name__ == '__main__':
    unittest.main()
    

    
#in an interview  5 Test cases are good enough