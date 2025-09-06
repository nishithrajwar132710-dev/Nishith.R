

# setup.py
# This file tells Python how to build our package
from setuptools import setup, find_packages

setup(
    name="signal_ICT_Nishith_92400133168",  # Name of the package
    version="0.1",                            # Version number
    packages=find_packages(),                  # Automatically find modules
    install_requires=["numpy", "matplotlib"], # Dependencies
    description="Custom Python package for signals and operations",
    author="Nishith Rajwar",
    author_email="nishith@example.com",
)
