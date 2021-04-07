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
    During this stage the possible failure messages will be reported in conemu console. Make sure \
    that warnings and failure messages are fixed.

.. attention::

    Do not get confused with the name of build folder here i.e, **build-html**. As this page \
    demonstrates the rendering to html format, a meaningful name has been chosen. Any name as per \
    the convenience can be used. 

#. use conan commands as follows.

    .. code-block:: bash

        cd Technical-Documents/onboarding_template/
        mkdir build-html
        cd build-html
        conan install ..
        conan build ..

#. The above working steps generate the html files under the directory \
   **package\\Doc_as_Code_Tools-DocumentsHtml\\**.

#. **index.html** serves the welcome page. It can be opened in any browser in order to preview \
   the contents.
