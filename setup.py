from setuptools import find_packages, setup

setup(
    name="alegra-e-provider",
    packages=find_packages(include=["alegra", "alegra.*"]),
    version="0.0.1",
    description="Alegra E-Provider, Python Wrapper for Alegra Electronic Provider API",
    long_description=open("README.md").read(),
    author="Luis Martinez",
    install_requires=[
        "pydantic[email]==2.8.2",
        "requests==2.32.3",
        "httpx==0.27.2",
    ],
    test_suite="tests",
    python_requires=">=3.6",
)
