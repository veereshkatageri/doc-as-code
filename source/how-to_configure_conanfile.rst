.. _how-to_configure_conanfile:

How to configure conanfile
++++++++++++++++++++++++++

In this chapter, the essential elements will be listed in order to adopt the project \
specific configuration. This chapter will be explained with existing onboarding template.

.. contents:: Table of contents
    :local:

Changing standard attribute
===========================

The conanfile.py is supposed to be used with the initialization of certain default attributes. \
Mainly

#. name
#. version
#. description

These variables are mapped to customized variables to make sure that conan standard attributes \
remain untouched.

.. hint::

    If it is required to initialize any other attribute apart from the attributes mentioned above, \
    then to have a glance on all attributes please visit the page \
    `Attributes <https://docs.conan.io/en/latest/reference/conanfile/attributes.html?highlight=name>`_

The following code snippet shows the declaration of the attributes.

.. code-block:: python

    # standard attributes
    var_name = "Doc_as_Code_Tools_Documents"
    var_version = "0.0.1"
    var_description = "User manual"

For a while, please assume that name of new doc as code repository as **hello_world**. After the \
modification, the contents will be shown below in following code-block

.. code-block:: python

    var_name = "Hello_World"
    var_version = "0.0.1"
    var_description = "User guide doc as code Hello_World"

Changing document generation type
=================================

Currently, three types of documentation will be provided by doc as code toolchain and \
those are

#. generate_html : doc as code source will be rendered to html and this type is default. It is always \
   enabled. This type will be taken into account for both local build and CICD build by default.
#. publish_confluence: doc as code source will be published to Confluence. This type is not default.
   This type will be taken into account for both local build and CICD build by default with minimum \
   adjustments.
   
   for local build please visit :ref:`How to publish documents to Confluence <how-to_publish_documents_to_confluence>`

#. Publish_pdf: doc as code source will be rendered to pdf. This type is not default. This type \
   can be taken into account only with local build.

   for local build please visit \
   :ref:`How to render doc as code to pdf (Publish to PDF) <how-to_render_doc_as_code_to_pdf>`

.. _changing_customized_attribute:

Changing customized attribute
=============================

.. attention::

    If it is required to generate only html from doc as code source, keep \
    :ref:`publish_related_settings` and :ref:`changing_tex_file_in_confpy` untouched.

    If it is required to generate pdf from doc as code source, keep \
    :ref:`publish_related_settings` untouched. And please read this section first and then \
    :ref:`changing_tex_file_in_confpy`

    If it is required to publish documents to confluence then keep \
    :ref:`changing_tex_file_in_confpy` untouched.

Now again we assume that name of new doc as code repository as **hello_world**. And **hello_world** \
contains configuration file, conanfile and doc as code source as same as onboarding template. 

The following code-block shows how all customized variables have been declared.

.. code-block:: python

    # customized attribute
    # adjust var_parent_dir_config_file accordingly if it is not a single folder
    var_parent_dir_config_file = 'onboarding_template'
    var_folder_html = "Doc_as_Code_Tools-DocumentsHtml"
    var_folder_spelling = "Doc_as_Code_Tools-DocumentsSpelling"
    var_folder_confluence = "Doc_as_Code_Tools-DocumentsConfluence"
    var_folder_pdf = "Doc_as_Code_Tools-DocumentsPDF"
    var_tex_file = "Doc_as_Code_Tools-Documents.tex"

where,

#. var_parent_dir_config_file defines the parent directory of configuration file (conf.py)
#. var_folder_html defines the name of the folder under which doc as code source will be rendered \
   to html
#. var_folder_confluence defines the name of the folder under which equivalent doctrees of doc as \
   source will be generated
#. var_folder_pdf defines the name of the folder under which doc as code source will be rendered \
   to pdf
#. var_tex_file defines the name of the tex file will be prepared by LaTeX

if you observe the contents of onboarding_template closely, the configuration file is located \
under the folder **onboarding_template**.

After the modification, the contents will be shown below in following code-block

.. code-block:: python

    # customized attribute
    # adjust var_parent_dir_config_file accordingly if it is not a single folder
    var_parent_dir_config_file = 'hello_world'
    var_folder_html = "HelloWorldHtml"
    var_folder_confluence = "HelloWorldConfluence"
    var_folder_pdf = "HelloWorldPDF"
    var_tex_file = "HelloWorld.tex"

.. _publish_related_settings:

Confluence publish-related settings
-----------------------------------

.. attention::

    This chapter is under progress.

Customized attribute PDF render type
------------------------------------

.. _changing_tex_file_in_confpy:

changing tex file in conf.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The configuration file (conf.py) defines the name of the tex file to be generated. The name of the \
tex file as of now is constant variable.

.. note::

    In future, it can be adjusted by conanfile.py. But now if it required to changed, please \
    follow instructions under this subchapter

The following code-block highlights where and how tex file will be defined in configuration file.

.. code-block:: python

    # Grouping the document tree into LaTeX files. List of tuples
    # (source start file, target name, title,
    #  author, documentclass [howto, manual, or own class]).
    latex_documents = [
        (master_doc, 'Doc_as_Code_Tools-Documents.tex', 'Doc-as-Code Documentation',
         'Generated by Veeresh Katageri', 'manual'),
    ]

The tex can be changed if it is required. Considering **hello_world** as an example, the code-block \
after the modification can be visualized as follows

.. code-block:: python

    # Grouping the document tree into LaTeX files. List of tuples
    # (source start file, target name, title,
    #  author, documentclass [howto, manual, or own class]).
    latex_documents = [
        (master_doc, 'Hello_World.tex', 'Hello_World Documentation',
        'Generated by Hello_World', 'manual'),
    ]

changing conanfile.py
^^^^^^^^^^^^^^^^^^^^^

Please visit :ref:`Changing customized attribute <changing_customized_attribute>` and observe how \
the customized variable **var_tex_file** has been modified with an example.

Related chapters
================

.. note::

    If all the steps have been performed as per the requirement, then next step would be to build \
    doc as code source in order to generate the documents to required target type. The following \
    related chapter helps you to navigate to working steps directly.

#. build target html, visit :ref:`Working steps - render to html <rendering_html>`
#. build target confluence, visit :ref:`Working steps - publish to confluence <how-to_publish_documents_to_confluence>`
#. build target pdf, visit :ref:`Working steps - render to pdf <rendering_pdf>`
