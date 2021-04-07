.. _prerequisites:

Prerequisites
=============

This chapter covers the requirements of doc-as-code toolchain. And also it provides the \
installation guide of the required tools.

.. contents:: Table of contents
    :local:

Requirements
------------

.. tip::

    Any editor can be used among VSCode or Notepad++.

.. list-table:: Toolchain
   :widths: auto
   :header-rows: 1

   * - Name
     - Version
     - Link
   * - conemu (Optional)
     - 201101
     - `Download conemu <https://www.fosshub.com/ConEmu.html>`_
   * - VSCode
     - 1.48.2
     - `Download Visual Studio Code <https://code.visualstudio.com/download>`_
   * - Notepad++
     - 7.8.8 release or higher
     - `Download Notepad++ <https://notepad-plus-plus.org/downloads/v7.8.8/>`_
   * - Notepad++ plugin
     - 1.0.0
     - `Download plugin <https://github.com/steenhulthin/reStructuredText_NPP>`_

Installation guide
------------------
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

    cd Technical-Documents/onboarding_guide/
    code .

#. Now VSCode will be opened and it looks as below

    .. figure:: images/doc-as-code/vscode_00.png
        :width: 800px
        :align: center
        :height: 483px
        :figclass: align-center

        Workspace VSCode

#. Click on the option **Open Preview to the Side** as highlighted in **red rectangle**

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
