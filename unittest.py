import unittest 
class Testing(unittest.TestCase):
    def testingMethods(self):
        self.assertEqual('PostOffice'.isalpha(),'Postoffice')
    def test_string(self):
        self.assertFalse('Alankar@theatre'.isalpha())
unittest.main()