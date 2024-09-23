from setuptools import setup, find_packages

setup(
    name="TestOpsDecor",  # Package name
    version="0.1.0",
    packages=find_packages(),  # Automatically finds all packages and sub-packages
    install_requires=[
        "pytest>=6.0",  # Ensure pytest is installed, minimum version 6.0
        "allure-pytest",  # Include Allure Pytest for reporting
        "requests>=2.25",  # Requests library for API testing, version 2.25 or higher
        "logging",  # Standard Python logging library
    ],
    author="Shashank Rushiya",
    author_email="shashankrushiya@gmail..com",
    description="A package to enhance Python testing with custom decorators",
    url="https://github.com/yourusername/testenhancer",  # URL of the project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
