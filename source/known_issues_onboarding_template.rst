.. _known_issues_onboarding_template:

Known issues onboarding template
++++++++++++++++++++++++++++++++

This page is intended to document the known issues of document publish mechanism to confluence \
using doc-as-code toolchain.

.. contents:: Table of contents
    :local:

WARNING: height value for image is unsupported in confluence
============================================================

Definition
----------

.. code-block:: bash

    ..\Technical-Documents\source\how-to_use_onboarding_template.rst:: WARNING: height value for image is unsupported in confluence

Workaround
----------

- if you are using the images with captions, such warning message will be generated.
- It can be either ignored or image directive without caption can be used

WARNING: unknown code language: rest
====================================

Definition
----------

.. code-block:: bash

    ..\Technical-Documents\source\prerequisites.rst:: WARNING: unknown code language: rest

Workaround
----------

- possible cause is the code-block **rest** would have been used as shown below

.. code-block:: bash

    .. code-block:: rest

- Use code-block **bash** instead as shown below

.. code-block:: bash

    .. code-block:: bash

