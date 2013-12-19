.. _doc-getting-started-create-project:

.. raw:: html

    <div class="span12 text-center">
        <ul class="nav nav-pills" style="display: inline-block">
            <li><a href="about_ovation.html">About Ovation</a></li>
            <li class="disabled"><a href="#">&raquo;</a></li>
            <li><a href="installation.html">Install</a></li>
            <li class="disabled"><a href="#">&raquo;</a></li>
            <li class="active"><a href="#">Create a Project</a></li>
            <li class="disabled"><a href="#">&raquo;</a></li>
            <li><a href="create_experiment.html">Create an Experiment</a></li>
            <li class="disabled"><a href="#">&raquo;</a></li>
            <li><a href="create_measurement_and_source.html">Create a Measurement and add a Source</a></li>
            <li class="disabled"><a href="#">&raquo;</a></li>
            <li><a href="create_team.html">Create a Team</a></li>
        </ul>
    </div>

****************
Create a Project
****************

Once you've :ref:`installed <doc-installation>` Ovation, you're ready to start organizing your data. Ovation organizes data in a fashion familiar to scientists - projects, experiments, measurements, etc.  The best way to get started is to create a project.


Before you can add data to your Ovation database, you must login using your email address and `ovation.io`_ password.  Open Ovation and click "file" then "login".

.. figure:: _static/login_screen1.png
   :figwidth: 50%
.. :padding: 10px

.. note:: If you've forgotten your `ovation.io`_ password, you can `reset <https://ovation.io/users/password/new>`_ it.

.. _sec-new-project:

Create a `Project`
######################

This section shows you how to add a new `Project` to the database. Projects are top-level entities in the Ovation data model, and are used to organize related Experiments. Projects may contain many Experiments, and Experiments can belong to more than one Project.


To add a new `Project`, right click on the "Project Navigator" browser window and select 'Insert Project..'.

.. image:: _static/full_screen_before_project_insert_project1.png
   :width: 60%




Follow the wizard to set the name, start time, and purpose for your Project.

.. image:: _static/insert_project_wizard1.png
   :width: 60%



TIP:  If you do not see the new Project in the "Project Navigator" after finishing the project insertion wizzard, choose :menuselection:`Tools --> Reset Query` to refresh the display.

.. image:: _static/full_screen_after_project1.png
   :width: 60%
   
   
.. _ovation.io: http://ovation.io
  