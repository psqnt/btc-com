import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="btc-dot-com-api-wrapper",
    version="0.0.1",
    author="Joe Pasquantonio",
    author_email="joepasquantonio@gmail.com",
    description="An api wrapper for btc.com block explorer api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pasquantonio/",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
