.. _paragraph_level_markup:

Paragraph-level markup
++++++++++++++++++++++

This page is intended to show how **Paragraph-level markup** can be used to documentation using \
reStructuredText syntax.

.. contents:: Table of contents
    :local:

.. caution::

    Multiple references have been considered to create this draft. The nomenclature of directives \
    slightly varies among the references used. An attempt has been made in this document to \
    mention the rest syntaxes accurately. In case of any misleading information, please contact \
    Katageri, Veeresh mailto:veeresh.mcis@gmail.com.

.. note::

    Paragraph-level markup [#paragraph-level-markup]_ have been mentioned with the other name as \
    Admonitions [#Admonitions]_

These directives create short paragraphs and can be used inside information units as well as \
normal text.

All directive types are "attention", "caution", "danger", "error", "hint", "important", "tip", \
"admonition"

note
====

This directive will be used to notify very important information.

Example::

    .. note::

        Use installation manual provided by Doc_as_Code to generate documentation and to experiment with doc-as-code \
        methodology.

The above example results in

.. note::

    Use manual provided by Doc_as_Code to generate documentation and to experiment with doc-as-code \
    methodology.


warning
=======

This directive will be used to notify the precaution.

Example::

    .. warning::

        High voltage. Keep away.

The above example results in

.. warning::

    High voltage. Keep away.

seealso
=======

Many sections include a list of references to module documentation or external documents. These \
lists are created using the :rst:dir:`seealso` directive.

Example::

    .. seealso::

        Visit `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to know how python documentation generator works.

The above example results in

.. seealso::

    Visit `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to know how python documentation generator works.

Footnote
========

.. rubric:: Footnotes

.. [#Admonitions] Please visit `Admonitions Documentation <https://www.sphinx-doc.org/en/1.5/rest.html?highlight=admonitions#directives>`_.
.. [#paragraph-level-markup] Please visit `Paragraph-level Markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#paragraph-level-markup>`_.

