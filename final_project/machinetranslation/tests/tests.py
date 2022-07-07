import unittest

from translator import EnglishToFrench, FrenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(EnglishToFrench("Hello"),"Bonjour")
    def test2(self):    
        self.assertEqual(EnglishToFrench("Hi how are you"),"Salut comment tu es")
  #  def test3(self):
  #      self.assertEqual(EnglishToFrench(""),"")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(FrenchToEnglish("Bonjour"),"Hello")
    def test2(self):    
        self.assertEqual(FrenchToEnglish("Salut comment tu es"),"Hi how you are")
   # def test3(self):
    #    self.assert(FrenchToEnglish(""),"")

unittest.main()
