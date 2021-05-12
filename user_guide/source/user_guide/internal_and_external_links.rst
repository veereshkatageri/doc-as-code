.. _internal_and_external_links:

Internal and External Links
+++++++++++++++++++++++++++

This page is intended to show how Internal and External links can be added to documentation using \
reStructuredText syntax.

.. contents:: Table of contents
    :local:

Types of Links

#. External links (http-like)
#. Implicit links to title
#. Explicit links to user-defined label (e.g., to refer to external titles)

External links with label
=========================

.. code-block:: rest

    `Python <http://www.python.org/>`_

Implicit links to title
=======================

.. caution::

    Implicit links work only within the same document

.. code-block:: rest

    .. _implicit:

    Some chapter
    ============

    Some other chapter
    ==================

    :ref:`implicit`

Explicit links to user-defined label
====================================

.. hint::

    To use explicit links, the label must be present at the beginning of the documentation

.. caution::

    reStructuredText follows a very strict syntax. Label will be defined with prefix underscore \
    for example **_label_foo**. It will be used without prefix using directive **:ref:** for \
    example **:ref:label_foo**

#. Define a label at the beginning of the documentation which is supposed to be used in another \
   documentation as shown below

    .. code-block:: rest

        .. _label_foo:

        Chapter foo
        +++++++++++

        This page is intended to show documentation of foo.

#. Use this label as reference to provide explicit link in another documentation

    .. code-block:: rest

        .. _label_bar:

        Chapter bar
        +++++++++++

        This page is intended to show documentation of bar.

        Read the chapter :ref:`label_foo`
