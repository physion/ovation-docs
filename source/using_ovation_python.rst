***************************
Using the Python client API
***************************

The Ovation Python API wraps the Ovation Java API for use with CPython. Through this Python API, Python users can access the full functionality of the Ovation ecosystem.

Requirements
============

* Java 1.6+
* Python 2.7.x
* `SciPy <http://scipy.org>`_ 0.13+

Physion recommends the `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ Python distribution.


Installation
============

Install the `ovation` package from `PyPI <http://pypi.python.org>`_:

	easy_install ovation


Usage
=====


1. Load the Ovation package::

    from ovation.connection import connect
    
2. Open a new `DataContext` with the `connect` function::

    context = connect('EMAIL')

where `EMAIL` is the email registered with your `ovation.io <http://ovation.io>`_ account.