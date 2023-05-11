from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hyparam",
    description="Container for hyper parameter tuning in machine learning. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="Christopher E. Mower",
    author_email="christopher.mower@kcl.ac.uk",
    url="https://github.com/cmower/hyparam",
    packages=["hyparam"],
    license="GNU General Public License v3.0",
    # entry_points={
    #     "console_scripts": [
    #         "hyparam = hyparam.main:main",
    #     ],
    # },
    project_urls={
        "Homepage": "https://cmower.github.io/hyparam/",
        "Bug Tracker": "https://github.com/cmower/hyparam/issues",
        "Source": "https://github.com/cmower/hyparam",
    },
    # install_requires=[],
)
