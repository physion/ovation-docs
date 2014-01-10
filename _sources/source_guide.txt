.. _doc-source-guide:

*******
Sources
*******

``Sources`` represent the subjects of experimental measurements. For example, each patient in a clinincal trial would be represented by a single ``Source`` object. Likewise each mouse in a laboratory study or each field site in a field ecology study would be represented by a single ``Source`` object. 

.. figure:: _static/subject-mri.png
    :align: right
    
.. figure:: _static/mouse.png
    :align: right

.. figure:: _static/field-ecology-site-rmbl.png
    :align: right


``Source`` objects are identified by a descriptive label and an identifier. Descriptive labels are commonly used to describe the type of ``Source`` (e.g. BL6 to describe a mouse's background, or a clinical patient's name) and the identifier is used to uniquey identify the ``Source`` (e.g. an animal's identifier in a facility database, a patient's clinical patient record number, etc.).


Metadata
========

Metadata about the entity reprsented by a ``Source`` object such as sex, birth date, genus, species, genetic background, location, etc. may be stored as :ref:`Properties <sec-property-annotations>`. Properties can be added in the Ovation application by selecting a ``Source`` object in the "Source Navigator" and then entering the Properties in the "Properties" window. Properties can also be added programatically using the `addProperty <http://javadoc.ovation.io/us/physion/ovation/domain/mixin/PropertyAnnotatable.html#addProperty(java.lang.String,%20java.lang.Object)>`_ method::

    # Python
    source.addProperty('genus', 'Mus')
    



Derived Sources
===============

Sometimes the subject of an experimental measurement is a ``Source`` derived from an individual such as a tissue biopsy or cell culture. Ovation can store these *child Sources* along with information about the :ref:`Procedure <sec-procedure>` used to perform the derivation. The parent Source(s) are the "input Sources" to the ``Procedure`` and the child Source(s) are the "output Sources" of the ``Procedure``.

.. note::
    ``Measurements`` may also be made during a ``Procedure`` has output Sources. You might want to do some quality control, right?
    
To add a child ``Source`` to the database, right-click on an existing ``Source`` in the Ovation application and choose "Insert Source…". You can also add a ``Source`` using the `insertSource <http://javadoc.ovation.io/us/physion/ovation/domain/Source.html#insertSource(us.physion.ovation.domain.EpochContainer,%20org.joda.time.DateTime,%20org.joda.time.DateTime,%20us.physion.ovation.domain.Protocol,%20java.util.Map,%20com.google.common.base.Optional,%20java.lang.String,%20java.lang.String)>`_ method which will insert an ``Epoch`` describing the ``Procedure`` as well as the new child ``Source``::

    #Python
    childSource = parentSource.insertSource(epochContainer,     #Container for inserted Epoch
                                            startTime,          #Epoch start
                                            endTime,            #Epoch end
                                            protocol,           #Epoch Protocol
                                            protocolParameters, #Dict of protocol parameters
                                            deviceParameters,   #Dict of device parameters
                                            childLabel,         #Descriptive label for childSource
                                            identifier)         #Identifier for childSource
