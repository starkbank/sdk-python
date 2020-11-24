from re import search
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('starkbank/__init__.py') as f:
    version = search(r'version = \"(.*)\"', f.read()).group(1)

setup(
    name="starkbank",
    packages=find_packages(),
    include_package_data=True,
    description="SDK to facilitate Python integrations with Stark Bank",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/starkbank/sdk-python",
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["stark bank", "starkbank", "sdk", "open banking", "openbanking", "banking", "open", "stark"],
    version=version,
    install_requires=[
        "requests>=2.23.0",
        "starkbank-ecdsa~=1.0.0",
    ],
)
