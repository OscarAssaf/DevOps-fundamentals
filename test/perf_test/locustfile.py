from locust import HttpUser, task, between
import json
import random

class CalculatorUser(HttpUser):
    #wait_time = between(2, 4)

    def check_operation(self, operation, operand1, operand2, expected):

        operations = {
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2
        }
        with self.client.post("/calculate", catch_response=True, name=operation, json=operations) as response:
            try:
                response_data = json.loads(response.text)
                if response_data.get('result') != expected:
                    response.failure(
                        f"Expected {expected} for {operation}({operand1}, {operand2}) "
                        f"but got {response_data.get('result')}"
                    )
            except Exception as e:
                response.failure(f"Invalid response: {e}")

    @task(2)  
    def add(self):
        test_cases = [[1, 1, 2], [2, 2, 4], [5, 10, 15], [7, 3, 10]]
        a, b, expected = random.choice(test_cases)
        self.check_operation("add", a, b, expected)

    @task(1)
    def subtract(self):
        test_cases = [[5, 2, 3], [10, 3, 7], [7, 7, 0], [20, 5, 15]]
        a, b, expected = random.choice(test_cases)
        self.check_operation("subtract", a, b, expected)

    @task(1)
    def multiply(self):
        test_cases = [[2, 2, 4], [3, 4, 12], [5, 6, 30], [10, 10, 100]]
        a, b, expected = random.choice(test_cases)
        self.check_operation("multiply", a, b, expected)

    @task(1)
    def divide(self):
        test_cases = [[4, 2, 2], [9, 3, 3], [20, 5, 4], [15, 3, 5]]
        a, b, expected = random.choice(test_cases)
        self.check_operation("divide", a, b, expected)


if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
