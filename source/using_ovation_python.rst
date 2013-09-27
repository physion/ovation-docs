****************************
Using the Python client API
****************************

The Ovation Python API wraps the Ovation Java API for use with Python 2.7+. Through this Python API, users can access the full functionality of the Ovation platform within Python.



Requirements
============

* Java 1.6+
* Python 2.7


Installation
============

Physion recommends the `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ Python distribution for scientific computing. Anaconda comes with necessary scientific and numeric computing tools ready to go. If you already have a working Python installation, continue with instructions for :ref:`sub-standard-python-install` below. If you do not already have a working Python installation, or you wish to use Anaconda, continue with instructions for :ref:`sub-anaconda-install`:

.. _sub-anaconda-install:

Anoconda
********

1. `Download <https://store.continuum.io/cshop/anaconda/>`_ and install Anaconda (`instructions <http://docs.continuum.io/anaconda/index.html>`_).

2. Create a new environment using `conda`::

    $ conda create -n ovation python=2.7 numpy=1.7 ovation
    
3. Activate the `ovation` environment::

    $ source activate ovation


.. _sub-standard-python-install:

Standard Python
***************

1. easy_install

2. Install the Ovation API::

    $ easy_install ovation
