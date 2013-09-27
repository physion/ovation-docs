.. Copyright (c) 2013 Physion LLC


.. _ch-data-model:

**********************
The Ovation Data Model
**********************

This chapter describes the data model used by the Ovation database and API. It explains in detail the main entities in the data model, and demonstrates how instances of these entities combine to represent experimental data and analyses.


Overview 
########

Ovation stores two fundamental types of data: *structural* data that describes the raw data of an experiment and the conditions under which it was acquired and *interpretational* data that describes information such as keywords, annotations, derived values and analysis added by the experimenter and colleagues after the experiment.

Everything that you know about data *before* viewing or analyzing it—the subject of the experiment, the stimuli presented, the type(s) of data acquired, the settings of any hardware devices that presented stimuli or recorded data, etc.—is structural data. Information such as additional metadata, keywords, derived values, or entire analysis results that can only be known *after* viewing or analyzing the data is interpretational data.

This chapter describes the classes of objects, called *entities*, in the Ovation data model that hold structural and interpretational data.


Entities
********

The Ovation database stores instances of several entities or classes [#]_ of objects [#]_. Entities in the database represent types in the nomenclature of science: ``Projects``, ``Experiments``, ``Epochs`` ("trials"), etc. This set of classes, their attributes, and their relationships defines the data model of the Ovation database.

Object instances represent a particular instance of their entity's class, e.g. an ``Experiment`` instance represents a particular experiment, performed on a specific date, with a specific subject, etc. All objects in an Ovation database must have a class type of one of the data model entities. To facilitate data sharing between Ovation databases, the Ovation data model has been carefully constructed to accommodate the variety of scientific data using a single data model.


Figure :ref:`3.1 <ovation-user-data-model-figure>` shows a diagram of the major user-visible entities in the Ovation data model.

.. _ovation-user-data-model-figure:
.. figure:: images/ovation-user-data-model.pdf
    :width: 95%

    User-visible classes in the Ovation data model. The major user-visible entities in the data model are shown as boxes with the entity name in bold. Entities that are the major structural data elements are highlighted in red. Inheritance is shown with grey lines with an open triangle pointing to the superclass, e.g. ``DerivedResponse`` is a subclass of ``ResponseBase``. All user-visible entities are direct or indirect subclasses of ``EntitytBase``. Subclasses "inherit" all of the attributes and relationships of their superclass. For example, all entities have a ``uuid`` attribute, inherited from ``EntityBase``. Required attributes (see :ref:`data-validation-sec`) are shown in bold/italic.
    
All user-visible entities in the Ovation data model share several common attributes:

    uuid
        A globally unique identifier
    owner
        The ``User`` that "owns" this object in the database.
    properties
        A collection of key-value pairs. You may add arbitrary metadata to any object in the database using its properties attribute. Each object has a separate collection of properties for each user. Thus, you may view and query the properties you added to an object or all of the properties added by all users.
    keywords
        A collection of keyword tags. Each object has a separate collection of keyword tags for each user. Thus, you may view and query the tags you added to an object or all of the tags added by all users. ``KeywordTag`` instances are not themselves taggable.
    annotations
        A collection of annotations. Annotations may be grouped by common ``KeywordTag`` into "annotation groups". Annotations are stored per-user.
    resources
        A collection of ``Resource`` objects representing files or URLs. You can use ``Resources`` to associate arbitrary files with any object. For example, you might use ``Resources`` to associate anatomical images with a ``Source``. File ``Resources`` are copied *into* the database and are synchronized when going offline. Data for ``URLResources`` are not stored in the database. Retrieving the data for a ``URLResource`` may require internet access.
               

.. [#] *Class* and *entity* may be used interchangeably.
.. [#] In engineering terminology, Ovation is an *Object Database Management System*.

Structural data entities


Structural data entities describe raw data and conditions of its acquisition within in a scientific experiment. The red-highlighted entities in Figure :ref:`3.1 <ovation-user-data-model-figure>` are the primary structural data entities in the Ovation data model. There is a natural containment relationship among these entities (with the exception of ``Sources``): ``Projects`` contain ``Experiments``, which contain ``ExternalDevices`` and ``EpochGroups``, which contain ``Epochs`` and so on. ``Sources`` are separate from this containment hierarchy because a ``Source`` instance, representing an experimental subject, may be associated with more than one ``Experiment`` instance.

Using the terminology of Ovation, new elements (e.g. an ``Experiment``) are *inserted into* their containing entity (e.g. the ``Project``). From an instance of one of these entities, you can move "upwards" in the containment hierarchy (e.g. by calling ``epochGroup.getExperiment()`` to get the experiment containing an ``EpochGroup``) or "downwards" in the containment hierarchy (e.g by calling ``epochGroup.getEpochs()``) to get the ``Epochs`` contained by an ``EpochGroup``.

The following sections describe particular aspects of some of these entities:

- `Timeline elements`_
- `Hierarchical elements`_
- `External devices`_


Timeline elements
*****************

All entities in the Ovation data model that have a natural timeline representation are called *timeline elements*. Timeline elements have a start and end time. The end time may be optional (e.g. for ``Experiments``) or required (e.g. ``Epochs`` are invalid without an end time).

All times in the Ovation data model are stored as date, time and timezone with time resolution to 100 nanoseconds. Internally, all times are converted to Coordinated Universal Time (UTC) but the original timezone is retained, allowing conversion back to either the local or original timezone.



.. _sec-hierarchical-elements:

Hierarchical elements
*********************

The Ovation data model has two entities that allow arbitrary hierarchical relationships. This structure was chosen to allow maximum flexibility in representing a wide variety of possible datasets while maintaining a common data model across all Ovation databases.

EpochGroup hierarchy
====================

``EpochGroup`` instances represent logical groups of ``Epochs`` within an experiment. Typically, an epoch group represents a group of epochs with common experimental conditions. For example, in a physiology experiment that compared biological response to a stimulus with and without the presence of a pharmacological agent, there may be "control", "drug" and "wash" ``EpochGroups`` to represent the structural grouping of Epochs in the experiment.

Each ``EpochGroup`` has a ``label`` property describing the group (e.g. "drug", "control", "wash", etc.). It is up to your lab to agree on a nomenclature for labeling ``EpochGroup`` instances. Agreeing on a nomenclature makes querying and interpreting data from other lab members easier.

``EpochGroup`` instances typically make use of the ``properties`` attribute to store any needed information about the experimental condition or group of Epochs. For example, an ``EpochGroup`` representing application of a drug might include the drug's lot number and concentration as properties. It is again up to your lab group to agree on a set of common property keys for storing the necessary information.

``EpochGroups`` may be nested, allowing description of complex structural hierarchies in grouping of trials.

.. note:: Nesting ``EpochGroups`` makes it harder to query for ``Epochs`` given properties of their containing ``Experiment``. You must know the number of parent ``EpochGroups`` in order to perform such a query. This restriction will be removed in a future Ovation release.

Source hierarchy
================


``Source`` instances represent the subject of an experiment. Each ``EpochGroup`` can be associated with a single ``Source``, from which all data for that ``EpochGroup`` was generated. Each ``Source`` has a ``label`` property describing the type of source (e.g. "animal", "mouse", "cortical slice", "pyramidal cell", etc.). It is up to your lab to agree on a nomenclature for labeling ``Source`` instances. Agreeing on a nomenclature makes querying and interpreting data from other lab members easier. 

``Source`` instances typically make use of the ``properties`` attribute to store any needed information about the represented source. For example, a ``Source`` representing an animal might store the identifier of that animal in a colony database as the 'animal-id' property. It is again up to your lab group to agree on a set of common property keys for storing the necessary information. Your Physion consultant will work with you to develop a set of common labels and property keys when developing your data import system.

``Sources`` may be nested, allowing for a description of tissues, cells, regions, etc. contained in another ``Source`` object. For example, an experiment that recorded *in vivo* physiology data from a primate cortex might represent the biological source of those recordings with a ``Source`` representing the animal and another ``Source`` representing the position in cortex where the recording was made (Figure :ref:`3.2 <monkey-cortex-figure>`). In the terminology of Ovation, the second source is a 'child' of the``Source`` representing the specific animal in the experiment. An *in vitro* experiment that recorded from a single cell, might include an additional hierarchical layer for representing the individual cells within a cortical region (Figure :ref:`3.3 <rat-cortex-cell-figure1>`).

.. _monkey-cortex-figure:
.. figure:: images/monkey-cortex-source.pdf

    A source hierarchy representing an animal and a cortical position. Properties are used to store species (e.g. Macaque) and position information.
    
.. _rat-cortex-cell-figure1:
.. figure:: images/rat-cortex-cell-source.pdf

    A source hierarchy representing an animal, cortical position and single cell. Properties are used to store species (i.e. rat), cortical postion and cell type.

``Source`` instances are "top-level" objects within the database. They are inserted directly into a data context and can be retrieved by name from a data context connected to the Ovation database. In some cases, a ``Source`` and one or more of its children may be associated with one or more ``Experiments``. For example, an animal may participate in several behavioral experiments. A single ``Source`` instance would be used to represent that animal. If the animal is later sacrificed for an *in vitro* experiment, a child ``Source`` would be added to the ``Source`` representing the animal. This child ``Source`` would be associated with the *in vitro* experiment(s). Figure :ref:`3.4 <behavior-invitro-source-fig>` shows the ``Source`` and ``Experiment`` hierarchy that results from this experimental structure.

.. _behavior-invitro-source-fig:
.. figure:: images/behavior-invitro-source.pdf

    A source hierarchy may be associated with ``EpochGroups`` at more than one level of the hierarchy. In this example, a ``Source`` representing an animal is associated with multiple experiments in which the represented animal participated in a group of behavioral trial in a "maze". In a subsequent experiment, the animal was sacrificed for an *in vitro* experiment. A ``Source`` representing a single cell recorded in a group of "*in vitro*" trials is shown.

External devices
****************

The ``ExternalDevice`` entity is a structural data entity that represents the physical device that presented a stimulus and/or recorded a response during an experiment. Each ``Stimulus`` and ``Response`` associated with an ``Epoch`` must also be associated with an ``ExternalDevice``. For multi-channel recordings or images, each channel must be described by a separate ``ExternalDevice`` instance. 

Properties of an external device at the time of use (e.g. the gain of an amplifier) are stored in the ``externalDeviceParameters`` property of the individual ``Stimulus`` or ``Response`` instances.

``ExternalDevices`` must be unique by the combination of ``name`` and ``manufacturer`` attributes within any single ``Experiment``. 


.. _parameter-maps-section:

Parameter maps
**************

Several Ovation data entities have a parameters attribute to store arbitrary key/value pairs describing relevant parameters of the structural data. ``Epoch`` instances have a ``protocolParameters`` map for storing the parameters of an ``Epoch's`` protocol, ``Stimulus`` instances have a ``stimulusParameters`` map for storing the parameters of that stimulus' generation, and ``Stimulus`` and ``Response`` instances have an ``deviceParameters`` map for storing the parameters of their associated ``ExternalDevice``. Ovation supports the following property value data types:

- Boolean
- Binary data
- Date/time
- Floating point numeric (scalar or array)
- Integer numeric (scalar or array)
- String
- Reference to an other object in the database

Each of these data types is represented internally by an instance of ``ovation.MapValueBase``. For example, single floating point numeric values are represented by ``ovation.FloatingPointValue``, numeric arrays or matricies by ``ovation.NumericDataValue``, string values by ``ovation.StringValue``, etc. Ovation automatically de-duplicates ``MapValueBase`` instances, so storing the same value multiple times does not increase the size of the Ovation database. 

You normally do not need to worry about the internal representation of parameter maps. You may think of them as a logical table like the following:

.. csv-table:: Hypothetical parameters map
    :header: "Key","Value"
    
    someKey,"'some value'"
    anotherKey, "100.1"
    thirdKey, "[1,3.1,4]"


You can access the values of a parameter map by key. For example, you can access the ``protocolParameter`` value for a key ``'someKey'`` on an ``Epoch`` instance with ``getProtocolParameter``::

    >> value = epoch.getProtocolParameter('someKey');
    
You can retrieve the entire parameters map as a ``java.util.Map<String,Object>`` instance. For example, you can get the entire ``protocolParameters`` map for an ``Epoch`` instance with ``getProtocolParameters``. You can access individual elements from this map object with the ``get`` method::

    >> parameters = epoch.getProtocolParameters();
    >> value = parameters.get('myKey');



.. _interpretational-data-entities-section:


Interpretational data entities
******************************


Interpretational data entities describe information added by users after viewing or analyzing data. This information might include keyword tags, additional metadata properties, notes, timeline annotations, derived responses or analyses. These types are described in the sections below.

.. _keyword-tags-section:

Keyword tags
============


Keyword tags are single string "tags" used to annotate one or more objects in the Ovation database. For example, you might add the tag "example" to all Epochs that are particularly good examples of a particular phenomenon.

Keyword tags are stored per-user. From an object you may get the tags you have applied to an object or all of the tags applied by all users.

Keyword tags are queryable (see :ref:`data-query-chapter`) like all "built-in" attributes. Thus, keywords represent an almost unlimited expansion capability for adding label annotations to objects in the Ovation database.


Properties
==========

All user-visible entities in the Ovation database may have be annotated with a set of key-value properties. Each property has a string key that identifies that property and a value. Ovation supports the following property value data types:

- Boolean
- Binary data
- Date/time
- Floating point numeric (scalar or array)
- Integer numeric (scalar or array)
- String
- Reference to an other object in the database

Like keywords, properties are stored per-user. Thus you may add a property with the same key as a property added by an other user, but with a different value. You may view the value for your property with a given key or all values for a property with a given key. Internally, property values are represented like parameter map values (see :ref:`parameter-maps-section`).

Properties are queryable (see :ref:`querying-parameter-map-values-section` and :ref:`propertyvalue-query-section`) like all "built-in" attributes. You may query for just *your* properties or for properties set by all users. Thus, properties represent an almost unlimited expansion capability for adding metadata or annotations to objects in the Ovation database.

Properties are used extensively in the ``Source`` and ``EpochGroup`` entities to store relevant information for objects in those hierarchies (see :ref:`hierarchical-elements-section`).


.. _analysis-records-section:

Analysis records
****************

*Analysis records* collect the information about an analysis result. In particular, ``AnalysisRecord`` objects store:

- References to all ``Epochs`` included in the analysis
- References to "input" ``AnalysisRecords`` (e.g. intermediate results)
- Source control [#]_ repository URL and revision identifier of code used to perform the analysis 
- The name of the top-level or entry function for performing the analysis
- Parameters (as key-value pairs) of the analysis
- Artifacts (figures, PDFs, etc.) of the analysis
- Additional metadata or annotations (properties, keywords, etc.)

Given this information, it is possible to recreate an analysis, locate the raw data that went into an analysis, repeat an analysis with different parameters or a different version of the analysis code, or add new data and re-run the analysis with the same code and parameters.

``AnalylsisRecords`` are queryable as with any other object in the database. For example, the following query will find all ``AnalysisRecords`` with a keyword tag "publication" containing a particular epoch (given its UUID)::

    >> epochUUID = epoch.getUuid();
    >> iterator = context.query(AnalysisRecord.class, ['anyequal(keywords(), "publication") && ...
                                                        contains(epochs.uuid,' epoch.getUuid() ')]);


It is recommended that you structure your analysis with a top-level or entry function that takes as parameters, an iterator over Epoch objects and a struct of parameters::

    function result = MyAnalysisEntry(epochIterator, parametersStruct)

Given this prototype, it is easy to automate the replication of an analysis from an ``AnalysisRecord`` instance.

``AnalysisRecords`` are stored per-user. Like ``DerivedResposnes``, this means that you may make use of an other user's ``AnalysisRecords``, but may not modify them.


.. [#] A source control system is a specialized database that stores the history of changes to code. A number of open source source control systems exist. We recommend Subversion. Subversion is mature and well supported. If you are not currently using Subversion or an other version control system, your Physion consultant can help you install and configure a suitable system. More information about Subversion can be found at `subversion.apache.org <http://subversion.apache.org/>`_.

*Derived responses* represent values derived from individual ``Responses`` or ``Epochs``. You may choose to store these derived values in the database rather than re-calculating them each time they are needed because calculation is costly or difficult to perform. ``DerivedResponses`` encapsulate the actual derived value as well as the parameters of its derivation along with any additional annotations or metadata.

``DerivedResponses`` are stored per-user. Like other interpretational data entities, this means that each Ovation user has their personal set of ``DerivedResponses`` for each Epoch. Although you can make use of other users' ``DerivedResposnes`` (as well as query for them), you may not modify an other user's ``DerivedResponses``. ``DerivedResposnes`` are associated with a single ``Epoch`` and must have a unique name within that ``Epoch`` for each user. 

``DerivedResponse`` instances are often used to store filtered versions of ``Response`` data or times of events such as "spikes" detected in ``Response`` data.

Annotations
***********

Ovation supports a variety of annotations including note, timeline and image annotations. Future versions of Ovation will add additional annotation types. As with other interpretational entities described above, ``Annotations`` are stored per-user, meaning each Ovation user has a personal collection of ``Annotations`` for each object. You may make use of of users' ``Annotations``, but the owner of an ``Annotation`` may modify that ``Annotation``. You may annotate objects owned by another user.

The sections below describe the currently supported annotation types:

- :ref:`note-annotations-section`
- :ref:`timeline-annotations-section`
- :ref:`image-annotations-section`


.. _note-annotations-section:

Note annotations
----------------

While ``KeywordTags`` represent short string tags, ``Note`` annotations may be used to add long-form text annotations to any object in the database. Of course, the text of a ``Note`` is fully searchable. See :ref:`ovation-operators-section` for information on the ``notes`` query operator.


.. _timeline-annotations-section:

Timeline annotations
--------------------

``TimelineAnnotations`` may be used to annotate particular time points or time ranges on the experimental timeline. Discrete time points can be annotated with a ``TimelineAnnotation`` that has the same start and end time. A time range can be specified by the start and end time of the annotation.

Like ``Note`` annotations, ``TimelineAnnotations`` may contain long-form text of the users' choice. This text is searchable using the Ovation query engine.

See :ref:`ovation-operators-section` for information on the ``timelineannotations`` query operator.

As with ``TimelineElement`` start and end times, ``TimelineAnnotations`` store start and end times as time to 100 nanosecond precision and time zone.

.. _image-annotations-section:

Image annotations
-----------------

``ImageAnnotations`` are used to annotatate regions in 2-D space such as an image or a single video frame. ``ImageAnnotations`` combine a long-form text block (like other ``Annotations``), with a shape or region in space.

Ovation currently supports ``Polygon``, ``Point``, ``Oval`` and ``Line`` regions. *N*-dimensional regions for *N* > 2 are not currently supported.

*ImageAnnotatables*
	
	Only entities that can store image data can be annotated with ``ImageAnnotations``. These entities (``Responses``, ``DerivedResponses``, and ``Resources``) implement the ``ImageAnnotatable`` interface.


*ShapeViews and CoordinateSystems*

	The coordinates of an ``ImageAnnotation's`` shape are in the underlying pixel coordinates of the image being annotated. It is often more convenient, however, to work with the shape in a different coordinate system. For example, when comparing several related images, you may want to mark a common landmark on each image and work with coordinates relative to that landmark as the origin. When you know calibration information for an image that can convert from pixel distances to physical distance, such as for images from a microscope, you may also want to work with coordinates in physical units rather than pixels.
	
	Coordinate systems are described by ``CoordinateSystem`` objects, which store a reference point, serving as the 'origin' for the coordinate system. ``CoordinateSystems`` also store the physical units of the image (e.g. microns) and the pixel-to-unit scaling factor, for each dimension. ``CoordinateSystem`` objects are stored by name and per-user and must be unique by name for each ``ImageAnnotatable`` object for each user. You may have multiple coordianate systems for a particular image stored in an ``ImageAnnotatable`` object (though each must have a unique name for each user).
	
	``ImageAnnotation`` exposes only a "view" (an ``IShapeView``) of its shape to users. This view may be in image pixel coordinates (the default) or in the coordinate system provided. ``ImageAnnotations`` are inserted in image coordinates::
	
	     >> annotation = response.addPolygonAnnotation(annotationText,
						   optionalTag,
						   xCoordinates,
						   yCoordinates)
						   
	The ``getShape()`` method of ``ImageAnnotation`` returns a view of the annotation's region in image (pixel) coordinates. If you own the ``ImageAnnotation`` associated with the shape view, you can modify the region's shape by changing the coordinates (in pixels)::
	
  	     >> polygonShapeView = annotation.getShape()
     	 	>> polygonShapeView.setXCoordinates(newCoordinates)

	
	To add a ``CoordinateSystem`` to an ``ImageAnnotatable``, use the ``insertCoordinateSystem`` method::
	
		>> coordinateSystem = response.addCoordinateSystem(coordinateSystemName,
						[10,10], % origin
						{'µm', 'µm'}, % units
						[100, 200] % µm/pixel
						)
	
	Using a ``CoordinateSystem`` (yours or an other user's), you can view the shape of an ``ImageAnnotation`` by passing that coordinate system to the ``getView(coordinateSystem)`` method of ``ImageAnnotation`` ::

             >> polygonShapeView = annotation.getShape(coordinateSystem)
			 
	If you own the associated image annotation, you may also modify the annotation's shape in coordinates in the given coordinate system once you have a view in that coordinate system::
	
     	     >>	polygonShapeView.setXCoordinates(newCoordinatesInGivenCoordinateSystem)



Curation
========

``Experiment`` entities in the Ovation database have a "curated" attribute used to indicate whether the data from a particular experiment has been reviewed by the user that performed that experiment.

The ``curated`` flag on an experiment is initially ``false`` (i.e. the ``Experiment's`` data has *not* been curated). After reviewing the data from an experiment, you can set the flag to ``true`` to indicate to other users that the data from that experiment is suitable for further analysis::

    >> experiment.setCurated(true);

Adding new ``Epoch(s)`` to an experiment will automatically reset the experiment's ``curated`` flag back to false.

The ``curated`` flag can be used to exclude data from a query that has not yet been reviewed by the researcher that collected it. For example, the following query finds all ``Epochs`` with ``procolID`` equal to "example.protocol" whose experiment is marked as curated::

    >> iterator = dataContext.query(Epoch.class, 'protocolID == "example.protcol" && ...
                                        epochGroup.experiment.curated == true');

.. _data-validation-sec:

Data validation
===============

To ensure that data in an Ovation database is fully interpretable, Ovation validates all data entered in the database. An object is invalid if all required fields are not present. In some cases, Ovation performs additional validation such as insuring that the ``endTime`` of a timeline element (i.e. ``Experiment``, ``EpochGroup``, or ``Epoch``), if present, is after the ``startTime`` of that element.

Required attributes and relationships are shown in bold/italic in Figure :ref:`3.1 <ovation-user-data-model-figure>`. You can find more information about validation requirements for each entity in the online documentation for that entity (see :ref:`online-help-section`).

If *any* modified or inserted object fails a validation check, Ovation will throw an exception at the end of the enclosing transaction. This exception aborts the transaction, preventing the invalid object(s) and *all other* modified or inserted objects from being written to the database. In this case, you should make the changes necessary to bring the invalid objects into compliance, at which point Ovation will allow the commit to succeed. The validation exception contains references to the invalid objects, as well as information about what attributes on those objects were invalid.

Allowing invalid or incomplete data
***********************************

In some cases, existing data may not have all of the required information to import as a fully validated data set. For example, the exact start and end times of ``Epochs`` may not be known if those times were not recorded in the original data. In this case, you may put the Data Context into "lenient" mode. In lenient mode, the data context will allow incomplete or invalid data to be written to the database. Objects written to the database while in lenient mode that would otherwise fail validation have their ``incomplete`` flag set to true. You may choose to exclude objects that are incomplete from your queries. For example, the following query finds all ``Epoch`` objects in the database that are complete (i.e. excludes all incomplete/invalid ``Epochs``)::

    >> iterator = dataContext.query(Epoch.class, 'incomplete == false');

