.. _math_formulas:

Math formulas
+++++++++++++

This page is intended to show how to use math formulas in doc as code.

.. contents:: Table of contents
    :local:

Reference
=========

Please visit the `Math in Sphinx <https://www.sphinx-doc.org/en/1.0/ext/math.html>`_

Rendering math formulas
=======================

1. Syntax to use math formula as follows

.. code-block:: bash

    .. math::

    (a + b)^2 = a^2 + 2ab + b^2
    (a - b)^2 = a^2 - 2ab + b^2

It yields to

.. math::

   (a + b)^2 = a^2 + 2ab + b^2
   (a - b)^2 = a^2 - 2ab + b^2

cross-referencing equations
===========================

Example::

  .. math:: e^{i\pi} + 1 = 0
     :label: euler

  Euler's identity, equation :eq:`euler`, was elected one of the most
  beautiful mathematical formulas.

It yields to

.. math:: e^{i\pi} + 1 = 0
 :label: euler

Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.