.. _including_markdown:

Including markdown files
++++++++++++++++++++++++

This page is intended to cover how to import the markdown files into doc as code.

.. contents:: Table of contents
    :local:

Reference
=========

- Please visit `Markdown sphinx <https://www.sphinx-doc.org/en/master/usage/markdown.html>`_
- Please visit `Markdown guide <https://www.markdownguide.org/basic-syntax/>`_

Instructions
============

Including markdown file to IncludeLists.csv
-------------------------------------------

1. Imaging the name of the markdown file is hello_world.md and the contents of the \
   IncludeLists.csv in the same directory as follows

.. code-block:: bash

    #file_name;generate_html;publish_confluence;
    body_elements.rst;True;True;

where
- #file_name is the name of the file or folder
- generate_html is the boolean value if set true the documentation will be included to target html
- publish_confluence is the boolean value if set true the documentation will be published to confluence

2. The hello_world.md must be mentioned in the IncludeLists.csv as follows

.. code-block:: bash

    #file_name;generate_html;publish_confluence;
    body_elements.rst;True;True;
    hello_world.md;True;True;

FAQ
===

.. note::

    Only existing Readme.md files were used in order to support markdown files of same workspace. \
    In case of any issue, please create support ticket.