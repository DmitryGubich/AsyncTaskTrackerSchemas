from os import path

from setuptools import find_packages, setup

current_dir = path.abspath(path.dirname(__file__))

setup(
    name="uber-popug-events",
    version="1.5",
    description="Provides client that can make requests to Enett",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/DmitryGubich/UberPopugIncSchemas",
    python_requires=">=3.9",
    packages=find_packages(),
    include_package_data=True,
    platforms=["any"],
)
