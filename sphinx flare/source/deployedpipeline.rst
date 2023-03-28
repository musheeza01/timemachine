.. _deployedpipeline:

Deployed Pipelines in Flare
*******************************

Overview
================

The deployed pipelines view within LigaData Flare displays a list of published pipelines that have successfully been deployed. You can also filter the pipelines based on the categories.

To access the deployed pipelines section, select **Deployed Pipelines** from the main menu. The following view will appear on the screen.

.. figure::  deployed.png
    :align:   center 

.. Note::
    If you do not see these options, you might not have the relevant permissions. For more details, check with your administrator.


Run/Pause Pipeline
=========================

To run a deployed pipeline, click on the play icon under the Actions column, corresponding to the pipeline that needs to be paused. Similarly, click on the pause icon to pause the pipeline.

Stop Pipeline
==================

To stop a running pipeline, click on the stop icon under the Actions column, corresponding to the pipeline that needs to be stopped. The pipeline will stop running.

.. _viewpipeline:

View Pipeline Stats
========================

Upon successfully running the pipeline, the pipeline stats are generated and the charts are populated based upon the recorded data.

To view stats specific to a pipeline, click on the **expand icon** under the **Actions** column, corresponding to the pipeline for which the pipeline details need to be viewed.

The section will expand and the following charts will appear on the screen.

.. figure::  stats.png
    :align:   center 

Each chart displays the following information:

+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fields   | Description                                                                                                                                                 | 
+==========+=============================================================================================================================================================+
| Error    | Displays the number of errors recorded by the origin or destination stage(s). The details of these errors is populated in the **Errors** chart to the right |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Output   | Displays the amount of records written into the destination stage(s)                                                                                        |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input    | Displays the amount of records read from origin stage(s)                                                                                                    |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| In MB    | Displays the size of records read from origin stage(s)                                                                                                      |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Out MB   | Displays the size of records written into the destination stage(s)                                                                                          |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Undeploy Pipeline
======================

To undeploy a pipeline, follow the steps below:

1. Click on the delete icon corresponding to the pipeline to be deleted. A dialog box will appear on the screen. 

2. Click on the Confirm button to proceed.

The pipeline will be undeployed successfully and moved back to the Published Pipelines page.

 