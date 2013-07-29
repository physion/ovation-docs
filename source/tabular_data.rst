.. _ch-getting-started:

******************************************
Importing and analyzing tabular (CSV) data
******************************************

This chapter describes methods for importing and analyzign tabular `Measurement` data in Comma Separated Value (CSV) format with Ovation and the `Rovation.csv <https://github.com/physion/ovation-R-tabular-data>`_ package for R. Two methods for importing tabular data are described:

* :ref:`Importing tabular (CSV) data via the Ovation application <sec-importing-csv-data-app>`
* :ref:`Importing tabular (CSV) data from R using the Rovation.csv package <sec-importing-csv-data-rovation>`

This chapter also describes the `Rovation.csv` tools for collecting tabular `Measurements` as an R `DataFrame` object:

* :ref:`Retrieving tabular (CSV) data with Rovation.csv <sec-retrieving-csv-data-rovation>`


.. _sec-importing-csv-data:

Importing tabular (CSV) data
============================

Ovation 

.. _sec-importing-csv-data-app:

Importing CSV data via the Ovation application
**********************************************


.. _sec-importing-csv-data-rovation:

Importing CSV data using `Rovation.csv`
***************************************

`Rovation.csv <https://github.com/physion/ovation-R-tabular-data>`_ package provides an `ImportCSV` for importing tabular data in CSV format. The `ImportCSV` function expects tabular data with the `Source` label and identifier listed in columns within the dataset. In this example, we use the following `example.csv`: 

============    =========   =========== =========== ===========
Source Label    Source ID   Col1        Col2        Col3    
============    =========   =========== =========== ===========    
label.1         id.1        0.378515032 0.4803887   0.278347607
label.2         id.2        0.752476952 0.464187255 0.769815514
label.3         id.3        0.715810992 0.510631993 0.404061552
============    =========   =========== =========== ===========


After installing the `Rovation` and `Rovation.csv` packages, 
`ImportCSV` will insert necesary `Source` objects in the database



.. _sec-retrieving-csv-data-rovation:

Retrieving tabular (CSV) data
=============================

