import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deui",
    version="1.0.0",
    author="Yuta Urushiyama",
    author_email="aswif10flis1ntkb@gmail.com",
    description="Declarative UI Wrapper Framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/urushiyama/deui",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
    install_requires=[
        "watchdog",
    ],
    include_package_data=True,
)
