.. _python_packages:

Python Packages
+++++++++++++++

.. contents:: Table of contents 
    :local:

.. attention::

    This chapter is only relevant if the chapter :ref:`Python <python>` is read and understood.

What is Python package
======================

#. A package is a collection of Python modules.

Why is it required?
===================

We organize a large number of files in different folders and subfolders based on some criteria, so \
that we can find and manage them easily. In the same way, a package in Python takes the concept of \
the modular approach to next logical level. As you know, a module can contain multiple objects, \
such as classes, functions, etc. A package can contain one or more relevant modules. Physically, \
a package is actually a folder containing one or more module files.

How to install python package
=============================

- The general syntax to download a python is as follows

.. code-block:: bash

    pip3 install name_of_the_packages

For example,

.. code-block:: bash

    pip3 install sphinx


Relevant python packages
========================

The following packages are supposed to be installed in order to generate the technical \
documentation.


.. list-table:: Toolchain
   :widths: auto
   :header-rows: 1

   * - Package
     - Version
     - Significance
   * - conan
     - 1.21.3
     - to generate documentation to different targets, ex html, latex and pdf
   * - pyecharts-jupyter-installer
     - 0.0.3
     -
   * - Sphinx
     - 3.3.1
     - to create intelligent and beautiful documentation
   * - sphinx-rtd-theme
     - 0.5.0
     - theme
   * - sphinxcontrib-confluencebuilder
     - 1.2.0
     - to publish documents to commercial wiki (Confluence)
   * - sphinxcontrib-imagesvg
     - 0.1
     - to integrate svg images
   * - sphinxcontrib-plantuml
     - 0.19
     - to integrate uml diagrams
   * - sphinx-git
     - 11.0.0
     - to integrate the git log
   * - sphinx-tabs
     - 1.3.0
     - to integrate tabs
   * - sphinxcontrib-excel
     - 0.0.1
     - to read an excel file
   * - sphinxcontrib-excel-table
     - 1.0.8
     - to display excel sheets
   * - recommonmark
     - 0.6.0
     - to integrate markdown files
   * - sphinx-markdown-tables
     - 0.0.15
     - to integrate markdown tables
   * - sphinxcontrib-spelling
     - 7.0.1
     - to check spellings
   * - sphinx-copybutton
     - 0.3.1
     - to insert copy button for code blocks

Related articles
================

#. `Python - Packages <https://www.tutorialsteacher.com/python/python-package>`_

