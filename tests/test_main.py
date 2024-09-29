import unittest
from main import add

class TestMain(unittest.TestCase):
	def testadd(self):
		self.assertEqual(add(1,2),3)
		self.assertEqual(add(-1,1),0)
		self.assertEqual(add(0,0),0)

if __name__=="__main__":
	unittest.main()