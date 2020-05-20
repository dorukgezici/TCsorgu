from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TCsorgu",
    version="0.3",
    description="Checks tckimlik.nvi.gov.tr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/dorukgezici/TCsorgu",
    author="Doruk Gezici",
    author_email="dorukgezici@gmail.com",
    license="MIT",
    packages=["TCsorgu"],
    install_requires=["requests"],
    scripts=["bin/TCsorgu"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
