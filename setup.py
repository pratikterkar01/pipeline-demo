from setuptools import setup,find_packages

setup(name="census-income",
       version="0.0.1",
       author="pratik",
       author_email="pratikterkar@gmail.com",
       pakages=find_packages(),
       install_requires=["pandas","numpy","flask"]
       )