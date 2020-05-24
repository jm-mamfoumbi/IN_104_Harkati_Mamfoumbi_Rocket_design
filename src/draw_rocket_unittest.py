import unittest
import draw_rocket
import tkinter as tk

window = tk.Tk()
drawer = draw_rocket.Drawer(window)

class TestDeleteAll(unittest.TestCase):
	def test_emptylist(self):
		drawer.delete_all()
		self.assertEqual(drawer.rockets, [], "Should be empty")
	def test_index(self):
		drawer.delete_all()
		self.assertEqual(drawer.r_index, -1, "Should be -1")
		
class TestSelectIndex(unittest.TestCase):
	def test_empty_list_index(self):
		drawer.delete_all()
		drawer.select(2)
		self.assertEqual(drawer.r_index, -1, "Should be -1")

class TestSelectNext(unittest.TestCase):
	def test_empty_list_index(self):
		drawer.delete_all()
		drawer.select_next(1)
		self.assertEqual(drawer.r_index, -1, "Should be -1")
    	

if __name__ == '__main__':
	unittest.main()
