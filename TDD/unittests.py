import classes
import unittest

class TestSword(unittest.TestCase):

	def test_inconsistentlength (self) :
		self.assertRaises(SwordLengthException, Sword, 100, 10, 1000, 'Steal', -1)
	def test_power100x4(self) :
		self.assertEqual((Sword(100, 10, 1000, 'Steal', 4)).power(), 100*4, "Should be 400")
	def test_power200x4(self) :
		self.assertEqual((Sword(200, 10, 1000, 'Steal', 4)).power(), 200*4, "Should be 800")
	def test_power200x2(self) :
		self.assertEqual((Sword(100, 10, 1000, 'Steal', 2)).power(), 100*2, "Should be 200")
	def test_power100x2(self) :
		self.assertEqual((Sword(200, 10, 1000, 'Steal', 2)).power(), 100*4, "Should be 400")

class TestBow(unittest.TestCase):

	def test_inconsistent_number_of_arrow (self) :
		self.assertRaises(BowArrowsException, Bow, 10, 100, 100, 50, -10)
	def test_power100x4(self) :
		self.assertEqual((Bow(10, 100, 100, 50, 500)).power(), 10*50, "Should be 500")
	def test_power200x4(self) :
		self.assertEqual((Bow(10, 100, 100, 0, 500)).power(), 0, "Should be 0")
	def test_power200x2(self) :
		self.assertEqual((Bow(0, 100, 100, 50, 500)).power(), 0, "Should be 0")
	def test_power100x2(self) :
		self.assertEqual((Bow(50, 100, 100, 10, 500)).power(), 10*50, "Should be 500")

if __name__ == '__main__':
	unittest.main()

