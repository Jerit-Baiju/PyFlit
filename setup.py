from distutils.core import setup

import setuptools


def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README

# url"https://github.com/Jerit-Baiju/PyFlict"


setup(
    name="pyflit",
    packages=setuptools.find_packages(),
    version="2.1",
    license="MIT",
    description="PyFlit provides you to add components, pages, and it has many other features.",
    author="Jerit Baiju",
    author_email="jeritalumkal@gmail.com",
    keywords=["add page", "addpage", "add_page",
              "add component", "addcomponent", "add_component"],
    install_requires=["flask"],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
