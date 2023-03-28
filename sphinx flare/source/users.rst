.. _users:


User Management 
*******************

Overview
=============

The category page within LigaData Flare allows you to manage users and their permissions. It provides the ability to associate the user with roles with predefined permissions so you do not have to manually edit the permissions for each role.

.. admonition:: Info
    
    For detailed information on setting roles and permissions, refer to the Roles :ref:`Roles <roles>` section.

.. figure::  newrole.png
    :align:   center 

Add LDAP User
===============

To add an LDAP user, follow the steps below:

1. Click on the **+ Add LDAP User** button located at the top right corner of the UI. A dialog box will appear on the screen.

2. Provide the following information:

+-------+---------------------------------------------------------------------------+
| Field | Description                                                               | 
+=======+===========================================================================+
| Name  | Click on the dropdown and select the user name to be added                |
+-------+---------------------------------------------------------------------------+
| Role  | Click on the dropdown and select the role to be assigned to the LDAP user |
+-------+---------------------------------------------------------------------------+

3. Click on the **Add** button to proceed.
The user will be added and assigned the selected role successfully.

.. _addnewuser: 

Add New User
==============

To add a new user, follow the steps below:

1. Click on the **+ Add New User** button located at the top right corner of the UI. A dialog box will appear on the screen.

2. Provide the following information:

+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Description                                                                                                                        | 
+=================+====================================================================================================================================+
| Name            | Specify the user name                                                                                                              |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Password        | Specify the password.                                                                                                              |
|                 |                                                                                                                                    |
|                 |  Note                                                                                                                              |
|                 |   * Password length must be between 8 and 128 characters                                                                           |           
|                 |   * Password must contain at least 1 upper case letter, 1 lower case letter, 1 number, 1 special character, and without whitespaces|
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Confirm Password| Re-enter the password.                                                                                                             |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| First Name      | Specify the first name of the user                                                                                                 |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Last Name       | Specify the last name of the user                                                                                                  |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Email           | Specify the user’s email                                                                                                           |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Role            | Click on the dropdown and select the role to be assigned to the user                                                               |
|                 |                                                                                                                                    |
|                 |  Note                                                                                                                              |
|                 |   * The user role assigned to the user must be activated.                                                                          |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Categories      | Click on the dropdown and select the category to be assigned to the user. Multiple categories can be assigned.                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+

3. Click on the **Add** button to proceed.
The user will be added and assigned the selected role successfully.

.. figure::  newuser.png
    :align:   center 

.. figure::  usererror.png
    :align:   center 

Activate / Deactivate User
===============================

To **activate** a user, tick the checkbox under the **Actions** column, corresponding to the user to be activated. A dialog box will appear on the screen to confirm the deactivation. Select **Confirm** to proceed. The user will be activated.

Similarly, to **deactivate** the user, untick the checkbox. A dialog box will appear on the screen to confirm the deactivation. Select **Confirm** to proceed. The user will be deactivated.

Edit User
=============

To edit a user, follow the steps below:

1. Click on the edit icon under the Actions column, corresponding to the user to be edited. A dialog box will appear on the screen.

2. Make the required changes. 

3. Click on the Save button to proceed.
The user will be edited successfully.

.. admonition:: Info

    For information on what these fields mean, refer to the :ref:`Add New User <addnewuser>` section.

Delete User
=============

To delete a user, follow the steps below:

1. Click on the delete icon under the Actions column, corresponding to the user to be deleted. A dialog box will appear on the screen.

2. Select Confirm to proceed.
The user will be deleted successfully.

.. Note::
    To view the deleted users, click on the **Show Deleted Users** button located at the top right corner of the UI. The deleted users will appear in the list.

Troubleshooting
==================

Error: Username already exists
----------------------------------

* **Root Cause:** You may come across this error when trying to enter a username that already exists.

* **Possible Solution:** Try entering a unique username.