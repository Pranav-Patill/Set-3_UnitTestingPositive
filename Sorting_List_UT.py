from operator import itemgetter
import unittest

def sortDicList1(DL):
    return (sorted(DL,key=itemgetter("model"),reverse=True))

dict_list= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print(sortDicList1(dict_list))

class TestsortDicList1(unittest.TestCase):
    
    def setUp(self):
        self.dict_list= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

    # funtion name shoud always start with 'test'
    def test_sortDicList1(self):
        self.assertEqual(
            sortDicList1(self.dict_list),
            [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
            )
        
if (__name__ == '__main__'):
    unittest.main()