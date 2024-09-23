from setuptools import find_packages, setup

setup(
    name="alegra",
    packages=find_packages(include=["alegra", "alegra.*"]),
    version="0.1.0",
    description="Python SDK for Alegra API",
    author="Luis Martinez",
    install_requires=[
        "pydantic[email]==2.8.2",
        "requests==2.32.3",
        "httpx==0.27.2",
    ],
    test_suite="tests",
    python_requires=">=3.6",
)
