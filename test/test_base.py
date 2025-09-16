from BE.calculator_helper import CalculatorHelper

class BaseTest:
    @classmethod
    def setup_class(cls):
        """Setup any state specific to the execution of the given class."""
        cls.calculator = CalculatorHelper()

    @classmethod
    def teardown_class(cls):
        """Teardown any state that was previously setup with a call to setup_class."""
        cls.calculator = None
