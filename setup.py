import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="govpack-yarusx", # Replace with your own username
    version="0.2.1",
    author="Yaroslav Khoruzhenko",
    author_email="yarusx@gmail.com",
    description="A package that helps to create pandas variables from a public datasets: https://data.gov.ua/ ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThatAIGeek/govpack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['pandas', 'xlrd==1.2.0'],
)
