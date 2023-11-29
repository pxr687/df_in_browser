from setuptools import setup, find_packages

setup(
    name="show_in_browser",
    version="0.1.0",
    author="Peter Rush",
    description="A simple python package for rendering a Pandas DataFrames and matplotlib/plotly plots in a browser.",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
    "pandas",
    "aspose-words"
    ],
)
