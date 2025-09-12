import pytest
from BE.calculator_helper import CalculatorHelper

class TestCalculator:
    def setup_method(self):
        self.calculator = CalculatorHelper()

    def teardown_method(self):
      self.calculator = None

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 2, 4),      
            (3, -3, 0),    
            (5, 2, 7),     
        ]
    )
    def test_addition(self, a, b, expected):
        value = self.calculator.add(a, b)
        assert value == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 2, 3),
            (2, 5, -3),
            (0, 3, -3),
        ]
    )
    def test_subtraction(self, a, b, expected):
        value = self.calculator.subtract(a, b)
        assert value == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (3, 3, 9),
            (2, -4, -8),
            (0, 5, 0),
        ]
    )
    def test_multiplication(self, a, b, expected):
        value = self.calculator.multiply(a, b)
        assert value == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (6, 3, 2),
            (9, -3, -3),
            (0, 5, 0),
        ]
    )
    def test_division(self, a, b, expected):
        value = self.calculator.divide(a, b)
        assert value == expected

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(5, 0)
