import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="swid-lint",
    version="0.0.1",
    description="Experimental SWID validator for baseline.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sthagen/silver-pancake",
    author="Stefan Hagen",
    author_email="stefan@hagen.link",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="software-bill-of-materials validation swid baseline extension development",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "jsonschema",
        "xmlschema"
    ],
    entry_points={
        "console_scripts": [
            "swid-lint=swid_lint.cli:main",
        ]
    },
)
