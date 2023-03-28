.. _workflows:

Workflows
*******************

Initial Steps with Flare
==========================

Once Flare has been successfully installed, it is important to look into the basic configurations and set up the necessary items required for creating and running a pipeline, as per your business requirements.

In this section, we will explore the necessary steps to be followed to set up Flare.


Create and Activate the Role
--------------------------------

As an administrator, the first thing that needs to be created on Flare is the user role. These roles define permissions at granular level for each section related to pipelines, environments, schemas, etc within Flare.

User Roles provide a means to creating team specific roles such as pipeline designer, pipeline testers, admin, super admin, etc as per your organization’s team structure. Relevant roles then can be assigned to the team members depending upon the access to the platform they might need.

.. figure::  activaterole.png
    :align:   center 

.. admonition:: Info
    
    To learn more about it, refer to the :ref:`Roles in Flare <roles>` section.

Once a role has been created, it is important to activate that role. To do so, mark the checkbox corresponding to the role name, under the **Actions** column.

The role will be activated and all set to be assigned to users.
    
    

Create a Category
--------------------------------

Once the user roles have been defined, the next step is to create categories. These categories act as a way to classify the pipelines based upon their focus area or a custom category such as Accounting, Operations, etc. at the time of creation. While creating a user, you can specify the categories that the user can use to assign the pipelines.

.. admonition:: Info
    
    To learn more about it, refer to the :ref:`Categories <categories>` section.

Create and Activate User
--------------------------------

Once the above-mentioned sections have been configured, your team will need access to Flare to design, test and deploy pipelines followed by some other necessary configurations, also discussed below.

While creating a user, make sure that you assign them to the most relevant role and mark all the categories that user must be able to use.

.. admonition:: Info
    
    To learn more about how to add users, refer to the :ref:`Users <users>` section.

Configure an Environment
--------------------------------

Before beginning with any kind of pipeline design or testing, it is important to have relevant environments for staging, development, and production so the pipeline operations can be conducted successfully while utilizing all the relevant connections, caches, and parameters.

.. admonition:: Info
    
    To learn how to create an environment, refer to the :ref:`Environment <environments>` section.

Create a Workspace
--------------------------------

All the pipelines within Flare are confined to a specific workspace, hence, it is important to have a workspace in place to be able to create a pipeline. You can also create multiple workspaces to manage pipelines efficiently.

.. admonition:: Info
    
   To learn how to create a workspace, refer to the :ref:`Workspace <workspace>` section.

Configure Schema
--------------------------------

Flare provides the ability to either import an existing schema, extract part of it or define a schema when creating a pipeline. To make the best out of these options, it is important to make sure all the relevant schemas have already been configured within Flare.

.. admonition:: Info
    
    To learn how to configure a schema, refer to the :ref:`Schemas <schemas>` section.

Design and Deploy a Pipeline
--------------------------------

Designing a pipeline is the most crucial part of the entire process of data operations management as it defines the data flow. Flare offers a drag-and-drop type canvas that allows you to define the source, processor and destination stages to be used for data in-flow and out-flow. 

Once a pipeline has been created, stages connected and setting configured, the next step is to place a place a pipeline publication request. As a user with privileged access, you can test the pipeline before approving or decline it right away. Approved pipelines can then further be published and deployed.

.. admonition:: Info
    
    To learn how to configure a pipeline from scratch, refer to the :ref:`Pipelines <pipelines>` section.