.. _publishedpipeline:

Published Pipeline in Flare
****************************

Overview
===================

The published pipelines view within LigaData Flare displays a list of pipelines that have been approved and and ready to be deployed.

To access the published pipelines section, select **Published Pipelines** from the main menu. The following view will appear on the screen.

.. figure::  publishedpipelinehome.png
    :align:   center 

.. Note::
    If you do not see these options, you might not have the relevant permissions. For more details, check with your administrator.

Deploy Pipeline
======================

To deploy a published pipeline, follow the steps below:

1. Click on the **Deploy** button under the **Actions** column, corresponding to the pipeline to be tested. A dialog box will appear on the screen.

2. Configure the following values for testing:

    a. **Version:** Select the pipeline version to be deployed

    b. **Environment:** Select the production environment in which the pipeline needs to be deployed. This is a critical step as it will define the connections, caches and the parameters that the pipeline can utilize.

.. Note::
    If the selected environment has no parameters defined, then the parameters/values configures for the selected pipeline will take precedence.

3. Once done, hit the Deploy button.
The pipeline will be added to the Deployed Pipelines page.

.. admonition:: Info

    For more information, refer to the :ref:`Deployed Pipelines <deployedpipeline>` section.

View Pipeline History
===========================

The history icon in Flare displays the list of pipeline versions that exist for the corresponding pipeline. Pipeline versions are created as a result of first, **importing** a certain pipeline and then **publishing** it once again. Repeating this process will result with an increment of the pipeline version. 

To view the previous versions of a pipeline, follow the steps below:

1. Click on the **History** icon under the **Actions** column, corresponding to the pipeline for which the version history needs to be viewed. The following page will appear on the screen with clickable version numbers.

.. figure::  history.png
    :align:   center 

2. Click on the version number that needs to be viewed. 
The pipeline designer view will appear on the screen displaying the pipeline structure and data flows in the selected version.

Import Pipeline
==========================

Using Flare, you can import the current or any previous version of the pipeline, back into the workspace. 

.. Caution::
    A previously imported pipeline cannot be reimported to the same workspace.

Import Latest Version of Pipeline
--------------------------------------------
Under the **Latest Version** column, you’ll notice the number of versions of the pipelines where the latest will be considered when importing or duplicating it.

To import a pipeline, follow the steps below:

1. Click on the **Import** button under the **Actions** column, corresponding to the pipeline to be imported. A dialog box will appear on the screen.

2. Select the workspace from the dropdown, in which the pipeline needs to be imported.

3. Click on the **Import** button to proceed.
The pipeline will be successfully imported as a local pipeline with the same name in the selected workspace.

.. Note::
    If the imported pipeline is published, it will be done so as a **new version** of the original pipeline.

Import Previous Version of Pipeline
------------------------------------------------

To import a previous version of the pipeline, follow the steps below:

1. Click on the **History** icon under the **Actions** column, corresponding to the pipeline for which the previous version needs to be imported. The pipeline versions page will appear on the screen.

2. Click on the **Import** button under the **Actions** column, corresponding to the version number to be imported. A dialog box will appear on the screen.

.. admonition:: Info

    To view the pipeline before importing it, click on the relevant version number. The pipeline will open up in the pipeline designer view.

3. Select the workspace from the dropdown, in which the pipeline needs to be imported.

4. Click on the Import button to proceed.
The selected version of the pipeline will be successfully imported as a local pipeline with the same name in the selected workspace.

.. Note::
    If the imported pipeline is published, it will be done so as a new version of the original pipeline.

Copy Pipeline
==================

To create a duplicate of a pipeline, follow the steps below:

1. Click on the **Copy** icon under the **Actions** column, corresponding to the pipeline that needs to be copied. A dialog box will appear on the screen.

2. Select the workspace from the dropdown, in which the pipeline needs to be copied.

3. Click on the **Duplicate** button to proceed.
A copy of the pipeline will be created in the selected workspace as a local pipeline.

.. admonition:: Info

    The naming convention of the duplicate pipeline consists of the original name followed by **_copy** as a suffix.

Delete Published Pipeline
==============================

To delete a published pipeline, follow the steps below:

1. Click on the delete icon corresponding to the pipeline to be deleted. A dialog box will appear on the screen. 

2. Click on the Confirm button to proceed.

The published pipeline will be deleted successfully.

.. Caution::
    A deployed pipeline cannot be deleted unless it is undeployed. For more information, refer to the **Troubleshooting Published Pipelines** section below.

Troubleshooting Published Pipelines
================================================

While working with published pipelines, you might come across some errors while performing certain actions. In this section, you will see the errors associated with published pipelines along with the remediation steps.

.. Note::
    To customize the error messages, refer to the :ref:`Appendix B <Appendixb>` Customization.

Error: Failed to retrieve published pipeline
------------------------------------------------

* **Root Cause:** You may come across this error when trying to import a published pipeline to a workspace.

* **Possible Solution:** 

Error: External Api returned an error: Failed to add pipeline
------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to deploy a published pipeline.

* **Possible Solution:** 

Error: Incompatible environment, can’t deploy pipeline.
------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to deploy a published pipeline.

* **Possible Solution:** Revisit the production environment configuration in which the pipeline needs to be deployed.

Error: Invalid connection name
-------------------------------------------

* **Root Cause:** You may come across this error when trying to deploy a published pipeline.

* **Possible Solution:** Revisit the connection settings for the production environment in which the pipeline needs to be deployed.

Error: This pipeline can't be deleted as it has been deployed
------------------------------------------------------------------------

* **Root Cause:** You may come across this error when trying to deleted a published pipeline that has been deployed.

* **Possible Solution:** Undeploy the pipeline from the Deployed Pipelines page and try to delete the pipeline again.