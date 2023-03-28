.. _pipelines:

Pipelines in Flare
*******************************

Overview
================

A Pipeline within LigaData Flare provides a visual representation of data flow passing through multiple steps and processes from data sources to destination systems.

It offers an end-to-end pipeline management capability that allows you to define how data should be processed at each stage and configure the settings for each origin, processor and destination node. Data pipelines can also make decisions or update states of system entities based on incoming data.

The image below shows the lifecycle of a typical pipeline created on LigaData Flare along with the various possible use cases.

.. figure:: pipelineflare.png
    :align: center

The pipeline views can be accessed from the main menu, by clicking on the LigaData Flare logo located at the top left corner of the screen. 

A brief description of each is shared below:

+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Section                    | Description                                                                                                                                                                                | 
+============================+============================================================================================================================================================================================+
| Workspace & Local Pipeline | Lets you create a workspace that can be used to create local pipelines within it.                                                                                                          |
+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pending Pipeline Approval  | Lets you view the list of pipeline publication requests, put the pipeline for testing, approve or reject the request. The approved pipelines will be moved to the published pipelines page.|
+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Published Pipelines        | Lets you view the list of approved pipelines ready to be deployed into the environment of your choice.                                                                                     |
+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Deployed Pipelines         | Lets you pause and resume a running pipeline, along with the ability to view the pipeline specific stats.                                                                                  |
+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pipelines in Testing       | Lets you test the validity of the pipelines requiring approval, by deploying them to a test environment.                                                                                   |
+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. Note::
    All pipelines are associated with a workspace. Hence, it is mandatory to create a workspace before creating a pipeline. For more information, refer to the :ref:`Workspace <workspace>` section.