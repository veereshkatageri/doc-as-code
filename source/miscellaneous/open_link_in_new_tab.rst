.. _open_link_in_new_tab:

Open external links in a new tab/window
+++++++++++++++++++++++++++++++++++++++

This page covers the implementation behind opening a link in new tab or window.

.. contents:: Table of contents
    :local:

Reference
=========

The article from Stackoverflow \
`Open a link in a new window in reStructuredText <https://stackoverflow.com/questions/11716781/open-a-link-in-a-new-window-in-restructuredtext>`_ \
has been used a reference here.

Required changes
================

#. Create a new folder under **_static** called **js**.
#. Create a new file under this folder and name it as **custom.js**
#. Copy paste the following code-block to the file **custom.js**
   
   .. code-block:: js

       $(document).ready(function () {
        $('a[href^="http://"], a[href^="https://"]').not('a[class*=internal]').attr('target', '_blank');
     });

   Basically this approach avoid modifying the existing theme.

#. Now newly created theme can be added to configuration file (conf.py). Under the options of html \
   output file, the following lines must be added.

   .. code-block:: js

        html_js_files = [
            'js/custom.js'
        ]

Known issues
============

The behaviour of opening an external links is not consistent in all browsers. The following table \
lists the actual behaviour of frequently used browsers while opening an external link.

.. list-table:: Behaviour of frequently used browsers
   :widths: auto
   :header-rows: 1

   * - Browser
     - Behaviour
   * - chrome
     - new tab
   * - Firefox
     - new tab
   * - Internet Explorer
     - new window
   * - Microsoft edge
     - new tab
