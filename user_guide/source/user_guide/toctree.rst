.. _toctree:

toctree
+++++++

This page is intended to show how **toctree** can be used to documentation using reStructuredText \
syntax.

.. contents:: Table of contents
    :local:

This directive inserts a “TOC tree” at the current location. The master documentation (called as \
master_doc in configuration file conf.py) must include this directive in order to implement \
hierarchy tree.

The following code snippet shows the hierarchy tree (folder structure of doc-as-code \
onboarding template)

.. code-block:: rest

    On-boarding guide doc-as-code toolchain
    +++++++++++++++++++++++++++++++++++++++

    .. Hint: add the description or the scope of the document 

    The scope of this document is how to use this On-boarding template to get hands on experience.

    .. Hint: toctree gathers list of subpages. 

    Contents:

    .. toctree::

       source/template_doc_as_code
       source/template_glossary_doc_as_code
       source/template_readme

toctree with maxdepth
=====================

As shown above the table of contents will be inserted with maximum depth of two.

toctree with nummering
======================

To insert section numbers even in HTML output, give the toplevel toctree a numbered option.

.. code-block:: rest

    .. toctree::
       :numbered:

       foo
       bar

Additional options
==================

You can use the ``caption`` option to provide a toctree caption and you can use the ``name`` \
option to provide an implicit target name that can be referenced by using :rst:role:`ref`::

    .. toctree::
       :caption: Table of Contents
       :name: mastertoc

       foo

If you want only the titles of documents in the tree to show up, not other headings of the \
same level, you can use the ``titlesonly`` option::

    .. toctree::
       :titlesonly:

       foo
       bar

You can use "globbing" in toctree directives, by giving the ``glob`` flag option.  All entries are \
then matched against the list of available documents, and matches are inserted into the list \
alphabetically.  Example::

    .. toctree::
       :glob:

       intro*
       recipe/*
       *

To reverse the tree  Example::

    .. toctree::
       :glob:
       :reversed:

       recipe/*

To hide the tree Example::

    .. toctree::
       :glob:
       :reversed:

         recipe/*

You can also give a "hidden" option to the directive, like this::

    .. toctree::
       :hidden:

       doc_1
       doc_2

This will still notify Sphinx of the document hierarchy, but not insert links into the document at \
the location of the directive

In cases where you want to have only one top-level toctree and hide all other
lower level toctrees you can add the "includehidden" option to the top-level
toctree entry::

    .. toctree::
        :includehidden:

        doc_1
        doc_2
