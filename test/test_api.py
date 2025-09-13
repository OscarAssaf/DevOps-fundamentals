import pytest
import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse





class TestCalculatorAPI():
    def test_add_api(self):
        url = "http://localhost:5000/calculate"
        payload = {
            "operation": "add",
            "operand1": 5,
            "operand2": 5
        }
        response = requests.post(url, json=payload)
        
        

        def test_generated_code(self):
            client = Client(base_url="http://localhost:5000")
            response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=5, operand2=4))
            assert isinstance(response, ResultResponse)
            assert response.result == 3


"""
class TestCalculatorAPI:
    
    @pytest.mark.parametrize(
        "operand1, operand2, expected",
        [
            (5, 4, 9),
            (3, 7, 10),
        ]
    )
    def test_add_generated_code(self, operand1, operand2, expected):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client=client, body=Calculation(Opertions.ADD, operand1=operand1, operand2=operand2))
        assert isinstance(response, ResultResponse)
        assert response.result == expected

    @pytest.mark.parametrize(
        "operand1, operand2, expected",
        [
            (10, 3, 7),
            (8, 5, 3),
        ]
    )
    def test_subtract_generated_code(self, operand1, operand2, expected):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client=client, body=Calculation(Opertions.SUBTRACT, operand1=operand1, operand2=operand2))
        assert isinstance(response, ResultResponse)
        assert response.result == expected

    @pytest.mark.parametrize(
        "operand1, operand2, expected",
        [
            (4, 3, 12),
            (2, 6, 12),
        ]
    )
    def test_multiply_generated_code(self, operand1, operand2, expected):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client=client, body=Calculation(Opertions.MULTIPLY, operand1=operand1, operand2=operand2))
        assert isinstance(response, ResultResponse)
        assert response.result == expected

    @pytest.mark.parametrize(
        "operand1, operand2, expected",
        [
            (12, 3, 4),
            (15, 5, 3),
        ]
    )
    def test_divide_generated_code(self, operand1, operand2, expected):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client=client, body=Calculation(Opertions.DIVIDE, operand1=operand1, operand2=operand2))
        assert isinstance(response, ResultResponse)
        assert response.result == expected
"""
        
"""
        class TestCalculatorAPI():
    def test_add_api(self):
        url = "http://localhost:5000/calculate"
        payload = {
            "operation": "add",
            "operand1": 5,
            "operand2": 5
        }
        response = requests.post(url, json=payload)
        
        

        def test_generated_code(self):
            client = Client(base_url="http://localhost:5000")
            response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=5, operand2=4))
            assert isinstance(response, ResultResponse)
            assert response.result == 3
 """