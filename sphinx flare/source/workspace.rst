.. _workspace:

Workspace & Local Pipeline
****************************

Overview
================

Workspace allows you to create a space that can be used to group the pipelines within it. You can create a local pipeline or import a published pipeline within a workspace.

.. Note::
    It is mandatory to assign a pipeline to a workspace.

To access the workspaces section, select **Workspaces & Local Pipelines** from the main menu. 
The workspaces page will appear on the screen.

.. figure:: workspace.png
    :align: center

Create New Workspace
================================

To create a workspace, follow the steps below:

1. Click on the + Create New Workspace button. A dialog box will appear on the screen. 

2. Specify the following information:

        a. Name:  Provide the name of the workspace

        b. Description: Provide a brief description of the type of pipeline(s) that will be linked with this workspace.

3. Click on the Create button.

The workspace will be created successfully.

Edit Workspace
====================


To edit a workspace, follow the steps below:

1. Click on the edit icon corresponding to the workspace to be edited. A dialog box will appear on the screen. 

2. Make the required updates.

3. Click on the Save button to proceed.

The workspace will be edited successfully.

Delete Workspace
========================

To delete a workspace, follow the steps below:

1. Click on the delete icon corresponding to the workspace to be edited. A dialog box will appear on the screen to confirm deletion.

2. Click on the Confirm button to proceed.

The workspace will be deleted successfully.

.. Note::
    A workspace cannot be deleted unless all the local pipelines and the ones pending approval within that workspace are deleted.

Troubleshooting Workspace
=============================

While working with workspaces, you might come across some errors while performing certain actions. In this section, you will see the errors associated with workspaces along with the remediation steps.

Error: This workspace can’t be deleted as it has pipelines
------------------------------------------------------------

* **Root cause:** You may come across this error when trying to delete a workspace, associated with certain local and pending pipelines.
* **Solution:** Delete all the pipeline associated with this workspace and then try deleting the workspace again. The error will then be resolved.