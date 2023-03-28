.. _Appendixb:

Appendix B
*************

Overview
============

LigaData Flare allows you to customize the text on your application and use your business-specific terminologies.

In this section, we will discuss the customization steps in detail.

LigaData Flare provides customization support for the following:

* Customization of error messages using :ref:`labels.properties <labels>`

* Customization of configuration fields for stages using :ref:`stages.properties <stages>`

* Customization of configuration fields for connections using :ref:`connections.properties <connections>`

* Customization of text displayed on the :ref:`Flare UI <ui>`

Executing the following command with the **-labels, -stages and -connections** flags followed by the path of the file, as shown below, will run the UI server with customized text as mentioned above:

.. code::

    java -Dlog4j.configurationFile=log4j2.xml -Dlogback.configurationFile=logback.xml -cp "FlareDISvc_2.12-0.01.00.jar" JettyLauncher -configFile=application.conf -keyWordsFile=keywords.csv -labels=labels.properties -stages=stages.properties -connections=connections.properties > /dev/null 2>&1 &

.. caution::

    * Please make sure that you provide the correct path of where your files with custom text, such as **labels.properties** is located
    * Running the above mentioned command without the **-labels, -stages and -connections** flags will signal the system to use the default messaging

.. _labels:

Error Message Customization
=================================

To customize the error messages displayed in the pop-up dialog boxes, follow the steps below:

1. Open the **labels.properties** file

2. Locate the previously used error message 

3. Replace it with the updated error message

Execute the command shared in the section above with the -labels=<path to labels.properties file> flag to apply the changes.

Example
+++++++++++

    When logging into Flare, if a user enters a wrong username or password, then the default error message that is displayed is **Invalid username or password.**

It can be changed to **Please enter the correct username and password.**


.. _connections:

Connection Fields Customization
====================================

To customize the connection field text displayed in the pop-up dialog boxes when adding a connection in an environment, follow the steps below:

1. Open the **connections.properties** file

2. Locate the previously used field name

3. Replace it with the updated field name

4. Execute the command shared in the section above with the **-connections=<path to connections.properties file>** flag to apply the changes

Example
+++++++++++

When configuring a Kafka connection, the text for Auto Offset Reset field can be updated to **Automatic Offset** Reset based on your preference.

.. _stages:

Stage Field Customization
=================================

To customize the stage field text displayed when configuring a stage, follow the steps below:

1. Open the **stages.properties** file

2. Locate the previously used field name

3. Replace it with the updated field name

4. Execute the command shared in the section above with the **-stages=<path to stages.properties file>** flag to apply the changes

Example
+++++++++++

When configuring the Landing Zone, the text for **Regular Expression** field can be updated to **RegEx** based on your preference.

.. _ui:

Flare UI Customization
=================================

To customize the text displayed on the Flare UI, follow the steps below:

1. Open **FLARE-WEB > out > resources > en.json** file

2. Locate the previously used text

3. Replace it with the updated text

Example
+++++++++++

In the main menu, you can update **In Testing** to **Pipelines In Testing** based on your preference.

.. note::
    Flare doesn’t support the ability to change text for the options displayed in the navigation sidebar
