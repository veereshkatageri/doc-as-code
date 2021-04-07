.. _how-to_configure_doc_as_code_folder_structure:

How to configure doc-as-code folder structure
+++++++++++++++++++++++++++++++++++++++++++++

This page is intended to provide the instructions on how to configure the folder structure using \
doc-as-code template as reference in order to create new base for the documentation.

.. contents:: Table of contents
    :local:

Working steps
=============

Copying the contents
--------------------

#. Clone the doc-as-code template from here \
   `SiANOMTech/Technical-Documents <https://github.com/SiANOMTech/Technical-Documents.git>`_
#. Checkout the develop branch

Creating new doc-as-code base
_____________________________

#. If you want to create a new repository as a doc-as-code base, then simply copy the following \
   contents to the root location of the repository

   .. code-block:: bash

        onboarding_template/
        Readme.md

#. Rename existing rst files as per the requirement. The existing rst files are::

    template_doc_as_code.rst
    template_glossary_doc_as_code.rst

   For example, we cane rename::

    template_doc_as_code.rst to template_glossary-hello_world.rst
    template_glossary_doc_as_code.rst to template_hellow_world.rst
    template_readme.md to template_readme_hellow_world.md

#. Update IncludeLists.csv. The contents before modification are::

    #file_name;generate_html;publish_confluence;generate_pdf;
    index.rst;True;True;True;
    template_glossary_doc_as_code.rst;True;True;True;
    template_doc_as_code.rst;True;True;True;
    template_readme.md;True;True;True;

   After modification, the contents of IncludeLists.csv file will be::

    #file_name;generate_html;publish_confluence;generate_pdf;
    index.rst;True;True;True;
    template_hello_world.rst;True;True;True;
    template_glossary_hello_world.rst;True;True;True;
    template_readme_hellow_world.md;True;True;True;

#. Rename onboarding_template to any other name as per the requirement.

Creating a separate doc-as-code base in onboarding_template
___________________________________________________________

#. Create a new folder at the same location where onboarding_template is located.
#. Copy all the contents from onboarding_template to newly created folder.

Adjustments in conanfile.py and conf.py
---------------------------------------

Refer to the chapter :ref:`How to configure conanfile <how-to_configure_conanfile>` to make all \
necessary adjustments.

How to build the doc-as-code
----------------------------

#. Go to the folder (no matter existing doc-as-code template or new doc-as-code base) where \
   conanfile.py is located.
#. Perform the following steps::

    mkdir build
    cd build
    conan install ..
    conan build ..

#. Read :ref:`how-to_publish_documents` to know more on where generated documents will be located.
