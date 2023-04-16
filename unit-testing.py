import unittest
from master import calculator
from unittest.mock import patch
from io import StringIO

class TestCalculator(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_addition(self, mock_stdout):
        user_input = ['5', '2', '1']  # Input values for the test
        with patch('builtins.input', side_effect=user_input):
            calculator()
            output = mock_stdout.getvalue().strip()
            expected_output = '7.0'
            self.assertEqual(output.endswith(expected_output),True, "Addition test failed")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_subtraction(self, mock_stdout):
        user_input = ['3', '2', '2']  # Input values for the test
        with patch('builtins.input', side_effect=user_input):
            calculator()
            output = mock_stdout.getvalue().strip()
            expected_output = '1.0'
            self.assertEqual(output.endswith(expected_output),True, "Subtraction test failed")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_Multiplication(self, mock_stdout):
        user_input = ['4', '4', '3']  # Input values for the test
        with patch('builtins.input', side_effect=user_input):
            calculator()
            output = mock_stdout.getvalue().strip()
            expected_output = '16.0'
            self.assertEqual(output.endswith(expected_output),True, "Multiplication test failed")

    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_Division(self, mock_stdout):
        user_input = ['4', '4', '4']  # Input values for the test
        with patch('builtins.input', side_effect=user_input):
            calculator()
            output = mock_stdout.getvalue().strip()
            expected_output = '1'
            self.assertEqual(output.endswith(expected_output),True, "Division test failed")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_Modulus(self, mock_stdout):
        user_input = ['5', '2', '5']  # Input values for the test
        with patch('builtins.input', side_effect=user_input):
            calculator()
            output = mock_stdout.getvalue().strip()
            expected_output = '1'
            self.assertEqual(output.endswith(expected_output),True, "Modulus test failed")
            

    
if __name__ == '__main__':
    unittest.main()