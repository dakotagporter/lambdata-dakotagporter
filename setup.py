"""lambdata - a collection of helper functions"""

import setuptools ## from standard library

REQUIRED = [
    "numpy",
    "pandas"
]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='lambdata-dakotagporter',
    version='0.0.1',
    author='dakotagporter',
    author_email='dakotap3045@gmail.com',
    description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/dakotagporter/lambdata-dakotagporter',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
