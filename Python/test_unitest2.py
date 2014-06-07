
import unittest
class ToRomanBadInput(unittest.TestCase):
	def test_too_large(self):
		self.assertRaises(roman1.OutOfRangeError,roman1.to_roman,4000)
