#Import the libraries
import unittest

#Import TASK5.py as prog
import TASK5 as prog
class TASK8(unittest.TestCase):
    #Function to test task5 url
    def test_EngineType(self):
        task5 = prog.TASK5
        #Checking the url of TASK5.py
        self.assertEqual(task5.url, 'http://192.168.253.129/algenius')

if __name__ == '__main__':
    unittest.main()
