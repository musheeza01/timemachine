.. _environments:

Environments
**************

Overview
====================

LigaData Flare provides you with the ability to create various environments to design, execute and test your pipelines without having to disrupt the production environment. 

You can create the following three types of environments:

* **Development:** Used by pipeline designers to create and test local pipelines while designing them

* **Staging:** Used to test pipelines pending approval before approving or declining the pipeline publication request

* **Production:** Used to deploy a published pipeline and process real data

To access the Environment page, click on the **Environments** widget. The following view will appear on the screen.

.. figure::  environment.png
    :align:   center 

Create Environment
====================

To create an environment, follow the steps below:

1. Click on the + Create New Environment button located at the top right corner of the screen. The new environment page will appear on the screen with the following fields.

.. figure::  createenvironment.png
    :align:   center 

2. Provide the following information:

General Information
---------------------

+-------------+--------------------------------------------------------------------------------------------------------------------+
| Field       | Description                                                                                                        | 
+=============+====================================================================================================================+
| Name        | Specify the name of the environment                                                                                |
+-------------+--------------------------------------------------------------------------------------------------------------------+
| Description | Provide the purpose of the environment                                                                             |
+-------------+--------------------------------------------------------------------------------------------------------------------+
| URL         | Specify the server URL to be used for this specific environment. The URL must be provided in the following format: |
|             |                                                                                                                    |
|             | **http://** <localhost or IP> **:** <Port number> **/** <path>                                                     |
|             |                                                                                                                    |
|             | For example,                                                                                                       |
|             |                                                                                                                    |
|             | http://172.168.10.1:8000/env                                                                                       |
+-------------+--------------------------------------------------------------------------------------------------------------------+
| Type        | Select the type of environment to be created from the dropdown. This can be one of the following:                  |
|             |     * **Development:** For designing and testing local pipelines                                                   |
|             |     * **Staging:** For testing pipelines to be published                                                           |
|             |     * **Production:** For running pipelines in production with real data                                           |
+-------------+--------------------------------------------------------------------------------------------------------------------+

The environment will be created successfully. However, it is important to edit the environment and configure the parameters, connections and cache settings. To do so, refer to the Edit Environment section below.

Edit Environment
====================

Technically, an environment is fully configured once the following actions are performed:

* Creating connections to its various data origins and destinations

* Adding parameters to the environment

* Associating caches and linking it to attributes

The details on how these settings are configured via UI is shared in this section.

To edit an environment, follow the steps below:

Click on the **Edit** icon under the **Actions** column, corresponding to the environment to be edited. The edit environment page will appear on the screen. Refer to the relevant sections below to make the required changes. 

Parameters
-------------

The parameters tab is the default tab of the **Edit Environment** page. Using this view, you can add, edit and delete parameters.

Add Parameter
++++++++++++++++

To add a new parameter, enter the required information as described in the table below:

+-------------+------------------------------------------+
| Field       | Description                              | 
+=============+==========================================+
| Name        | Specify the name of the parameter        |
+-------------+------------------------------------------+
| Value       | Specify the value of the parameter       |
+-------------+------------------------------------------+
| Description | Specify the description of the parameter |
+-------------+------------------------------------------+

Click on the plus icon to proceed. The parameter will successfully be added.

Edit Parameter
++++++++++++++++

To edit a parameter, follow the steps below:

1. Click on the edit icon corresponding to the parameter name, under the **Actions** column.

2. Make the required edits.

3. Click on the **Save** icon.

The parameter will be updated successfully.

Delete Parameter
+++++++++++++++++

To delete a parameter, follow the steps below:

1. Click on the **delete** icon corresponding to the parameter name, under the **Actions** column. A dialog box will appear on the screen.

2. Select **Confirm** to proceed.

The parameter will be deleted successfully.

Connections
--------------

When creating an environment, it is important to specify the connections linking the origins to destinations. The capability to define the data flow makes connections an integral part of configuring an environment.

To view this section, click on the **Connections** tab right next to the **Parameters** tab.

Using this tab, you can add, edit and delete connections, which can then further be used while configuring the stages within a pipeline.

.. admonition:: Info

    Currently, the connections can be added for the following stages only:
    * HDFS
    * Impala
    * Kafka
    * MySQL
    * Oracle
    * PostgreSQL
    * Teradata
    * UDP

Add Connection
++++++++++++++++

To add a new connection, click on the **+ Add Connection** button. A dialog box will appear on the screen. Enter the required information, as described in the table below:

+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field  | Description                                                                                                                                                                             | 
+========+=========================================================================================================================================================================================+
| Name   | Specify a unique name for the connection.                                                                                                                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type   | Select the stage from the dropdown, for which the connection needs to be created. Doing so will reveal the configuration fields that needs to be filled, specific to the selected stage.|
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Refer to the relevant section below to fill in the specific details:

HDFS
^^^^^^^

When adding a connection for HDFS, the following fields need to be populated:

+--------------------+----------------------------------------------------------------------------------------------------+
| Field              | Description                                                                                        | 
+====================+====================================================================================================+
| URL                | Specify the URL to access HDFS in the following format: http://<Domain name or IP address>         |
|                    |                                                                                                    |
|                    | Example: http://171.163.1.8/hdfs                                                                   |
+--------------------+----------------------------------------------------------------------------------------------------+
| Configuration File | Specify the path of the configuration file in the following format: file:<path>                    |
|                    |                                                                                                    |
|                    | Example: file://home/file1.xml                                                                     |
+--------------------+----------------------------------------------------------------------------------------------------+
| Authentication File| Select the type of authentication from the dropdown. The following options are supported for HDFS: |
|                    |  * Simple                                                                                          |
|                    |  * Kerberos: If selected, the following fields need to be specified:                               |
|                    |      * Principal: Specify the email to be used for authentication.                                 |
|                    |      * Keytab: Specify the path for the keytab file. Example:                                      |
|                    |                                                                                                    |
|                    |        /opt/Flare/DIService/someUser.keytab                                                        |
|                    |                                                                                                    |
+--------------------+----------------------------------------------------------------------------------------------------+
| HDFS Config        | To add a new HDFS key, click on the plus icon and provide the following information:               |
|                    |  * Key: Specify the name of the key                                                                |
|                    |  * Value: Specify the value of the key                                                             |
+--------------------+----------------------------------------------------------------------------------------------------+

Click on **Add** to proceed. The connection will successfully be added.

Impala/MySQL/Oracle/PostreSQL/Teradata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When adding a connection for Impala, the following fields need to be populated:


+--------------------+----------------------------------------------------------------------------------------------+
| Field              | Description                                                                                  | 
+====================+==============================================================================================+
| Connection String  | Specify the Specify the connection string.                                                   |
+--------------------+----------------------------------------------------------------------------------------------+
| Authentication Type| Select the type of authentication:                                                           |
|                    |  * **User name and password:** Allows to authenticate to Impala using username and password. |
|                    |  * **Other:** Allows to authenticate using other methods such as Kerberos, JaaS etc.         |
+--------------------+----------------------------------------------------------------------------------------------+

Click on **Add** to proceed. The connection will successfully be added.

Kafka
^^^^^^^^

When adding a connection for Kafka, the following fields need to be populated:

+---------------------------+----------------------------------------------------------------------------------------------+
| Field                     | Description                                                                                  | 
+===========================+==============================================================================================+
| Bootstrap Servers         | Multiple servers can also be added.                                                          |
+---------------------------+----------------------------------------------------------------------------------------------+
| Security Protocol         |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Sasl Mechanism            |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Sasl Kerberos Service Name|                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Max Outstanding Messages  |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| ABlock On Buffer Full     |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Linger Ms                 |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Auto Offset Reset         |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+
| Enable Auto Commit        |                                                                                              |
+---------------------------+----------------------------------------------------------------------------------------------+

Click on **Add** to proceed. The connection will successfully be added.

UDP
^^^^^^^
When adding a connection for UDP, the following field needs to be populated:

+-------------+-------------------------------------------------------------------+
| Field       | Description                                                       | 
+=============+===================================================================+
| Port Number | Specify the port number to be used for establishing a connection. |
+-------------+-------------------------------------------------------------------+

Click on **Add** to proceed. The connection will successfully be added.

Caches
====================

The Caches tab is located next to the Connections tab in the **Edit Environment** page. Click on this tab to view the available options. 

Using this tab, you can add, edit and delete caches.

Add Cache
----------

To add a new cache, click on the + Add Cache button. A dialog box will appear on the screen. Enter the required information, as described in the table below:

+-----------+------------------------------------------------------------------------------------------------------------------+
| Field     | Description                                                                                                      | 
+===========+==================================================================================================================+
| Name      | Specify a unique name of the cache.                                                                              |
+-----------+------------------------------------------------------------------------------------------------------------------+
| Cache Key | Select the attribute to be specified as the cache key from the dropdown.                                         |
|           | If you do not see the desired attribute, you can add a new attribute first and then select it from the dropdown. |
+-----------+------------------------------------------------------------------------------------------------------------------+
| Attriutes | To add a new attribute, click on the plus icon and provide the following information:                            |
|           |   * **Name:** Specify the name of the attribute                                                                  |
|           |   * **Data Type:** Specify the type of the attribute from the dropdown                                           |
+-----------+------------------------------------------------------------------------------------------------------------------+

Click on **Create** to proceed. The cache will successfully be added.

Delete Environment
====================

To delete an environment, follow the steps below:

1. Click on the **Delete** icon under the **Actions** column, corresponding to the environment to be deleted. A dialog box will appear on the screen.

2. Click on the **Save** button to proceed.
The environment will be deleted successfully.

.. Note::
    An environment cannot be deleted unless all the pipelines within that environment are deleted.

Troubleshooting
====================

While working with environments, you might come across some errors while performing certain actions. In this section, you will see the errors associated with environments along with the remediation steps.

.. admonition:: Info

    The error messages mentioned in this section are set by default and can be modified by editing the JSON file. To customize the error messages, refer to the :ref:`Appendix B Customization <Appendixb>`

Error: Invalid Environment URL
--------------------------------

* **Root Cause:** You may come across this error when trying to enter an invalid Environment URL.

* **Possible Solution:** Try entering a valid Environment URL that exists.

Error: Invalid Environment URL
-----------------------------------

* **Root Cause:** You may come across this error when trying to enter an URL of Environment that does not exist or may have been deleted.

* **Possible Solution:** Try entering a valid Environment URL that exists.

Error: This environment can't be deleted as pipelines are deployed to it
------------------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to delete an Environment with pipelines deployed to it.

* **Possible Solution:** Try deleting the pipelines deployed to the environment and then delete the Environment.

Error: Cache already exists
--------------------------------

* **Root Cause:** You may come across this error when trying to name a cache that already exists.

* **Possible Solution:** Try adding a cache with a unique name.

Error: Connection already exists
------------------------------------------

* **Root Cause:** You may come across this error when trying to name a connection that already exists.

* **Possible Solution:** Try creating a connection with a unique name.

Error: Used connection can’t be updated/removed
--------------------------------------------------------

* **Root Cause:** You may come across this error when trying to edit or remove a connection that is already in use.

* **Possible Solution:** Remove the connection from all stages/pipelines and try again.