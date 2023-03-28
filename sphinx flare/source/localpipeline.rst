.. _localpipeline:

Local Pipeline
****************
Overview
================

The local pipelines view displays the list of pipelines available locally that is yet to be tested, published and deployed.

The following are the potential source of local pipelines that are displayed in the local pipelines page as shown in the screenshot below:

* **New Pipeline:** All new pipelines created from the Local Pipeline section can be viewed here

* **Pending Pipelines:** The pipelines for which the publication request is declined are also listed here

* **Published Pipelines:** The following pipelines can be viewed in this section:

    * The pipelines duplicated from the published pipelines section

    * The pipelines imported from the published pipelines section

* **Pipelines in Testing:** The undeployed pipelines put into test from the local pipelines section are listed back here

Once you login to LigaData Flare and configure the necessary settings, the first step of the pipeline creation process is creating a local pipeline. A local pipeline lets you access the pipeline designer to create one from scratch.

To access the local pipelines section, select **Workspaces & Local Pipelines** from the main menu and click on the relevant workspace. The local pipeline page will appear on the screen.

.. figure::  localpipelinehome.png
    :align:   center 

.. Note::
    If you do not see these options, you might not have the relevant permissions. For more details, check with your administrator.

Create Local Pipeline
==========================

To create a local pipeline, follow the steps below:

1. Select the Workspace in which the pipeline need to be created. The Local Pipelines page corresponding to that workspace will appear on the screen.

2. Click on the + Create New Pipeline button located at the top right corner of the UI. A dialog box will appear on the screen. 

3. Specify the following information:

+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field         | Description                                                                                                                                                                                                          | 
+===============+======================================================================================================================================================================================================================+
| Name          | Specify a unique name of the pipeline.                                                                                                                                                                               |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description   | Provide a brief description of the pipeline.                                                                                                                                                                         |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Categories    | Specify the category the pipeline should be associated with.                                                                                                                                                         |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment   | Select the development environment from the dropdown, in which the pipeline needs to be created. This is a critical step as it will define the connections, caches and the parameters that the pipeline can utilize. |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type          | Select the type of pipeline from the dropdown. Currently, the following types are supported:                                                                                                                         |
|               |   * **Data Pipeline:** Regular data pipeline                                                                                                                                                                         |
|               |   * **Cache Pipeline:** Pipeline used to define caches                                                                                                                                                               |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment   | Specify the keywords to be associated with the pipeline, that can be used later to search the pipeline                                                                                                               |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

4. Click on the Create button. 

The pipeline will be created successfully.

.. warning::
    Once defined, the pipeline type i.e, data or cache pipeline cannot be edited later.

Once the pipeline has been created, the next step is to configure the pipeline and the data flow in the pipeline designer.

Pipeline designer
------------------

Once a local pipeline has been successfully created, you will be redirected to the Pipeline Designer page to build the pipeline.

LigaData Flare provides a drag and drop style canvas that allows you to pick the nodes/stages to be included from the right pane and place it where it needs to be in the pipeline. 

It gives you the full authority to define how data must flow from origin to destination and how it must be processed along the way.

.. figure::  pipelinedesigner.png
    :align:   center 

Before you begin configuring the data flow, it is important to get familiar with the UI of the pipeline designer.

The top right section of the UI contains the following features:

+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option          | Description                                                                                                                                                 | 
+=================+=============================================================================================================================================================+
| Pipelines       | Located at the top left corner of the UI. Clicking on it takes you back to the local pipelines page                                                         |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show DSL        | Displays the pipeline in code format. You can also copy and download the code using this option.                                                            |
|                 | **Note**                                                                                                                                                    |
|                 | The pipeline design must be free of any errors/warnings to be able to view the code.                                                                        |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pipelines       | Lets you create and manage various data flows in the form of pipelines. LigaData Flare offers the following pipeline specific views:                        |
|                 |    * Workspaces & Local Pipelines                                                                                                                           |
|                 |    * Pending Pipelines Approval                                                                                                                             |
|                 |    * Published Pipelines                                                                                                                                    |
|                 |    * Deployed Pipelines                                                                                                                                     |
|                 |    * Pipelines in Testing                                                                                                                                   |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Undo            | Reverses the change made                                                                                                                                    |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Redo            | Performs the change again                                                                                                                                   |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delete          | To enable the delete option, click on the node to be deleted. Then hit the delete icon to remove the selected node from the pipeline                        |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pipeline Errors | Displays the errors in the pipeline and highlights any missing configuration in the nodes                                                                   |
|                 |     * **Origins:** The datasource to be used for retrieving data in the pipeline                                                                            |
|                 |     * **Processors:** The type of processor to be used for data processing as per your use case                                                             |
|                 |     * **Segments:** The predefined pipeline segments with preconfigured settings that can be reused while designing a pipeline                              |
|                 |     * **Destinations:** The target node to which the data will be sent towards the end of the pipeline                                                      |
|                 |                                                                                                                                                             | 
|                 |     Selecting a data node type from the drop down located at the top right corner of the screen, populates the relevant nodes corresponding to thatcategory | 
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data Node Type  | Displays the type of data nodes available. This includes:                                                                                                   |
|                 |     * Info                                                                                                                                                  |
|                 |     * Origin Data Schema                                                                                                                                    |
|                 |     * Parameters                                                                                                                                            |
|                 |     * Rejects                                                                                                                                               |
|                 |     * Schedule                                                                                                                                              |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. admonition:: Info

    For detailed information about the data nodes, refer to the **Stage documentation** section.

As you land on the pipeline designer, the first step is to configure the pipeline details. Refer to the relevant section below to view the details to be specified in each configuration tab.

Pipeline Designer Shortcuts
++++++++++++++++++++++++++++++++

While configuring the local pipeline and populating the fields, the following shortcuts can be used to auto-retrieve functions, parameters and context attributes. 

To see it in action, click on the text field in one of the properties panel tab and press the shortcut key(s).

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Shortcut         | Description                                                                                                                                      | 
+==================+==================================================================================================================================================+
| ctrl/cmd + space | Displays the list of functions                                                                                                                   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| $                | Displays the list of predefined pipeline parameters. They can be defined from, the **Parameters** tab                                            |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| @                | Displays the list of pipeline attributes.                                                                                                        |
|                  | **Note**                                                                                                                                         |
|                  | Attributes are subject to change after applying certain processors such as Attribute Renamer, Attribute Remover & Enrich (adding new attributes).|
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Pipeline Design Rules
++++++++++++++++++++++

Once the pipeline has been configured successfully, the next step is to drag and drop the required data nodes and configure the connections. While doing so, the following rules must be kept in mind: 

1. All pipelines must have atleast 1 origin and 1 destination node.

2. All input and output ports must be connected.

3. No individual node must be left unconnected.

Pipeline Settings
++++++++++++++++++++++++

Once the pipeline has been created, it is important that its settings are configured properly. To do so, the fields in the following tabs need to be populated:

* Info
* Origin data schema
* Parameters
* Rejects
* Schedule

A brief description of each is shared below:


Info
------------

The information tab displays all the essential information configured while creating the local pipeline. Any edits required in the pipeline settings can be made here.

.. Note::
    The fields in this section are pre-populated depending on the values entered while creating the local pipeline.

Origin Data Schema
------------------------

The origin data schema tab allows you to specify the schema of the origin data source when designing the pipeline. In order to begin, first you need to specify the type of schema you would like to proceed with. This can be one of the following:

+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Schema Type       | Description                                                                                                                               | 
+===================+===========================================================================================================================================+
| Predefined Schema | Allows you to select from one of the existing and predefined schemas within LigaData Flare. It can be added from the **Schemas** section. |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Extracted Schema  | Allows you to extract the schema from the source data system                                                                              |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Define Schema     | Allows you to define the schema right away                                                                                                |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

To view the fields required to be configured for each schema type, refer to its corresponding section below.


Predefined Schema
++++++++++++++++++++

LigaData Flare allows you to define schemas in the :ref:`Schemas <schemas>` section. These predefined schemas can be called while defining the origin data schema.

To configure this schema, provide the following information:

+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Field         | Description                                                                                                                       | 
+===============+===================================================================================================================================+
| Schema Name   | Select the schema from the dropdown                                                                                               |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Primary Key   | Select one of the attributes as the primary key from the dropdown to be associated with the schema                                |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Constraints   | To add a constraint or say filter/condition, click on the plus icon and provide the following information:                        |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Last Modified | Specifies the timestamp when the directory was last updated or modified                                                           |
|               |    * Name: Specify the name of the constraint                                                                                     |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. Note::
    To delete a constraint, click on the minus icon corresponding to that constraint.

Extracted Schema
++++++++++++++++++++

LigaData Flare allows you to extract the schema from the source data system.

To configure this schema, provide the following information:

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Description                                                                                                                                                                       | 
+=============+===================================================================================================================================================================================+
| Origin      | From the dropdown list of origin datasoruces dragged to and available in the canvas, select the datasource from which the schema needs to be extracted and hit the Extract button | 
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute   | To add an attribute or say data field, click on the plus icon and provide the following information:                                                                              |
|             |   * **Name:** Specify the name of the attribute                                                                                                                                   |
|             |   * **Type:** Specify the type of the attribute from the dropdown                                                                                                                 |
|             |   * **Format:** Specify the format of the attribute. For example, if the attribute is a date, the format could be dd-mm-yyyy, mm/dd/yy or some other format as per your use case  |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Primary Key | Select one of the attributes as the primary key from the dropdown to be associated with the schema                                                                                |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COnstraint  | To add a constraint or say filter/condition, click on the plus icon and provide the following information:                                                                        |
|             |   * **Name:** Specify the name of the constraint                                                                                                                                  | 
|             |   * **Expression:** Provide the expression. It can be either in regex format, a mathematical/logical operation or a function call                                                 |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. Note::
    To delete a constraint/attribute, click on the minus icon corresponding to that constraint/attribute.

Define Schema
+++++++++++++++++++

To configure this schema, provide the following information:

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Description                                                                                                                                                                       | 
+=============+===================================================================================================================================================================================+
| Attribute   | To add an attribute or say data field, click on the plus icon and provide the following information:                                                                              |
|             |   * **Name:** Specify the name of the attribute                                                                                                                                   |
|             |   * **Type:** Specify the type of the attribute from the dropdown                                                                                                                 |
|             |   * **Format:** Specify the format of the attribute. For example, if the attribute is a date, the format could be dd-mm-yyyy, mm/dd/yy or some other format as per your use case  |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Primary Key | Select one of the attributes as the primary key from the dropdown to be associated with the schema                                                                                |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COnstraint  | To add a constraint or say filter/condition, click on the plus icon and provide the following information:                                                                        |
|             |   * **Name:** Specify the name of the constraint                                                                                                                                  |
|             |   * **Expression:** Provide the expression. It can be either in regex format, a mathematical/logical operation or a function call                                                 |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. Note::
    To delete a constraint/attribute, click on the minus icon corresponding to that constraint/attribute.

Parameters
------------
To add a parameter, provide the following information:

+------------+-------------------------------------------+
| Field      | Description                               | 
+============+===========================================+
| Name       | Specify the name of the parameter         |
+------------+-------------------------------------------+
| Value      | Specify the value of the parameter        |
+------------+-------------------------------------------+
| Description| Specify the description of the parameter  |
+------------+-------------------------------------------+


Rejects
------------

.. Note::
    This tab is not available for Cache Pipelines.

To configure rejects, provide the following information:

+---------------------+----------------------------------------------------------+
| Field               | Description                                              | 
+=====================+==========================================================+
| Directory Template  | Specify the directory path to write the rejects to       |
+---------------------+----------------------------------------------------------+
| File Prefix         | Specify the file prefix                                  |
+---------------------+----------------------------------------------------------+
| File Suffix         | Specify the file suffix                                  |
+---------------------+----------------------------------------------------------+
| Data Format         | Specify the format of rejects file from the dropdown     |
+---------------------+----------------------------------------------------------+
| Attribute Delimiter | Specify the character used to separate items in the file |
+---------------------+----------------------------------------------------------+

Schedule
------------

To run the pipeline on a one time basis or periodically, configure the following options:


+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field        | Description                                                                                                                                                            | 
+==============+========================================================================================================================================================================+
| None         | Selecting this option creates a pipeline but never applies it to the selected objects. This option can be used if you don’t want to activate the pipeline immediately  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Once         | Selecting this option runs this pipeline only once                                                                                                                     |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Repeat       | Selecting this option allows you to run the pipeline periodically                                                                                                      |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Date & Time  | Specify the date and time when the pipeline should be executed                                                                                                         |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Repeat Every | Specify the frequency of the pipeline in days, weeks or years                                                                                                          |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Repeat On    | Specify the days on which the pipeline should be executed                                                                                                              |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ends at      | Specify when should the pipeline execution end                                                                                                                         |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. Note::
    To learn about node configurations, refer to the **Stage documentation** section.

Test Local Pipeline
==========================

.. Warning::
    The pipeline must not have the warning sign next to its name and be free of any errors to be eligible for testing.

To place a pipeline publish request, follow the steps below:

1. Click on the **Test** button corresponding to the pipeline to be tested. A dialog box will appear on the screen. 

2. Select the development environment in which the pipeline needs to be deployed for testing. This is a critical step as it will define the connections, caches and the parameters that the pipeline can utilize.

3. Click on the **Deploy** button to proceed.
The pipeline will be successfully deployed for testing.

.. Note::
    The pipelines deployed for testing can be viewed in the :ref:`Pipelines in Testing <pipelinetesting>` page.


Request Pipeline Publish
==========================

.. Warning::
    The pipeline must not have the warning sign next to it and be free of any errors to be eligible for pipeline publish request.

To place a pipeline publish request, follow the steps below:

1. Click on the **Publish** button corresponding to the pipeline to be published. A dialog box will appear on the screen. 

2. Provide details for why the pipeline needs to be published as a note. This is an optional step. 

3. Click on the **Confirm** button to proceed.
A toast message will appear on the screen indicating that a notification will be sent to you once the pipeline request is processed. 

.. Note::
    * The pipelines requested for publishing can be viewed in the :ref:`Pipelines Pending Approval <pipelinepending>`  page.
    * You cannot edit the pipeline once the pipeline publication request has been placed.

Copy Local Pipeline
==========================

To copy a local pipeline, follow the steps below:

1. Click on the copy icon corresponding to the pipeline to be copied. A dialog box will appear on the screen. 

2. Click on the Confirm button to proceed.

The pipeline will be copied successfully.

.. admonition:: Info

    The naming convention of the duplicate pipeline consists of the original name followed by **_copy** as a suffix.

Delete Local Pipeline
==========================

To delete a local pipeline, follow the steps below:

1. Click on the delete icon corresponding to the pipeline to be deleted. A dialog box will appear on the screen. 

2. Click on the **Confirm** button to proceed.
The pipeline will be deleted successfully.

Troubleshooting Local Pipeline
======================================

While working with local pipelines, you might come across some errors while performing certain actions. In this section, you will see the errors associated with local pipelines along with the remediation steps.

.. admonition:: Info

    The error messages mentioned in this section are set by default and can be modified by editing the JSON file. To customize the error messages, refer to the :ref:`Appendix B <Appendixb>`

Error: External API returned an error: Failed to add pipeline
------------------------------------------------------------------

Error: Can’t test this pipeline because there is a pipeline with the same name
------------------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to deploy a local pipeline for testing with the same name as a previously deployed pipeline.

* **Possible Solution:** Edit the pipeline, give it a unique name and try to deploy the pipeline for testing again.

Error: Sql query contains {tblName} parameter but table name is empty
------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to extract schema with an empty table

* **Possible Solution:** Extract the table or schema that is not empty

