import unittest
import os

class SimpleTest(unittest.TestCase): 
    
    def setUp(self):
        self.a = 10
        self.b = 20
    
    # Returns True or False.  
    def test(self):
        self.assertFalse(False)
        
    
    def test2(self):
        self.assertEqual("abc","abc")
    
    def tearDown(self):
        print("End of testcase",self.shortDescription)
  
unittest.main()
os.system("ping 5.5.5.5")
