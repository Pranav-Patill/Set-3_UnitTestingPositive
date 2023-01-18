import unittest

def checkCondition(int_list):
    if(len(int_list)==8):
        if(int_list.count(int_list[4])==3):
            return "True"
        else:
            return "False"
    else:
        return "False"

# Unit testing
class TestCheckCondition(unittest.TestCase):
    
    def setUp(self):
        self.list_True=[19, 19, 15, 3, 5, 5, 5, 2]
        self.list_FLength=[19, 19, 5, 5, 5]
        self.list_FOccurence=[19, 15, 3, 5, 5, 6 ,2, 9]

    # funtion name shoud always start with 'test'
    def test_checkCondition(self):
        self.assertEqual(checkCondition(self.list_True),"True") #All condition check
        self.assertEqual(checkCondition(self.list_FLength),"False") #length check
        self.assertEqual(checkCondition(self.list_FOccurence),"False") # Occurance check

if (__name__ == '__main__'):
    unittest.main()