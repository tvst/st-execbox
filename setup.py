import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="st-execbox",
    version="1.0.0",
    author="Thiago Teixeira",
    author_email="me@thiagot.com",
    description="An editable text box for executing Python code live",
    license="Apache 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tvst/st-execbox",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=["streamlit", "streamlit-ace"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
