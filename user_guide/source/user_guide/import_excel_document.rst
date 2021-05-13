.. _import_excel_document:

Importing excel documents
+++++++++++++++++++++++++

This page is intended to show how to import excel documents in doc-as-code.

.. contents:: Table of contents
    :local:

Reference
=========

Please visit `sphinxcontrib-excel <https://pypi.org/project/sphinxcontrib-excel/>`_

Please visit `sphinxcontrib-excel-table <https://pypi.org/project/sphinxcontrib-excel-table/>`_

Syntax
======

Import excel document
---------------------

The syntax to import the excel document in doc-as-code as follows

.. code-block:: bash

    .. excel-table::
    :file: ../documents/doc-as-code/import_excel.xlsx

It yields to

.. excel-table::
   :file: ../documents/doc-as-code/import_excel.xlsx

Embed csv into your sphinx documentation
----------------------------------------

.. code-block:: bash

    .. pyexcel-table::

        ---pyexcel:example table---
        Name,Age
        Adam,28
        Beatrice,29
        Ceri,30
        Dean,26

It yields to

.. pyexcel-table::

   ---pyexcel:example table---
   Name,Age
   Adam,28
   Beatrice,29
   Ceri,30
   Dean,26