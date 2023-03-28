.. _roles:


Roles
**************

Overview
=============

LigaData Flare provides role based access controls to its users. This allows the administrator to create separate user roles for different teams such as QA, DevOps, Pipeline designers, etc that require access to the system.

.. figure::  roles.png
    :align:   center 

.. _addnewrole:

Add New Role
=============

To add a new role, follow the steps below:

1. Click on the + Add New Role button located at the top right corner of the UI. 
A dialog box will appear on the screen.

2. Provide the following information:

.. figure::  rolesnew.png
    :align:   center 

New Role
^^^^^^^^^^

+---------------+----------------------------------+
| Field         | Description                      | 
+===============+==================================+
| Name          | Specify the category name        |
+---------------+----------------------------------+
| Description   | Specify the category description |
+---------------+----------------------------------+

.. Note::
    Tick the desired checkboxes relevant to the role.

Edit Role
=============

To edit a role, follow the steps below:

1. Click on the **edit** icon under the **Actions** column, corresponding to the role to be edited. 
A dialog box will appear on the screen.

2. Make the required changes. 

+---------------------+-----------------+------------------------------------------------------------------------+
| Type                | Permissions     | Description                                                            | 
+=====================+=================+========================================================================+
| Local Pipelines     | Add/Edit/Delete | Allows the user to add, edit and delete a local pipeline               |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Publish         | Allows the user to create a publish request to publish the pipeline    |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Deploy          |                                                                        |
+---------------------+-----------------+------------------------------------------------------------------------+
| Pending Pipelines   | View            | Displays the list of pending pipelines                                 |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Approve/Reject  | Allows the user to approve or reject a pipeline                        |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Deploy          |                                                                        |
+---------------------+-----------------+------------------------------------------------------------------------+
| Published Pipelines | View            | Displays the lists of published pipelines                              |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Import          | Allows the user to import pipelines                                    |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Deploy          | Allows the user to deploy a published pipeline                         |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | History         | Displays the pipeline versions                                         |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Delete          | Allows the user to delete a published pipeline                         |
+---------------------+-----------------+------------------------------------------------------------------------+
| Deployed Pipelines  | View            | Displays the list of deployed pipelines                                |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Start/Stop      | Allows the user to run a deployed pipeline and stop a running pipeline |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | History/Status  | Displays the status of the pipeline                                    |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Undeploy        | Allows the user to undeploy the pipeline                               |
+---------------------+-----------------+------------------------------------------------------------------------+
| Pipelines in Testing|                 |                                                                        |
+---------------------+-----------------+------------------------------------------------------------------------+
| Roles               | View            | Display the list of existing roles                                     |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Add/Edit/Delete | Allows the user to create, edit and delete a role                      |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Enable/Disable  | Allows the user to activate or deactivate a role                       |
+---------------------+-----------------+------------------------------------------------------------------------+
| Users               | View            | Display the list of existing users                                     |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Add/Edit/Delete | Allows the user to create, edit and delete a user                      |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Enable/Disable  | Allows the user to activate or deactivate a user                       |
+---------------------+-----------------+------------------------------------------------------------------------+
| Environments        | View            | Displays the list of existing environments                             |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Add/Edit/Delete | Allows the user to add, edit and delete an environment                 |
+---------------------+-----------------+------------------------------------------------------------------------+
| Categories          | View            | Displays the list of existing categories                               |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Add/Edit/Delete | Allows the user to add, edit and delete a category                     |
+---------------------+-----------------+------------------------------------------------------------------------+
| Schemas             | View            | Displays the list of schema                                            |
+---------------------+-----------------+------------------------------------------------------------------------+
|                     | Add/Edit/Delete | Allows the user to add, edit and delete a schema                       |
+---------------------+-----------------+------------------------------------------------------------------------+

3. Click on the **Save** button to proceed.
The role will be edited successfully.

.. admonition:: Info

    For information on what these fields mean, refer to the :ref:`Add New Role <addnewrole>` section.

Activate / Deactivate Role
===============================

To **activate** a role, tick the checkbox under the **Actions** column, corresponding to the role to be activated. A dialog box will appear on the screen to confirm the deactivation. Select **Confirm** to proceed. The role will be activated.

Similarly, to **deactivate** the role, untick the checkbox. A dialog box will appear on the screen to confirm the deactivation. Select **Confirm** to proceed. The role will be deactivated.

.. Warning::
    Deactivating a role will deactivate all the users associated with that role.

Delete Role
=============

To delete a user, follow the steps below:

1. Click on the **delete** icon under the **Actions** column, corresponding to the role to be deleted. A dialog box will appear on the screen.

2. Select **Confirm** to proceed.
The role will be deleted successfully

.. Note::
    The role associated with a user cannot be deleted. The user must be assigned to a different role to delete that role.