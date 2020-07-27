from setuptools import setup, find_packages
import os
import pathlib
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def load_version():
    version_file = os.path.join(os.path.dirname(
        __file__), "src/GreenPonik_WaterPump_Driver", "version.py")
    version = {}
    with open(version_file) as fd:
        exec(fd.read(), version)
    return version["__version__"]


setup(
    name="greenponik-waterpump-driver",
    version=load_version(),
    author="GreenPonik SAS",
    author_email="contact@greenponik.com",
    description="GreenPonik WaterPump i2c driver Python3 on raspberry pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GreenPonik/GreenPonik_WaterPump_Driver",
    license="MIT",
    install_requires=["adafruit-circuitpython-tsl2561"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where='src'),  # Required
    package_dir={'': 'src'},  # Optional
    python_requires='>=3.6',
    project_urls={  # Optional
        'Source': 'https://github.com/GreenPonik/GreenPonik_WaterPump_Driver/',
        'Bug Reports': 'https://github.com/GreenPonik/GreenPonik_WaterPump_Driver/issues',
    },
    keywords="GreenPonik hydroponics WaterPump i2c driver python hardware diy iot raspberry pi",
    py_modules=["GreenPonik_WaterPump_Driver"],
)
