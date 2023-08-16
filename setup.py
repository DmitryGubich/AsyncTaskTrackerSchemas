from setuptools import setup

setup(
    name="uber-popug-events",
    version="1.2",
    description="Schema registry for UberPopugInc",
    long_description_content_type="text/markdown",
    url="https://github.com/DmitryGubich/UberPopugIncSchemas",
    python_requires=">=3.9",
    packages=["uber-popug-events"],
    install_requires=["jsonschema"],
    license="MIT",
    platforms=["any"],
)
