.. _pipelinepending:

Pipeline Pending Approval
****************************

Overview
=============

The pending pipelines view within LigaData Flare displays a list of pipelines that have been created and are pending approval.

The following are the potential source of pending pipelines that are displayed in the screenshot below:

* **Local Pipelines:** The locally created pipelines for which the publication request is received is listed here

* **Pipelines in Testing:** The undeployed pipelines put into test from the pending pipelines section are listed back here.

To access the pending pipelines section, select **Pipelines Pending Approval** from the main menu. The following view will appear on the screen.

.. figure::  pipelinependingapprove.png
    :align:   center 

Test Pipeline
=======================

LigaData Flare provides the ability to test your local pipelines directly from the workspace or from the pipelines pending approval page. Doing so, allows you to verify if the pipeline is running as expected and anything that might be offtrack can be identified immediately.

To put a pending pipeline to test, follow the steps below:

1. Click on the **Test** button under the **Actions** column, corresponding to the pipeline to be tested. A dialog box will appear on the screen.

2. Configure the following values for testing:

    a. **Version:** Select the pipeline version

    b. **Environment:** Select the staging environment in which the pipeline needs to be tested. This is a critical step as it will define the connections, caches and the parameters that the pipeline can utilize.

3. Once done, hit the **Deploy** button.
The pipeline will be moved to the Pipelines in Testing page.

.. admonition:: Info

    For more information, refer to the :ref:`Pipelines in Testing <pipelinetesting>` section.

Approve or Decline Pipeline
==================================

To approve or decline a pipeline, follow the steps below:

1. Click on the Details button under the Actions column, corresponding to the pipeline to be approved or declined. A dialog box will appear on the screen with the following information:

+--------------+-------------------------------------------------------------------------------------------------------------------+
| Field        | Description                                                                                                       | 
+==============+===================================================================================================================+
| User Name    | Name of the pipeline creator                                                                                      |
+--------------+-------------------------------------------------------------------------------------------------------------------+
| Pipeline Name| Name of the pipeline. Clicking on the **View** button takes you to the non editable mode of the pipeline designer.|
+--------------+-------------------------------------------------------------------------------------------------------------------+
| Email        | Email of the pipeline creator                                                                                     |
+--------------+-------------------------------------------------------------------------------------------------------------------+
| Request Date | Timestamp for when the request was submitted                                                                      |
+--------------+-------------------------------------------------------------------------------------------------------------------+
| User Note    | Note typed by the pipeline creator at the time of submitting approval request                                     |
+--------------+-------------------------------------------------------------------------------------------------------------------+
| Note         | Note to be included when approving or declining a pipeline publication request.                                   |
+--------------+-------------------------------------------------------------------------------------------------------------------+

2. In the **Note** field, type a brief note on why the pipeline is being approved or declined.

3. Click on **Approve** or **Decline** as per your use case. A dialog box will appear on the screen.

4. Select **Confirm** to proceed.

If **approved**, the pipeline will be moved to the Published Pipelines page and if declined, the pipeline will be moved back to the Local Pipelines page.

.. admonition:: Info
    
    For more information, refer to the :ref:`Published Pipelines <publishedpipeline>` section.

Troubleshooting
========================

While working with the pipelines pending approval, you might come across some errors while performing certain actions. In this section, you will see the errors associated with the pipelines pending approval along with the remediation steps.

.. admonition:: Info

    The error messages mentioned in this section are set by default and can be modified by editing the JSON file. To customize the error messages, refer to the :ref:`Appendix B Customization <Appendixb>`

Error: Can’t approve a pipeline in testing
---------------------------------------------

* **Root Cause:**  You may come across this error when trying to approve a local pipeline in testing stage.

* **Possible Solution:** Stop the pipeline from testing and undeploy it to bring it back to the pipelines pending approval page.

Error: Please undeploy pipeline before approving
--------------------------------------------------

* **Root Cause:**  You may come across this error when trying to approve a local pipeline in testing stage.

* **Possible Solution:** Undeploy the pipeline and try to approve the pipeline again.

Error: Incompatible environment, can't deploy pipeline
---------------------------------------------------------

* **Root Cause:** You may come across this error when trying to approve a local pipeline with environment settings not configured properly

* **Possible Solution:** Edit the relevant environment and fix any misconfigurations.

Error: Invalid connection name
--------------------------------

* **Root Cause:** You may come across this error when trying to approve a local pipeline with environment settings not configured properly

* **Possible Solution:** Edit the relevant environment and fix the connection name.