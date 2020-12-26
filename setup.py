import sys
from setuptools import setup, find_packages

from spinglass.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="spinglass",
    version=VERSION,
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="mit",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "standardmodel@git+https://github.com/terminal-labs/standardmodel.git",
    ],
    entry_points="""
        [console_scripts]
        spinglass=spinglass.cli:main
     """,
)