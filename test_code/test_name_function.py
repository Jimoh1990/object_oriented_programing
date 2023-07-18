import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Test for 'name_funtion.py'. """
    
    def test_first_last_name(self):
        """ Do names like 'jimoh sikiru' work? """
        formatted_name = get_formatted_name('jimoh','sikiru')
        self.assertEqual(formatted_name, 'Jimoh Sikiru')

    def test_first_last_middle_name(self):
        """ Do names like 'jimoh adebayo sikiru' work? """
        formatted_name = get_formatted_name('jimoh', 'adebayo', 'sikiru')
        self.assertEqual(formatted_name, 'Jimoh Sikiru Adebayo')

if __name__ == '__main__':
    unittest.main()
