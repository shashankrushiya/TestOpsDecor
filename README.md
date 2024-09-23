# TestOpsDecor

TestOpsDecor is a Python package that enhances your test automation capabilities with custom decorators. It provides decorators for retrying tests, caching results, timeout management, and more.

## Installation

```bash
pip install testopsdecor
```

## Usage

**Example for @retry_on_exception Decorator**

```bash
from testopsdecor.decorator import retry_on_exception

@retry_on_exception(ValueError, retries=3, delay=2)
def flaky_test():
    # Test logic here
```

## See more examples in the documentation.