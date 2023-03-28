.. _pipelinetesting:

Pipelines in Testing In Flare
********************************

Overview
================

The pipelines in testing view within LigaData Flare displays a list of pipelines that are currently in the testing phase.

The pipelines can be put into the testing phase from the following views:

* **Local pipelines:** These pipelines are deployed in the development environment for testing

* **Pending pipelines:** These pipelines are deployed in the staging environment for testing

To access this section, select **Pipelines in Testing** from the main menu. The following view will appear on the screen.

.. figure::  testing.png
    :align:   center 

.. Note::
    * You can choose the environment in which the pipeline needs to be deployed for testing from the **Environment** dropdown located at the top right corner of the screen.
    * If you do not see these options, you might not have the relevant permissions. For more details, check with your administrator.

Run/Pause Pipeline
=======================

To run a pipeline in test, click on the play icon under the Actions column, corresponding to the pipeline that needs to be paused. 

Doing so will generate the pipeline stats which can be viewed by clicking on the expand icon located at the right. 

.. admonition:: Info

    To learn more about the pipeline stats, refer to the :ref:`View Pipeline Stats <viewpipeline>` section.

Stop Pipeline
====================

To stop a running pipeline in test, click on the stop icon under the Actions column, corresponding to the pipeline that needs to be stopped. 

The pipeline will stop running.

Undeploy Pipeline
====================

To undeploy a pipeline, follow the steps below:

1. Click on the delete icon corresponding to the pipeline to be undeployed. A dialog box will appear on the screen. 

2. Click on the Confirm button to proceed.

The pipeline will be undeployed successfully and moved back to it source from where (Local Pipelines or Pending Pipelines section) it was sent for testing.