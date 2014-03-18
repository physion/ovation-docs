***************************
Using the Python client API
***************************

The Ovation Python API wraps the Ovation Java API for use with CPython. Through this Python API, Python users can access the full functionality of the Ovation ecosystem.

Requirements
============

* `Java <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_ 1.6+
* `Python <https://www.python.org/downloads/>`_ 2.7.x
* `SciPy <http://scipy.org>`_ 0.13+
* `Pandas <http://pandas.pydata.org>`_ 0.11.0+
* `Phyjnius <https://pypi.python.org/pypi/phyjnius>`_ 1.2.1+

Physion recommends the `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ Python distribution.


Installation
============

Install the `ovation` package from `PyPI <http://pypi.python.org>`_ using `pip`::

	pip install ovation


Usage
=====


1. Load the Ovation package::

    from ovation.connection import new_data_context
    
2. Open a new `DataContext` with the `connect` function::

    context = new_data_context('<EMAIL>')

where `<EMAIL>` is the email registered with your `ovation.io <http://ovation.io>`_ account.