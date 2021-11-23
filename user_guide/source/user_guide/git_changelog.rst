.. _git_changelog:

Git changelog
+++++++++++++

This page is intended to show how git changelog can be included to doc-as-code.

.. contents:: Table of contents
    :local:

Reference
=========

Please visit the `sphinx-git <https://sphinx-git.readthedocs.io/en/latest/using.html>`_

Syntax
======

1. The following code block shows the syntax of using git changelog to doc-as-code.

.. code-block:: rest

    .. git_changelog::

It yields

.. git_changelog::

2. The git changelog also allows to restrict the total number of recent commits

.. code-block:: rest

    .. git_changelog::
        :revisions: 5

It yields

.. git_changelog::
    :revisions: 5