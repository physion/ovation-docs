===============
Getting Started
===============

|Ovation(TM)| is a combination web service, local application and programming platform. To get started with Ovation, you sign up for an account on `ovation.io <http://ovation.io>`_.

Once you've signed up for an account, you can download the Ovation application and get started.

Requirements
============

Ovation supports the following operating systems and architectures:

* OS X 10.8 and later
* Windows 7 and later (64-bit)

Installation
============

To install the Ovation application, download the appropriate platform binary from `ovation.io <http://ovation.io>`_.


Programming environment setup
=============================

Ovation integrates with several scientific programming environments. Follow the instructions for your language of choice below.

Matlab
------

1. Download the the bundled Ovation `jar`. Add the path to this jar to the *top* of the `${matlabroot}/toolbox/local/classpath.txt` file.

2. Download the `Ovation Matlab API <https://github.com/physion/ovation-matlab/archive/master.zip>` package. Add the unzipped folder to the Matlab path. After unzipping `ovation-matlab-master`, you may add the following to Matlab's `startup.m` to autmatically load the Ovation API at startup::

    addpath path/to/ovation-matlab-master
    import ovation.*

.. note::
    You must add the Ovation jar to the top of Matlab's `classpath.txt`. The Ovation API will not function properly if you add the jar to Matlab's classpath via `javaaddpath`.

3. After starting Matlab, open a `DataContext`—a view of the Ovation database data—with the `NewDataContext()` function. Enter your `ovation.io <http://ovation.io>`_ account email and password when prompted::

    >> context = NewDataContext()


.. todo::
    Provide JAR download

Python
------

R Project for Statistical Computing
-----------------------------------

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


Ovation API documentation is available on the Ovation `documentation <http://docs.ovation.io>`_ site.

.. |Ovation(TM)| unicode:: Ovation U+2122
