from setuptools import setup, find_packages

setup(
    name="df_in_browser",
    version="0.1.0",
    author="Peter Rush",
    description="A simple python package for rendering a Pandas DataFrame in a browser.",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
    "pandas",
    "aspose-words"
    ],
)
