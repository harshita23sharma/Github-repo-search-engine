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
        self.assertEqual([u'blocksig.c', u'signal.c'],a)

    def test_result_search(self):
        q_param = "struct linger nolinger"
        a,b = load_search.find_file(q_param)
        self.assertEqual("  \t  struct      ebmb_node node    \t  struct      eb64_node val    \t  struct      eb32_node *n    \t  struct      eb32_node *n    \t  struct      timer *t = NULL    \t  struct      url_stat *ustat = NULL   f < 5; f++) {  \t  struct      eb32_node *n   f < 5; f++) {  \t  struct      eb32_node *next    \t  struct      srv_st *srv    \t  struct      ebmb_node *srv_node    \t  struct      ebpt_node *ebpt_old    \t  struct      ebpt_node *ebpt_old",str(b))

    def test_random_search(self):
        q_param = "fcwer"
        a,b = load_search.find_file(q_param)
        self.assertEqual('[InvalidDocument("Cannot encode object: KeyError(\'the label [fcwer] is not in the [index]\',)",)]',str(a))

if __name__ == '__main__':
    unittest.main() 
    # run_all_tests 