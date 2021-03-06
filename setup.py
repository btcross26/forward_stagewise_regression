"""Package setup file."""

from pathlib import Path

from setuptools import find_packages, setup

# Core package components and metadata

NAME = "genestboost"
EMAIL = "btcross26@yahoo.com"
PACKAGES = find_packages()
KEYWORDS = [""]
DESCRIPTION = "Generic estimator boosting"
LONG = "Generic boosting framework for any regression estimator"

PROJECT_URLS = {
    "Documentation": (
        "https://github.com/pages/btcross26/genestboost/build/html/index.html"
    ),
    "Bug Tracker": "https://github.com/btcross26/genestboost/issues",
    "Source Code": "https://github.com/btcross26/genestboost",
}

CLASSIFIERS = [
    "Intended Audience :: Everyone",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.7",
]

INSTALL_REQUIRES = [
    "numpy==1.*,>=1.18.5",
    "scipy==1.*,>=1.4.1",
    'typing-extensions; python_version == "3.7"',
]

HERE = Path(__file__).absolute().parent
VERSION = "0.1.0"
URL = PROJECT_URLS["Source Code"]
AUTHORS = (HERE / "AUTHORS").read_text().split("\n")
LICENSE = (HERE / "LICENSE.txt").read_text()


def install_pkg():
    """Configure the setup for the package."""
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG,
        url=URL,
        project_urls=PROJECT_URLS,
        author=AUTHORS,
        maintainer=AUTHORS[0],
        license=LICENSE,
        python_requires=">=3.7.0",
        packages=PACKAGES,
        install_requires=INSTALL_REQUIRES,
        classifiers=CLASSIFIERS,
        include_package_data=True,
        zip_safe=False,
    )


if __name__ == "__main__":
    install_pkg()
