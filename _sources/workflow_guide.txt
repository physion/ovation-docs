.. _doc-workflow-guide:

****************
Ovation Workflow
****************

There are many ways that you can use Ovation's powerful data organization and provenance tracking features. This document describes a workflow that other Ovation users have found succesful. If you have suggestions or find an other way of using Ovation that you really like, please `tell <http://ovation.uservoice.com>`_ us!


.. _fig-organize-track-workflow:

.. figure:: _static/organize-track-workflow.png
   :align: center

   Recommended workflow for organizig primary data (`Measurements`) and analyses in Ovation. The sections below describe how to do each step in this simple workflow.



.. _sec-import-files-workflow:

1. Import files
===============

Data files can be imported directly from the instrument(s) used in an experiment or from existing files on your computer or server. When stored in Ovation, we call these files "Measurements". You can use the Ovation application to insert new :ref:`Measurements <sec-new-measurement>`. You can also add Measurements programatically using the Ovation programming interface (API):

.. language_specific::
    
    --Python
    ::

        from ovation.conversion import to_map, to_java_set, to_file_url, asclass
        from ovation.core import date_time

        # Obtain a reference to the containing experiment, e.g. by URI
        experiment = asclass('Experiment', data_context.getObjectWithURI('ovation://...'))
        
        # Obtain a reference to the measured Source(s)
        source = asclass('Source', data_context.getObjectWithURI('ovation://...'))
        
        # Insert an Epoch describing the procedure that recorded the measurement(s)
        
        input_sources = {'source': source}  # Map of Sources that were "inputs" to the measurements named by map key.
                                            # Input Source name(s) give the Sources' named in the context of this procedure.
                                            
        protocol = data_context.getProtocol('My protocol name') # Get a protocol (by name) describing the Measurement procedure
        
        protocol_parameters = {} # Map of variable parameters for this protocol
        device_parameters = {} # Map of device parameters for devices used in making the Measurement(s)
        
        epoch = experiment.insertEpoch(to_map(input_sources),
                                        None,                                       # No Sources were generated in this Epoch
                                        date_time(2014, 3, 2, hour=8, minute=5),    # Start of measurement procedure
                                        date_time(2014, 3, 2, hour=8, minute=15),   # End of measurement procedure
                                        protocol,                                   # Measurement protocol or None
                                        to_map(protocol_parameters),                # Protocol parameters or None
                                        to_map(device_parameters))                  # Device parameters or None
        
        
        
        # Add a measurement file by path
        measurement_path = "/path/to/local/my_file"
        measurement_url = to_file_url(measurement_path)
        measurement_name = os.path.split("/path/to/local/file")[-1] # i.e. "my_file"
        epoch.insertMeasurement(measurement_name,
                                to_java_set('source'),                  # When Epoch has multiple input Sources, which are associated with this measurement, by name
                                to_java_set(['device1', 'device2']),    # Devices used in this measurement or empty if none
                                measurement_url,
                                'application/octet-stream'              # Measurment content type, e.g. text/csv, imate/tiff, etc. Application/octet-stream is the most generic
                                )
                                
    --R
    ::

        # Obtain a reference to the containing experiment, e.g. by URI
        experiment <- data_context$getObjectWithURI('ovation://...')
        
        # Obtain a reference to the measured Source(s)
        source <- data_context$getObjectWithURI('ovation://...')
        
        # Insert an Epoch describing the procedure that recorded the measurement(s)
        
        input_sources <- list(source_name = source)  # List of Sources that were "inputs" to the measurements named by list key.
                                                    #Input Source name(s) give the Sources' named in the context of this procedure.
                                            
        protocol <- data_context$getProtocol('My protocol name') # Get a protocol (by name) describing the Measurement procedure
        
        protocol_parameters <- list()   # Map of variable parameters for this protocol
        device_parameters <- list()     # Map of device parameters for devices used in making the Measurement(s)
        
        epoch <- experiment$insertEpoch(list2map(input_sources),
                                        None,                                       # No Sources were generated in this Epoch
                                        Datetime(2014, 3, 2, hour=8, minute=5),     # Start of measurement procedure
                                        Datetime(2014, 3, 2, hour=8, minute=15),    # End of measurement procedure
                                        protocol,                                   # Measurement protocol or None
                                        list2map(protocol_parameters),              # Protocol parameters or None
                                        list2map(device_parameters))                # Device parameters or None
        
        
        
        # Add a measurement file by path
        measurement_path = '/path/to/local/my_file'
        measurement_url = NewUrl(measurement_path)
        epoch.insertMeasurement('my_file',                              # Measurement display name
                                Vector2Set(c('source')),                # When Epoch has multiple input Sources, which are associated with this measurement, by name
                                Vector2Set(c('device1', 'device2')),    # Devices used in this measurement or empty if none
                                measurement_url,
                                'application/octet-stream')             # Measurment content type, e.g. text/csv, imate/tiff, etc. Application/octet-stream is the most generic

    --Matlab
    ::

        import ovation.*
        
        % Obtain a reference to the containing experiment, e.g. by URI
        experiment = dataContext.getObjectWithURI('ovation://...');
    
        % Obtain a reference to the measured Source(s)
        source = dataContext.getObjectWithURI('ovation://...');
    
        %% Insert an Epoch describing the procedure that recorded the measurement(s)
        input_sources = struct()
        input_sources.sourceName = source;  % Struct of Sources that were "inputs" to the measurements named by struct field.
                                            % Input Source name(s) give the Sources' named in the context of this procedure.
                                        
        protocol = dataContext.getProtocol('My protocol name'); % Get a protocol (by name) describing the Measurement procedure
    
        protocol_parameters = struct(); % Map of variable parameters for this protocol
        device_parameters = struct();   % Map of device parameters for devices used in making the Measurement(s)
    
        epoch = experiment.insertEpoch(struct2map(input_sources),...
                                        [],...                                 % No Sources were generated in this Epoch
                                        datetime(2014, 3, 2, 8, 5),...         % Start of measurement procedure
                                        datetime(2014, 3, 2, 8, 15),...        % End of measurement procedure
                                        protocol,...                           % Measurement protocol or []
                                        struct2map(protocol_parameters),...    % Protocol parameters or []
                                        struct2map(device_parameters));        % Device parameters or []
    
    
    
        % Add a measurement file by path
        measurement_path = '/path/to/local/my_file';
        measurement_url = java.net.URL(['file://' measurement_path]);
        measurement_name = 'my_file';
        epoch.insertMeasurement(measurement_name,...            % Measurement display name
                                {'source'},...                  % When Epoch has multiple input Sources, which are associated with this measurement, by name
                                {'device1', 'device2'},...      % Devices used in this measurement or empty if none
                                measurement_url,...
                                'application/octet-stream'...   % Measurment content type, e.g. text/csv, imate/tiff, etc. Application/octet-stream is the most generic
                                )


.. _sec-use-files-workflow:

2. Use files in your existing pipeline
======================================

Once data files are stored in Ovation, it is easy to retrieve them for use in your existing analysis pipeline(s). To open a file, click the "Open in native application…" button in the Data Viewer or select "Open in Finder" (OS X) or "Open in Explorer" (Windows) from the context menu of a Measurement in the Ovation application.

You can also retrieve the file programatically using the Ovation programming interface (API):

.. language_specific::

    --Python
    ::
        
        # Given a Measurement URI, retrieve the Measurement from the local Data Context
        measurement = data_context.getObjectWithURI('ovation://...')
        
        # Get the path to the Measurement's file(s). getLocalDataPath() returns asynchronously, get() waits for completion
        local_path = measurement.getLocalDataPath().get()
        
    --R
    ::
    
        # Given a Measurement URI, retrieve the Measurement from the local Data Context
        measurement <- data_context$getObjectWithURI('ovation://...')
        
        # Get the path to the Measurement's file(s). getLocalDataPath() returns asynchronously, get() waits for completion
        local_path <- measurement$getLocalDataPath()$get()
        
    --Matlab
    ::
    
        % Given a Measurement URI, retrieve the Measurement from the local Data Context
        measurement = dataContext.getObjectWithURI('ovation://...');
        
        % Get the path to the Measurement's file(s). getLocalDataPath() returns asynchronously, get() waits for completion
        local_path = measurement.getLocalDataPath().get();
        
        
Now you can perform your analysis as you do now (using the local data files). Don't forget to record the parameters of your analysis so that you can store that information in Ovation!


.. _sec-import-analyses-workflow:

3. Import results as Analysis Records
=====================================

Once you've performed an analysis, store the results (and parameters of that analysis) into Ovation as an Analysis Record. An Analysis Record lets you track the inputs, procedure and results of an analysis. No more losing track of how you did an analysis amidst a sea of files! The :ref:`Analysis Record Guide <doc-analysis-records-guide>` had all the info you need to add an Analysis Record to Ovation.