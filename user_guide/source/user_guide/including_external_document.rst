.. _including_external_document:

Including external document (rst inside another rst)
++++++++++++++++++++++++++++++++++++++++++++++++++++

This page is intended to show how to include external documents (rst in rst) reStructuredText \
syntax.

.. contents:: Table of contents

What should I be aware of before embedding external document?
=============================================================

If any external document will be included using reStructuredText directive **include**, it brings \
certain drawback with existing doc-as-code templates.

Here the external document (.rst file) **example_including_external_document.rst** has been used \
to showcase the advantages, disadvantages and workarounds.

Example
-------

The contents of the external document as follows

.. code-block:: bash

    .. _example_including_external_document:

    Example Including external document
    +++++++++++++++++++++++++++++++++++

    This page will be included by external documents using the directive **include**.


If we try to embed the document as it is, if leads to following warning


.. code-block:: bash

    ../step_by_step_guide/example_including_external_document.rst:4: WARNING: duplicate label example_including_external_document, other instance in ..\example_including_external_document.rst

It means the reStructuredText does not recommend to include an external document if it has been \
defined with a label.

Modifying the content
---------------------

In such scenario it requires to remove the label from the external document. The modified content \
of the external document is as shown below

.. code-block:: bash

    Example Including external document
    +++++++++++++++++++++++++++++++++++

    This page will be included by external documents using the directive **include**.

Table of contents
-----------------

If it is required to display the contents of external document, please make sure that directive \
**.. contents::** will be used precisely in order to avoid the confusions.

In embedding document
_____________________

The doc as code template mentions to the use the directive **.. contents::** as follows

.. code-block:: bash

    .. contents:: Table of contents
        :local:

In this scenario, the directive must be used as follows

.. code-block:: bash

    .. contents:: Table of contents

In external document
____________________

It is required to use the directive **.. contents::** as mentioned by doc as code \
template. i.e, 

.. code-block:: bash

    .. contents:: Table of contents
        :local:

IncludeLists.csv and toctree
----------------------------

.. attention::

    If it is required to embed an external document using include directive, please make sure that \
    the embedded document will not be included in both IncludeLists.csv and toctree document.

Embedding one external document
===============================

The syntax in order to embedded only one external document is as follows

.. code-block:: bash

    .. include:: example_including_external_document.rst

Embedding multiple external document
====================================

Adjusting directive contents
----------------------------

Embedding nested external documents or embedding multiple external documents are recommended if \
and only if the table of contents are not required. It is known issue of reStructuredText \
directive **.. contents:** that it does not support the indexing of nested external documents.

For example, consider there are three documents as follows

.. code-block:: bash

    example_including_external_document_level_1.rst
    example_including_external_document_level_2.rst
    example_including_external_document_level_3.rst

The first document example_including_external_document_level_1.rst includes the external document \
example_including_external_document_level_2.rst and \
example_including_external_document_level_2.rst includes \
example_including_external_document_level_3.rst so on.


If the directive **.. contents::** will be used as follows in all documents::

    .. contents:: Table of contents
        :local:

Only the table of contents of specific of the document will be listed.

If the directive **.. contents::** will be used as follows in all documents::

    .. contents:: Table of contents

The table of contents of specific of the document and also the table of contents of embedded \
document will be listed.

The syntax in order to embedded only one external document is as follows

#. In external document example_including_external_document_level_1.rst, use the following \
   code-block

    .. code-block:: bash

        .. include:: example_including_external_document_level_2.rst

#. In external document example_including_external_document_level_2.rst, use the following \
   code-block

    .. code-block:: bash

        .. include:: example_including_external_document_level_3.rst

Adjusting headings
------------------

Please visit the chapter :ref:`reStructuredText without label <restructuredtext_without_label>`.

Example of embedding multiple external document
===============================================

.. hint::

    The content of the external document **Example Including external document level 1** begins now

.. include:: example_including_external_document_level_1.rst

.. hint::

    The content of the external document **Example Including external document level 1** begins now

Example of embedding one external document
==========================================

.. hint::

    The content of the external document begins now

.. include:: example_including_external_document.rst

.. hint::

    The content of the external document ends now
