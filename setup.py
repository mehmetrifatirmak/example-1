import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addition", # Replace with your own username
    version="0.0.1",
    author="M.R.I. ",
    author_email="mehmet.r.river@gmail.com",
    description="A small example package as learning publication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)