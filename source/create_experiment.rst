.. _doc-getting-started-create-experiment:

.. raw:: html

    <div class="span12 text-center">
        <ul class="nav nav-pills" style="display: inline-block">
            <li><a href="installation.html">Install</a></li>
            <li><a href="create_project.html">Create a Project</a></li>
            <li class="active"><a href="#">Create an Experiment</a></li>
            <li><a href="create_measurement_and_source.html">Create a Measurement and add a Source</a></li>
        </ul>
    </div>
    
********************
Create an Experiment
********************

Now that you have created a Project, you can create individual Experiments within that Project.  Experiments will contain all the measurements collected or trials conducted as part of that specific Experiment.  Experiments can also contain the general setup and protocol information for these same Measurement and trials.

TIP:  Information about the equipment used, including make, model, software version, as well as global settings of that equipment all belong in the EquipmentSetup entity attached to the Experiment. Information about the protocol for the Experiment belongs in the Protocol entity attached to this Experiment. Both the protocol and equipment setup information can be added after the fact, so we will not add it now.

To add a new `Experiment`, right click on a Project entity, and select 'Insert Experiment...'

.. figure:: _static/insert_experiment1.png
   :figwidth: 40%


.. figure:: _static/insert_experiment_wizard1.png
   :figwidth: 40%


We are now ready to add the data to our Experiment!
