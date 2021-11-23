.. _how-to_render_doc_as_code_to_pdf:

How to render doc-as-code to pdf (Publish to PDF)?
++++++++++++++++++++++++++++++++++++++++++++++++++

This page is intended to guide you how to render (Publish) the doc-as-code to PDF format.

.. contents:: Table of contents
    :local:

Requirements
============

.. note::

    Even though sphinx provides a publishing mechanism to pdf directly, the outcome of publish \
    mechanism is not as good as the publishing the pdf documents from latex. Thus in this chapter \
    the workaround has been documented.

    Using doc-as-code toolchain along with additional tools will allow to publish the documents in \
    PDF format.

#. Install `MikTex 2.9 <https://miktex.org/download>`_
#. Update the system environment variable in order to the include MikTex path. For example if the \
   miktex has been installed under directory C:\\Tools\\, then the path \
   **C:\\Tools\\MiKTeX 2.9\\miktex\\bin** must be included in system environment variable.

.. _rendering_pdf:

Working steps
=============

#. use conan commands as follows.

    .. code-block:: bash

        cd Technical-Documents/onboarding_template/
        python -m venv ./venv
        .\venv\Scripts\activate.bat
        pip install -r requirements.txt
        conan install . -if build -o generate_pdf=True
        conan build . -bf build
        .\venv\Scripts\deactivate.bat

#. The above working steps generate the pdf file **Doc-as-Code-Tools-Documents.pdf** under the \
   directory **build\\package\\\Doc-as-Code-Tools-Documents-PDF\\**.

