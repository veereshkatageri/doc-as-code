.. _how-to_render_doc_as_code_to_html:

How to render doc as code to html (Publish to HTML)
+++++++++++++++++++++++++++++++++++++++++++++++++++

This page is intended to guide you how to render (Publish) the doc as code to HTML format.

.. contents:: Table of contents
    :local:

.. _rendering_html:

Working steps
=============

.. note::

    These instructions will translate the contents from doc as code repositories to html format. \
    During this stage the possible failure messages will be reported in Cmder console. Make sure \
    that warnings and failure messages are fixed.

#. use conan commands as follows.

    .. code-block:: bash

        cd Technical-Documents/onboarding_template/
        python -m venv ./venv
        .\venv\Scripts\activate.bat
        pip install -r requirements.txt
        conan install . -if build
        conan build . -bf build
        .\venv\Scripts\deactivate.bat

#. The above working steps generate the html files under the directory \
   **build\\package\\Doc_as_Code_Tools-DocumentsHtml\\**.

#. **index.html** serves the welcome page. It can be opened in any browser apart from \
   **Internet explorer** in order to visualize the contents.
