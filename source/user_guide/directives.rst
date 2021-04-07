.. _directives:

Directives
++++++++++

This page is intended to document all **Directives** supported by reStructuredText syntax.

.. contents:: Table of contents
    :local:

A directive is a generic block of explicit markup. Besides roles, it is one of the extension \
mechanisms of reST, and Sphinx makes heavy use of it.

Docutils supports the following directives:

* Admonitions: :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` and the generic
  :dudir:`admonition <admonitions>`.  (Most themes style only "note" and
  "warning" specially.)

* Images:

  - :dudir:`image` (see also :ref:`Images <images>`  below)
  - :dudir:`figure` (an image with caption and optional legend)

* Additional body elements:

  - :dudir:`contents <table-of-contents>` (a local, i.e. for the current file
    only, table of contents)
  - :dudir:`container` (a container with a custom class, useful to generate an
    outer ``<div>`` in HTML)
  - :dudir:`rubric` (a heading without relation to the document sectioning)
  - :dudir:`topic`, :dudir:`sidebar` (special highlighted body elements)
  - :dudir:`parsed-literal` (literal block that supports inline markup)
  - :dudir:`epigraph` (a block quote with optional attribution line)
  - :dudir:`highlights`, :dudir:`pull-quote` (block quotes with their own
    class attribute)
  - :dudir:`compound <compound-paragraph>` (a compound paragraph)

* Special tables:

  - :dudir:`table` (a table with title)
  - :dudir:`csv-table` (a table generated from comma-separated values)
  - :dudir:`list-table` (a table generated from a list of lists)

* Special directives:

  - :dudir:`raw <raw-data-pass-through>` (include raw target-format markup)
  - :dudir:`include` (include reStructuredText from another file)
    -- in Sphinx, when given an absolute include file path, this directive takes
    it as relative to the source directory
  - :dudir:`class` (assign a class attribute to the next element) [1]_

* HTML specifics:

  - :dudir:`meta` (generation of HTML ``<meta>`` tags)
  - :dudir:`title <metadata-document-title>` (override document title)

* Influencing markup:

  - :dudir:`default-role` (set a new default role)
  - :dudir:`role` (create a new role)

  Since these are only per-file, better use Sphinx's facilities for setting the
  :confval:`default_role`.

Do *not* use the directives :dudir:`sectnum`, :dudir:`header` and
:dudir:`footer`.

Directives added by Sphinx are described in \
`sphinxmarkup <https://www.sphinx-doc.org/en/1.5/markup/index.html#sphinxmarkup>`_.

Basically, a directive consists of a name, arguments, options and content. (Keep
this terminology in mind, it is used in the next chapter describing custom
directives.)  Looking at this example, ::

   .. function:: foo(x)
                 foo(y, z)
      :module: some.module.name

      Return a line of text input from the user.

``function`` is the directive name.  It is given two arguments here, the
remainder of the first line and the second line, as well as one option
``module`` (as you can see, options are given in the lines immediately following
the arguments and indicated by the colons).  Options must be indented to the
same level as the directive content.

The directive content follows after a blank line and is indented relative to the
directive start.

.. rubric:: Footnotes

.. [1] When the default domain contains a :rst:dir:`class` directive, this
       directive will be shadowed.  Therefore, Sphinx re-exports it as
       :rst:dir:`rst-class`.
