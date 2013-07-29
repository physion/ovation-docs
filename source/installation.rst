.. _doc-installation:

************
Installation
************

|Ovation(TM)| is a data management platform that helps researchers organize, search and share their data. To get started with Ovation, sign up for an account on `ovation.io <http://ovation.io>`_. Once you've signed up for an account, you can download_ the Ovation application and get started.

.. _download: http://ovation.io/downloads

Requirements
============

Ovation supports the following operating systems and architectures:

* OS X 10.8 and later
* Windows 7 and later (64-bit)

Ovation requires the Java runtime (JRE) version 7 or later. Please download_ and install Java before installing Ovation.


Installation
============

To install the Ovation application, download the appropriate platform binary from `ovation.io <http://ovation.io>`_.

Mac OS X
--------

These instructions detail installation on Mac OS X 10.8 or later.

1. Open the installer disk image
2. Drag the Ovation application to the "Applications" folder

.. figure:: _static/osx_installer_dmg.png
    :figwidth: 33%
    :align: center

    To install Ovation, drag the Ovation application to the "Applications" folder.

3. Double-click the Ovation application in the "Applications/" folder

.. figure:: _static/ovation_icon_osx.png
    :align: center

    Double-click the Ovation application in the "Applications/" folder to start Ovation

Windows
-------

These instructions detail installation on Windows 7 or later.

1. Double-click the "Ovation Installer.exe" to start the installation wizard.
2. Follow the on-screen steps to install Ovation
3. Open the Ovation application from the "Start" menu (Windows 7) or the "Start screen" (Windows 8)


Programming environment setup
=============================

Ovation integrates with several scientific programming environments. Follow the instructions for your language of choice below.

.. _sec-matlab-installation:

Matlab
------

1. `Download <http://ovation.io/downloads>`_ the the "Ovation API all-in-one Jar". Add the path to the all-in-one jar file to the *top* of the `${matlabroot}/toolbox/local/classpath.txt` file.

.. note::
    You must add the Ovation jar to the top of Matlab's `classpath.txt`. The Ovation API will not function properly if you add the jar to Matlab's classpath via `javaaddpath`.

2. Download the `Ovation Matlab API <https://github.com/physion/ovation-matlab/archive/master.zip>`_ package. Add the unzipped folder to the Matlab path. After unzipping `ovation-matlab-master`, you may add the following to Matlab's `startup.m` to autmatically load the Ovation API at startup::

    addpath path/to/ovation-matlab-master
    import ovation.*

3. After starting Matlab, open a `DataContext`—a view of the Ovation database data—with the `NewDataContext()` function. Enter your `ovation.io <http://ovation.io>`_ account email and password when prompted::

    >> context = NewDataContext()


.. _sec-python-installation:

Python
------

Ovation's Python API supports CPython 2.7. Installation requires the `setuptools` package. If you don't have (or don't know if you have) `setuptools` installed, download the `ez_setup.py <https://bitbucket.org/pypa/setuptools/raw/0.7.4/ez_setup.py>`_ tool and run it to install `setuptools`::

     python ez_setup.py

Ovation's Python API depends on the `NumPy <http://www.numpy.org>`_ and `SciPy <http://www.scipy.org>`_ packages. Before installing the `ovation` package, make sure that both NumPy and SciPy are installed::

    easy_install numpy scipy
    
.. note::
    If you experience trouble installing NumPy or SciPy, there are a number of pre-built distributions provided by 3rd parties. Mac users may wish to install the SciPy `superpack <http://fonnesbeck.github.io/ScipySuperpack/>`_. Windows users can find unofficial binary installers for these and other common Python packages at "`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_". 

To install the Ovation Python API::

    easy_install ovation


.. tip:: Although not required, we recommend the following additional packages:

    * `ipython <http://ipython.scipy.org>`_::
    
        easy_install ipython



R Project for Statistical Computing
-----------------------------------

Ovation's R API (`Rovation`) supports R 2.15 and later via the `rJava` package. To install the R API, follow the instructions below.

1. Download the Ovation R API from http://ovation.io/downloads.
2. Install the `Rovation` from the package archive file.

.. figure:: _static/r_studio_install_package.png
    
    Rstudio package installation window. Select Install From "Package Archive", then choose the path to the Rovation package downloaded from http://ovation.io. Click "Install" to install `Rovation`.

.. note::
    The first version of Rovation was written by Romain Franconville at the Janelia Farm Research Campus of the Howard Hughes Medical Institute. Thanks, Romain!

Java
----

Ovation's API is available as a Java library. Add the following dependencies in your Maven project::

    <dependency>
        <groupId>us.physion</groupId>
        <artifactId>ovation-api</artifactId>
        <version>2.0</version>
    </dependency>


    <dependency>
        <groupId>us.physion</groupId>
        <artifactId>ovation-logging</artifactId>
        <version>2.0</version>
    </dependency>


If you want to write JUnit-based unit tests for code that uses the Ovation API, you may want to make use of the `ovation-test-utils` package::

    <dependency>
        <groupId>us.physion</groupId>
        <artifactId>ovation-test-utils</artifactId>
        <version>2.0</version>
        <scope>test</scope>
    </dependency>

Finally, the following `repository` descriptors should be added to your Maven project's `<repositories>` section::

    <repository>
        <id>ovation-release-repository</id>
        <name>Ovation Release Repository</name>
        <url>s3://us.physion.maven/release</url>
    </repository>
    <snapshotRepository>
        <id>ovation-snapshot-repository</id>
        <name>Ovation Snapshot Repository</name>
        <url>s3://us.physion.maven/snapshot</url>
    </snapshotRepository>


Ovation API documentation is available on the Ovation `JavaDoc <http://javadoc.ovation.io>`_ site.

.. |Ovation(TM)| unicode:: Ovation U+2122