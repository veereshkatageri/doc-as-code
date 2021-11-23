.. _prerequisites:

Prerequisites
=============

This chapter covers the requirements of doc-as-code toolchain. And also it provides the \
installation guide of the required tools.

.. contents:: Table of contents
    :local:

.. _requirements:

Requirements
------------

.. tip::

    Any editor can be used among VSCode or Notepad++. Editor can be used to highlight the \
    syntaxes of reStructuredText and also to preview the reStructuredText files before generating \
    the document. Please note that admin rights are required to install the editors.

.. attention::

    The tools **Graphviz** and **Java** are relevant if it requires to integrate the graphviz and \
    uml diagrams respectively.

.. list-table:: Toolchain
   :widths: auto
   :header-rows: 1

   * - Name
     - Version
     - Link
     - Comments
   * - Cmder
     - v1.3.18
     - `Download fill with Git for Windows <https://github.com/cmderdev/cmder/releases/download/v1.3.18/cmder.zip>`_
     - Mandatory
   * - Chocolatey
     - 0.10.15
     - 
     - Mandatory (Must be installed using PowerShell)
   * - Python
     - 3.6.5 or higher
     - 
     - Mandatory (Must be installed using Chocolatey)
   * - VSCode
     - 1.48.2
     - `Download Visual Studio Code <https://code.visualstudio.com/download>`_
     - Optional (Will allow to preview the reStructuredText)
   * - Notepad++
     - 7.8.8 release or higher
     - `Download Notepad++ <https://notepad-plus-plus.org/downloads/v7.8.8/>`_
     - Optional (Will allow to edit the reStructuredText files easily)
   * - Notepad++ plugin
     - 1.0.0
     - - `Download plugin <https://github.com/steenhulthin/reStructuredText_NPP>`_
       - This plugin highlights the syntax of reStructuredText
     - Optional (Will allow to visualize the syntax)
   * - Graphviz
     - dot - graphviz version 2.38.0 (20140413.2041)
     - - `Download graphviz <https://graphviz.org/download/>`_
       - Any latest stable version
     - Optional (Must be installed to integrate plantuml diagrams)
   * - Java
     - 1.8.0_271
     - - `Offline installation guide <https://java.com/en/download/help/windows_offline_download.html>`_
       - Version as same or higher than :ref:`Java version <java_version>`
     - Optional (Must be installed to integrate plantuml diagrams)

Installation guide
------------------

Cmder
_____

- Download Cmder with the link provided in :ref:`Requirements <requirements>`
- Create a folder called "cmder" under **C:\\Tools\\**
- Copy and paste the contents of "cmder.zip" to **C:\\Tools\\cmder**

.. note::

    The cmder complete version contains the ready to use **git for windows**.

Chocolatey
__________

In order to install python without admin rights, it is required to install Chocolatey. Perform \
the following working steps.

- Create a file called **ChocolateyInstallNonAdmin.ps1** under **C:\\Tools\\**
- Copy and paste the following contents to **ChocolateyInstallNonAdmin.ps1**

.. code-block:: bash

    # Set directory for installation - Chocolatey does not lock
    # down the directory if not the default
    $InstallDir='C:\Tools\chocoportable'
    $env:ChocolateyInstall="$InstallDir"

    # If your PowerShell Execution policy is restrictive, you may
    # not be able to get around that. Try setting your session to
    # Bypass.
    Set-ExecutionPolicy Bypass -Scope Process -Force;

    # All install options - offline, proxy, etc at
    # https://chocolatey.org/install
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

- Open Powershell, go to the location where **ChocolateyInstallNonAdmin.ps1** is located

.. code-block:: bash

    cd C:\Tools

- To setup proxy authentication, run the following command

.. code-block:: bash

    netsh winhttp show proxy

- Run the following command to install Chocolatey

.. code-block:: bash

    .\ChocolateyInstallNonAdmin.ps1

- If installation is successful, the Chocolatey version can be verified by running the following \
  command

.. code-block:: bash

    choco --version

Python
______


If you have already installed python, then this chapter can be skipped. In this chapter, how \
python can be installed without admin rights will be covered.

- Open cmder terminal
- Run the following command

.. code-block:: bash

    choco install python

- If installation is successful, the python version can be verified by running the following \

.. code-block:: bash

    python --version

VSCode
______

VSCode Extensions
^^^^^^^^^^^^^^^^^

The editor VSCode allows to preview the reStructuredText. In order to review, it is required to \
install the extension from **Visual Studio Marketplace**.

#. Make sure that the VSCode is installed
#. Go to the link `Preview <https://marketplace.visualstudio.com/items?itemName=searKing.preview-vscode>`_
#. Install the extension
#. Restart VSCode IDE

Show whitespace characters
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. caution::

    The reStructuredText follows a very strict syntax. To become familiar with the syntax, it will \
    be helpful if additional options are configured in vscode.

#. Open vscode
#. Go to View
#. Make sure **Render whitepsace** is set

In VSCode
_________

#. perform the following steps

  .. code-block:: bash

    git clone -b master https://github.com/SiANOMTech/Technical-Documents.git
    cd Technical-Documents/onboarding_template/
    code .

#. Now VSCode will be opened and it looks as below

    .. figure:: images/doc-as-code/vscode_00.png
        :width: 800px
        :align: center
        :height: 483px
        :figclass: align-center

        Workspace VSCode

#. Click on the option **Open Preview to the Side** as highlighted in **red rectangle**. If you do \
   not find it, use the shortcut **Ctrl+Shift+V**.

    .. figure:: images/doc-as-code/vscode_01.png
        :width: 800px
        :align: center
        :height: 483px
        :figclass: align-center

        Using the preview option

#. Now a separate side tab will be opened as shown below

    .. figure:: images/doc-as-code/vscode_02.png
        :width: 800px
        :align: center
        :height: 483px
        :figclass: align-center

        VScode in Preview mode
