#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="univariate_linear_regression",
      version="0.1.0",
      description="Univariate linear regression of housing price against housing area",
      author="Dipankar Nath",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="nathdip@gmail.com",
      install_requires=["scikit-learn==0.22.2",
                        "pytest"
                        ],
      )
