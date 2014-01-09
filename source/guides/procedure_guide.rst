.. _doc-procedure-guide:


************************
Protocols and Procedures
************************

``Protocols`` describe a ``Procedure`` for making a *Measurement*, creating a new *Source* or performing an *Analysis*. Ovation ``Protocol`` objects may contain written textual description. They may also contain a reference to computer code describing the process. Each ``Protocol`` should be represented only once in the Ovation database, even if the Procedure it describes is performed many times.

A ``Procedure`` references the ``Protocol`` object and stores *protocol parameter* values, the values of any *variables* in the Procedure description such as reagent concentration, lot number, time intervals, etc.


.. _sec-procedures-measurements:

Making Measurements
===================

Ovation's data model contains a number of ``Procedure`` elements that describe how *Measurement(s)* are made during an experiment. As shown in the :ref:`Expanded Structural Model <fig-expanded-data-model>` *Measurements* are made during an ``Experiment``. An ``Experiment`` may be subdivided into one or more ``Epochs``. An :ref:`Epoch <sec-procedures-epochs>` represents a segment of the experimental timeline with a known start and end time. In trial-based experiments, each trial is one ``Epoch``. ``Epochs`` may be (optionally) grouped into ``EpochGroups`` to describe the experimental structure. In a trial-based experiment, ``EpochGroups`` would represent blocks of trials, such as "control", "treament" and "recovery" blocks of a pharmacological study.

.. figure:: _static/expanded-data-model.png
   :figwidth: 50%
   :align: right
   
``Epochs`` deserve a bit of special attention because they represent Ovation's "unit of scientific work". During an ``Epoch`` a procedure is performed, one or more named *Measurements* are made and/or one or more *Sources* are derived. 

.. figure:: _static/epoch-data-model.png
   :figwidth: 50%
   :align: right

An ``Epoch`` contains references to the ``Sources`` from which *Measurements* were made during that epoch (the "input sources"). Each ``Measurement`` references one or more of its Epoch's *input sources* by name.  

If new ``Source(s)`` are created during the procedure, they are also referenced (the "output sources").

Each of the ``Epoch > EpochGroup > Experiment`` elements may be associated with a ``Protocol``. It's up to you to determine where it makes most sense to attach the protocol for your experiment. If you have a protocol that describes the entire experiment, it makes sense to attach it at the ``Experiment``. If you have a potentially different protocol describing the measurements made in each Epoch, the ``Protocol(s)`` should be associated with the ``Epochs``.


Source derivation
=================



Analysis Records
================

