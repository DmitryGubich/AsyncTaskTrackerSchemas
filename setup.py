from setuptools import find_packages, setup

setup(
    name="uber-popug-events",
    version="1.2",
    description="Schema registry for UberPopugInc",
    long_description_content_type="text/markdown",
    url="https://github.com/DmitryGubich/UberPopugIncSchemas",
    python_requires=">=3.9",
    packages=find_packages(),
    include_package_data=True,
    platforms=["any"],
)
