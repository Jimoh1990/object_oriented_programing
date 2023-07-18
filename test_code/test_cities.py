import unittest
from city_functions import city_name

class CityTestCase(unittest.TestCase):
    # To test a single unit

    def test_city_country(self):
        """ Do location like 'lagos, nigeria' work? """
        clean_location = city_name('lagos', 'nigeria')
        self.assertEqual(clean_location, 'Lagos, Nigeria')

    def test_city_country_population(self):
        clean_location = city_name('lagos', 'nigeria', 'population')
        self.assertEqual(clean_location, 'Lagos, Nigeria-Population 5000000')

if __name__ == '__main__':
    unittest.main()
