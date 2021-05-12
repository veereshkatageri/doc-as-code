.. _tabs:

Tabs
++++

This page is intended to show how to use tabs in doc as code.

.. contents:: Table of contents
    :local:

Reference
=========

Please visit the `sphinx-tabs <https://github.com/executablebooks/sphinx-tabs>`_

Types
=====

Basic Tabs
----------

Basic tabs can be coded as follows:

.. code-block:: rst

    .. tabs::

    .. tab:: Apples

        Apples are green, or sometimes red.

    .. tab:: Pears

        Pears are green.

    .. tab:: Oranges

        Oranges are orange.

.. only:: builder_html

    It yields to

    .. tabs::

       .. tab:: Apples

          Apples are green, or sometimes red.

       .. tab:: Pears

          Pears are green.

       .. tab:: Oranges

          Oranges are orange.

.. hint::

    Credits: `tabs.gif <https://github.com/executablebooks/sphinx-tabs/blob/master/images/tabs.gif>`_

.. only:: not builder_latex

    It can be visualized as follows

    .. image:: ../images/doc-as-code/tabs.gif
        :width: 640px
        :align: center
        :height: 336px

Grouped Tabs
------------

Tabs can be grouped, so that changing the current tab in one area changes the current tab in the \
another area. For example:

.. code-block:: rst

    .. tabs::

       .. group-tab:: Linux

          Linux tab content - tab set 1

       .. group-tab:: Mac OSX

          Mac OSX tab content - tab set 1

       .. group-tab:: Windows

          Windows tab content - tab set 1

    .. tabs::

       .. group-tab:: Linux

          Linux tab content - tab set 2

       .. group-tab:: Mac OSX

          Mac OSX tab content - tab set 2

       .. group-tab:: Windows

          Windows tab content - tab set 2

.. only:: builder_html

    It yields to

    .. tabs::

       .. group-tab:: Linux

          Linux tab content - tab set 1

       .. group-tab:: Mac OSX

          Mac OSX tab content - tab set 1

       .. group-tab:: Windows

          Windows tab content - tab set 1

    .. tabs::

       .. group-tab:: Linux

          Linux tab content - tab set 2

       .. group-tab:: Mac OSX

          Mac OSX tab content - tab set 2

       .. group-tab:: Windows

          Windows tab content - tab set 2

.. hint::

    Credits: `groupTabs.gif <https://github.com/executablebooks/sphinx-tabs/blob/master/images/groupTabs.gif>`_

.. only:: not builder_latex

    It can be visualized as follows

    .. image:: ../images/doc-as-code/groupTabs.gif
        :width: 640px
        :align: center
        :height: 291px

Code Tabs
---------

Grouped tabs containing code areas with syntax highlighting can be created as follows:

.. code-block:: rst

    .. tabs::

       .. code-tab:: c

             C Main Function

       .. code-tab:: c++

             C++ Main Function

       .. code-tab:: py

             Python Main Function

       .. code-tab:: java

             Java Main Function

       .. code-tab:: julia

             Julia Main Function

       .. code-tab:: fortran

             Fortran Main Function

       .. code-tab:: r R

             R Main Function

    .. tabs::

       .. code-tab:: c

             int main(const int argc, const char **argv) {
             return 0;
             }

       .. code-tab:: c++

             int main(const int argc, const char **argv) {
             return 0;
             }

       .. code-tab:: py

             def main():
                return

       .. code-tab:: java

             class Main {
                public static void main(String[] args) {
                }
             }

       .. code-tab:: julia

             function main()
             end

       .. code-tab:: fortran

             PROGRAM main
             END PROGRAM main

       .. code-tab:: r R

             main <- function() {
                return(0)
             }

.. only:: builder_html

    It yields to

    .. tabs::

       .. code-tab:: c

             C Main Function

       .. code-tab:: c++

             C++ Main Function

       .. code-tab:: py

             Python Main Function

       .. code-tab:: java

             Java Main Function

       .. code-tab:: julia

             Julia Main Function

       .. code-tab:: fortran

             Fortran Main Function

       .. code-tab:: r R

             R Main Function

    .. tabs::

       .. code-tab:: c

             int main(const int argc, const char **argv) {
             return 0;
             }

       .. code-tab:: c++

             int main(const int argc, const char **argv) {
             return 0;
             }

       .. code-tab:: py

             def main():
                return

       .. code-tab:: java

             class Main {
                public static void main(String[] args) {
                }
             }

       .. code-tab:: julia

             function main()
             end

       .. code-tab:: fortran

             PROGRAM main
             END PROGRAM main

       .. code-tab:: r R

             main <- function() {
                return(0)
             }

Code tabs also support custom lexers (added via sphinx `conf.py`).

By default, code tabs are labelled with the language name, though can be provided with custom \
labels like so:

.. code-block:: rst

    .. tabs::

       .. code-tab:: c I love C

            int main(const int argc, const char **argv) {
            return 0;
            }

       .. code-tab:: py I love Python more

            def main():
                return

.. only:: builder_html

    It yields to

    .. tabs::

       .. code-tab:: c I love C

            int main(const int argc, const char **argv) {
            return 0;
            }

       .. code-tab:: py I love Python more

            def main():
                return

.. hint::

    Credits: `codeTabs.gif <https://github.com/executablebooks/sphinx-tabs/blob/master/images/codeTabs.gif>`_

.. only:: not builder_latex

    It can be visualized as follows

    .. image:: ../images/doc-as-code/codeTabs.gif
        :width: 640px
        :align: center
        :height: 393px
