from os import path

from setuptools import find_packages, setup

current_dir = path.abspath(path.dirname(__file__))

setup(
    name="uber-popug-schemas",
    version="1.0",
    description="Schema registry for UberPopugInc",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/DmitryGubich/UberPopugIncSchemas",
    python_requires=">=3.9",
    packages=find_packages("app/"),
    include_package_data=True,
    platforms=["any"],
)
