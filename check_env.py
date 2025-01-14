""" Run this file to check your python installation.
"""

def test_import_pandas():
    import pandas


def test_pandas_version():
    import pandas
    version_found = pandas.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found > (0, 15)


def test_import_numpy():
    import numpy


def test_import_matplotlib():
    import matplotlib


def test_scrape_web():
    import pandas as pd
    pd.read_html("http://en.wikipedia.org/wiki/World_population")


if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__name__)
