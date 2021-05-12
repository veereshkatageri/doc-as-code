.. _text_formatting:

Text formatting
+++++++++++++++

This page is intended to show how text can be for formatted using reStructuredText syntax.

.. contents:: Table of contents
    :local:

Inline markup and special characters (e.g., bold, italic, verbatim)
===================================================================

=========== ================================== ==============================
usage          syntax                           HTML rendering
=========== ================================== ==============================
italic      `*italic*`                         *italic*
bold        `**bold**`                         **bold**
link        ```python <www.python.org>`_``     `python <www.python.org>`_
verbatim    ````*````                               ``*``
=========== ================================== ==============================

Headings
========

In this section, the best practise to include Headings will be covered.

.. _reStructuredText_with_label:

reStructuredText with label
---------------------------

.. code-block:: rest

    title
    +++++

    sections
    ========

    subsections
    -----------

    subsubsections
    ______________

    and so on
    ^^^^^^^^^^

.. _restructuredtext_without_label:

reStructuredText without label
------------------------------

The hierarchy of the heading must be changed in a reStructuredText file if it will be included in \
another reStructuredText using the directive **inlcude**.

In order to simplify the explaination, we choose two files. And we name them as follows

#. document_layer_up : this reStructuredText file will import document_layer_down
#. document_layer_down : this reStructuredText file will be imported by document_layer_down

The contents of document_layer_up can be as same as :ref:`reStructuredText_with_label`.

importing a document_layer_down after titles in document_layer_up
__________________________________________________________________

.. code-block:: rest

    title
    =====

    sections
    --------

    subsections
    ___________

importing a document_layer_down after sections in document_layer_up
____________________________________________________________________

.. code-block:: rest

    title
    -----

    sections
    ________

    subsections
    ^^^^^^^^^^^

importing a document_layer_down after subsections in document_layer_up
______________________________________________________________________

.. code-block:: rest

    title
    _____

    sections
    ^^^^^^^^

