import unittest
from unittest.mock import patch
import original_file
from original_file import language_l1
from original_file import language_l2

class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=['a','b','aba', 'q'])
    def test_language(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l1()
        self.assertEqual(result,'True')

    @patch('builtins.input', side_effect=['a','b','abb', 'q'])
    def test_language_false(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l1()
        self.assertEqual(result,'False')
    
    @patch('builtins.input', side_effect=['a','b','abbcc', 'q'])
    def test_language1_invalid(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l1()
        self.assertEqual(result,'Invalid')


    @patch('builtins.input', side_effect=['a','b','ababab', 'q'])
    def test_language2(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l2()
        self.assertEqual(result,'True')

    @patch('builtins.input', side_effect=['a','b','baaaba', 'q'])
    def test_language2_false(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l2()
        self.assertEqual(result,'False')

    @patch('builtins.input', side_effect=['a','b','baaabaxxx', 'q'])
    def test_language2_invalid(self, m_input):
        # m_input.side_effect = [1,'a','b','aba', 'q']
        result = language_l2()
        self.assertEqual(result,'Invalid')


    

unittest.main()