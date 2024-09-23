import functools
import time
import logging
import signal
import random

class TimeoutException(Exception):
    pass

"""
@functools.wrap decorator is used to ensure 
the decorated function retains its original 
name and metadata.
"""


# Decorator 1: Retry Logic
def retry(retries=3, delay=1):
    """
    Retry the function if it raises an exception.

    Args:
        retries (int): Number of times to retry.
        delay (int): Delay between retries in seconds.
    """

    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    print(f"Attempt {attempt + 1} of {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, retrying in {delay} seconds...")
                    last_exception = e
                    time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator_retry


# Decorator 2: Logging
logging.basicConfig(level=logging.INFO)


def log_test(func):
    """
    Log the start and end of the test function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log start of the test
        logging.info(f"Starting test: {func.__name__}")
        try:
            # Execute the original test function
            result = func(*args, **kwargs)
            # Log success if no exception is raised
            logging.info(f"Test passed: {func.__name__}")
            return result
        except Exception as e:
            # Log failure if an exception occurs
            logging.error(f"Test failed: {func.__name__}, Error: {e}")
            raise

    return wrapper


# Decorator 3: Timing
def time_test(func):
    """
    Measure the time taken by the test function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting {func.__name__}...")

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Finished {func.__name__} in {end_time - start_time:.2f} seconds")

        return result

    return wrapper


# Decorator 4: Mark Test with Priority/Category
def mark_test(priority="low", category="general"):
    """
    Mark the test with custom metadata such as priority and category.

    Args:
        priority (str): The priority of the test.
        category (str): The category the test belongs to.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running {func.__name__} with priority: {priority}, category: {category}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Decorator 5: Add extra behavior before and after the test runs
def custom_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Add functionality before function call
        print(f"Before calling {func.__name__}")

        result = func(*args, **kwargs)  # Call the original function

        # Add functionality after function call
        print(f"After calling {func.__name__}")

        return result

    return wrapper


def timeout(seconds=10):
    """
    Timeout decorator to raise an exception if a test runs longer than the specified time.

    Args:
        seconds (int): The maximum number of seconds the test can run.
    """
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutException(f"Test {func.__name__} timed out after {seconds} seconds.")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)  # Set an alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Disable the alarm
            return result
        return wrapper
    return decorator


def retry_on_exception(exception, retries=3, delay=1):
    """
    Retry the function if a specific exception is raised.

    Args:
        exception (Exception): The exception to retry on.
        retries (int): Number of retry attempts.
        delay (int): Delay in seconds between retries.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    print(f"Retrying {func.__name__} due to {e}. Attempt {attempt + 1} of {retries}.")
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


def cache_results(func):
    """
    Cache the results of the function to avoid re-computation.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {func.__name__} with arguments {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def parameterize(arg_values):
    """
    Run the test with multiple sets of arguments.

    Args:
        arg_values (list of tuples): List of argument tuples to pass to the test function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for index, param in enumerate(arg_values):
                print(f"Running {func.__name__} with parameter set {index + 1}: {param}")
                func(*param)
        return wrapper
    return decorator


def retry_with_backoff(retries=3, delay=1, backoff=2):
    """
    Retry the function with exponential backoff.

    Args:
        retries (int): Number of retries.
        delay (int): Initial delay between retries in seconds.
        backoff (int): Factor by which to increase the delay.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay} seconds...")
                    last_exception = e
                    time.sleep(current_delay)
                    current_delay *= backoff
            raise last_exception
        return wrapper
    return decorator

