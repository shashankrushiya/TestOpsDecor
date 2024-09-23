import time

from custom_decorator.decorators import *


# Test with retry logic
@retry(retries=5, delay=2)
def test_flaky_api():
    response = call_some_api()  # Add functionality for calling any API
    assert response.status_code == 200


# Test with logging
@log_test
def test_example():
    assert 1 + 1 == 2


# Test with timing
@time_test
def test_slow_function():
    time.sleep(5)  # Simulating a slow test
    assert True


# Test with priority and category marking
@mark_test(priority="high", category="login")
def test_login_functionality():
    assert login_user() == "success"  # Add functionality for logging in user


# Example for timeout
@timeout(seconds=5)
def test_long_running():
    time.sleep(6)  # This will trigger the timeout after 5 seconds


# Example for retry_on_exception
@retry_on_exception(ValueError, retries=3, delay=1)
def test_flaky_function():
    if random.choice([True, False]):
        raise ValueError("Random failure!")
    print("Test passed")


# Example for cache_results
@cache_results
def test_expensive_computation(x, y):
    time.sleep(2)  # Simulating a time-consuming function
    return x + y


# Example for parameterize
@parameterize([(1, 2), (2, 3), (3, 4)])
def test_addition(a, b):
    print(f"Testing: {a} + {b} = {a + b}")


# Example for retry_with_backoff
@retry_with_backoff(retries=3, delay=1, backoff=2)
def test_retry_with_backoff():
    if random.choice([True, False]):
        raise ConnectionError("Flaky server issue!")
    print("Test succeeded after retries")