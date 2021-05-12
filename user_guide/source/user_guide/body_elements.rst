.. _body_elements:

Additional body elements
++++++++++++++++++++++++

This page is intended to show how **Additional body elements** can be used to documentation using \
reStructuredText syntax.

.. contents:: Table of contents
    :local:

contents
========

The directive content is used to display the table of contents.

Implicit contents
-----------------

The example is

.. code-block:: bash

    .. contents::

This yields to

.. contents::

Explicit contents
-----------------

The example is

.. code-block:: bash

    .. contents:: Table of contents

This yields to

.. contents:: Table of contents

container
=========

a container with a custom class, useful to generate an outer <div> in HTML)

For example::

.. container:: custom

   This paragraph might be rendered in a custom way.

rubric
======

It can be used to prepare footnotes. Apart from that it is used to mention a heading or headings \
without any relation to documentation sectioning.

Here is the example of rubric syntax usage

Defining a rubric in the documentation
--------------------------------------
.. code-block:: bash

    [#rubric_example]_ will be linked to footnotes

Using rubric in footnotes to render the reference
-------------------------------------------------

.. code-block:: bash

    .. rubric:: Footnotes

    .. [#rubric_example] linked from chapter rubric

It yields to

[#rubric_example]_ will be linked to footnotes

.. _topic:

topic, sidebar
==============

topic
-----

This directive will allow to write a title and a text together.

Example::

    .. topic:: My topic is foo

        Without bar, foo can not be documented.

The above example results in

.. topic:: My topic is foo

    Without bar, foo can not be documented.

sidebar
-------
It is used to provide parallel documents in within same documentation.

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

The syntax to use sidebar will be and it will be rendered as,

.. code-block:: bash

    .. sidebar:: Optional Sidebar Title
       :subtitle: Optional Sidebar Subtitle

       Subsequent indented lines comprise
       the body of the sidebar, and are
       interpreted as body elements.


parsed-literal
==============

literal block that supports inline markup. For more info visit \
`parsed-literal <lhttp://docutils.sourceforge.net/docs/ref/rst/directives.html#parsed-literal>`_

epigraph
========

a block quote with optional attribution line. For more info visit \
`epigraph <http://docutils.sourceforge.net/docs/ref/rst/directives.html#epigraph>`_

highlights, pull-quote
======================

block quotes with their own class attribute. For more info visit \
`highlights <http://docutils.sourceforge.net/docs/ref/rst/directives.html#highlights>`_ and \
`pull-quote <http://docutils.sourceforge.net/docs/ref/rst/directives.html#pull-quote>`_

compound
========

a compound paragraph. For more info, visit \
`compound <http://docutils.sourceforge.net/docs/ref/rst/directives.html#compound-paragraph>`_


.. rubric:: Footnotes

.. [#rubric_example] linked from chapter rubric
