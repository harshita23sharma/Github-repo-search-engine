import unittest
import load_search

class TestBasic(unittest.TestCase):
    "Basic tests"

    
    def test_basic(self):
        a = 1
        assert a == 1
     
    def test_search(self):
        q_param = "SIG_SETMASK"
        a,b = load_search.find_file(q_param)
        self.assertEqual("flags.c",a)



# def run_all_tests():
#     unittest.main() 

if __name__ == '__main__':
    unittest.main() 
    # run_all_tests 