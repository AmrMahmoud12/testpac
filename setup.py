from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="AmrMahmoud12", # Replace with your own username
    version="0.0.1",
    author="amr mahmoud",
    author_email="ammah246@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmrMahmoud12/testpac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
