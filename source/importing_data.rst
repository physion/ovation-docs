=======================
Selected Data Importers
=======================

This page describes usage of selected Ovation data import plugins.


Fenton Lab .dat Data
====================

The Fenton Lab dat import script is a trio of Matlab functions. The top-level function is `import_fenton_dat`. The `import_fenton_dat` script requires the :ref:`Ovation Matlab API <sec-matlab-installation>`.

1. Add a Project and Experiment to the databse (if needed)
2. Set the Experiment equipment setup::

    >> exp.setEquipmentSetup(config2map('<cfg file>', 'Arena'))

    
.. note::
    You may choose a different equipment prefix than `Arena` if you choose. Whatever you choose, you'll need to use the same name later when calling `import_fenton_dat`

3. Create an EpochGroup within the new Experiment for the behavioral data
4. Retrieve a reference to the `EpochGroup`, `Source` and `Protocol` for the data. You can browse from the `DataContext` in Matlab or copy-and-paste from the Ovation application, using `getObjectWithURI` from the Matlab `DataContext`, e.g.::

    >> source = context.getObjectWithURI('<pasted URI from Ovation application>');
    >> protocol = context.getObjectWithURI('<pasted URI from Ovation application Protocols View>');
    >> epochGroup = context.getObjectWithURI('<pasted URI from Ovation application>');

4. Import the room-frame and arena-frame .dat and image files. This example shows an import of the `bl1D1Hab` trial::

    >> epoch = import_fenton_dat(source, epochGroup, protocol, 'Arena', 'Arena.Camera', 'America/New_York', 600, 'bl1D1Hab_Arena.dat', fullfile(pwd(), 'bl1D1Hab_Arena.png'), 'bl1D1Hab_Room.dat', fullfile(pwd(), 'bl1D1Hab_Room.png'), 'image/png')
    
.. note:: 
    You must provide the *abolute* path (i.e. from the file-system root) to the image files. Because Matlab does not change the JVM's working directory when changing Matlab working directories, there is no way to calculate the absolute path in code. You can use `fullfile(pwd(), <relative path>)` to create an absolute path.

6. Additional table (e.g. CSV) data can be imported using the "Insert Measurement..." wizard in the Ovation application::

    >> epoch.insertMeasurement('<table name>', ...
        array2set({'subject'}), ...
        array2set({'Arena'}), ...
        java.util.File('<absolute path to .csv>').toURI().toURL(), ...
        'application/csv'... % or other appropriate content type
        )


.. pClamp ABF
.. ==========
.. 
.. The Ovation pClamp (ABF) importer is a command-line tool
.. 
.. 1. If needed, install Python 2.7 (download from http://python.org)
.. 2. Install the Python `setuptools` package. Download and run `ez_setup.py <http://peak.telecommunity.com/dist/ez_setup.py>`_:
.. 
..     python ez_setup.py
..     
.. 3. If needed, install the ovation-api and ovation python modules. Download the ovation-api and install with `easy_isntall`:
.. 
..     easy_install ovation-



