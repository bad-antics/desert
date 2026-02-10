import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from desert.core import DesertEngine

class TestDesert(unittest.TestCase):
    def test_explore(self):
        d=DesertEngine()
        r=d.explore("physical")
        self.assertIn("quote",r)
    def test_void(self):
        d=DesertEngine()
        r=d.void_index({"mass_media":True,"consumerism":True,"social_media":True,"simulation":True})
        self.assertEqual(r["state"],"Desert")
    def test_meditation(self):
        d=DesertEngine()
        self.assertIsInstance(d.generate_meditation(),str)

if __name__=="__main__": unittest.main()
