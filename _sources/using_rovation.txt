*****************************
Using the Rovation client API
*****************************

The Ovation R API wraps the Ovation Java API for use with the R statistical computing environment. Through this R API, R users can access the full functionality of the Ovation ecosystem from within R. 

Requirements
============

* Java 1.6+
* R 2.15.0+


Installation
============

Download the Ovation R library from http://ovation.io/downloads. You can install the library archive directly via the R package manager or at the R command line::

	install.packages(pathToOvationR.tar.gz, repos=NULL)


Usage
=====


1. Load the Ovation R library::

	library(Rovation)
    
.. note:: 
    OS X users see details  :ref:`below <subsec-rovation-osx>`.
    
2. Open a new `DataContext` with the `NewDataContext` function::

	dataContext <- NewDataContext("EMAIL")

where `EMAIL` is the email registered with your `ovation.io <http://ovation.io>`_ account.

.. _subsec-rovation-osx:

OS X
----
OS X users may receive an error 
    
    Apple AWT Java VM was loaded on first thread -- can't start AWT.
    
when creating a new data context. If you receive this error, restart R and load `Rovation` using the following pattern to disable the "AWT" thread during initialization::

    Sys.setenv(NOAWT=1)
    library(Rovation)
    Sys.unsetenv("NOAWT")