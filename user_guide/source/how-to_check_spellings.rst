.. _how-to_check_spellings:

How to check spelling mistakes?
+++++++++++++++++++++++++++++++

This page is intended to guide you how to check spellings recursively while generating the \
documents.

.. contents:: Table of contents
    :local:

.. _spell_checks:

Working steps
=============

#. use conan commands as follows.

    .. code-block:: bash

        cd Technical-Documents/onboarding_template
        python -m venv ./venv
        .\venv\Scripts\activate.bat
        pip install -r requirements.txt
        conan install . -if build
        conan build . -bf build
        .\venv\Scripts\deactivate.bat

#. The above working steps generate the .spelling files under the directory \
   **build\\package\\Doc_as_Code_Tools-DocumentsSpelling\\**.

#. For example the existing spelling mistakes in this repository will be available under \
   **package\\Doc_as_Code_Tools-DocumentsSpelling\\source\CHANGELOG.spelling**.

#. The content of the above file will be as shown below

.. code-block:: bash

    source\CHANGELOG.md:41: (ä)  e.g. German umlaut alphabet ä, ö, ü, Ä, Ö, Ü and ß
    source\CHANGELOG.md:41: (ö)  e.g. German umlaut alphabet ä, ö, ü, Ä, Ö, Ü and ß
    source\CHANGELOG.md:41: (ü)  e.g. German umlaut alphabet ä, ö, ü, Ä, Ö, Ü and ß
    source\CHANGELOG.md:41: (ß)  e.g. German umlaut alphabet ä, ö, ü, Ä, Ö, Ü and ß

#. The same content will be published to terminal console output too.

How to ignore spell check on specific terms
===========================================

It is quite common that certain terms are not part of standard dictionary. For example, \
**Powerpoint**. In order to exclude such words from spell check, the following working steps must \
be performed.

Where to locate spelling_wordlist.txt
-------------------------------------

The **Technical-Documents/onboarding_template** is already equipped with spell check. The file \
**spelling_wordlist.txt** can be found the under the location \
**Technical-Documents/onboarding_template/source**.

How to add new word
-------------------

The actual contents of the file spelling_wordlist.txt are as follows

.. code-block:: bash

    reStructuredText
    Readme
    pdf
    subsubsections
    toolchain
    On-boarding
    subsubsections

If you want to include a new word to filter for example the word **Powerpoint**, then extend the \
list as follows

.. code-block:: bash

    reStructuredText
    Readme
    pdf
    subsubsections
    toolchain
    On-boarding
    subsubsections
    Powerpoint
