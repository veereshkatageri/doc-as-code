# Readme doc-as-code toolchain

> Please read this document completely to get an idea on

    * What is DocAsCode Manual
    * Prerequisites

- This repository is the source of all doc as code documentation.
- This repository is a base or reference over which doc as code manual have been generated.
- The documentations are written down in reStructuredText (.rst) format and in markdown (.md).

Table of contents

- [DocAsCode Manual](#docascode-manual)
  * [Why should I use DocAsCode Manual](#why-should-i-use-docascode-manual)
- [How should I contribute to DocAsCode Manual](#how-should-i-contribute-to-docascode-manual)
    * [Prerequisites](#prerequisites)
    * [How shall I generate documentation from docAsCode source code](#how-shall-i-generate-documentation-from-docascode-source-code)
    * [How shall I edit documentation of docAsCode source code](#how-shall-i-edit-documentation-of-docascode-source-code)
    * [How shall I publish documentation from docAsCode source code](#how-shall-i-publish-documentation-from-docascode-source-code)
    * [How shall I become familiar with syntax of reStructuredText](#how-shall-i-become-familiar-with-syntax-of-reStructuredText)
    * [What should I do to setup in my repository to build my repository using CICD setup](#what-should-i-do-to-setup-in-my-repository-to-build-my-repository-using-cicd-setup)
- [The folder structure](#the-folder-structure)
    * [Root folder](#root-folder)
    * [source](#source)

## DocAsCode Manual

- The docAsCode manual contains the doc-as-code toolchain relevant documentation in a bundle
- Using python package sphinx, the doc as code will be generated to different target types like HTML and Confluence.

### Why should I use DocAsCode Manual
The following are documented thoroughly

- what is required in order to generate the documentation using reStructuredText and Sphinx using docAsCode toolchain
- how to become familiar with onboarding template
- how to become familiar with syntax provided reStructuredText

## How should I contribute to DocAsCode Manual

> If you have installed python package Conan already skip the following chapter

### Prerequisites

It is mandatory to have

* Cmder
* Powershell
* Access to SiANOMTech Github
    * [SiANOMTech/Technical-Documents](https://github.com/SiANOMTech/Technical-Documents.git)

### How shall I generate documentation from docAsCode source code

* Working steps

```
git clone -b develop https://github.com/SiANOMTech/Technical-Documents.git
cd Technical-Documents/user_guide
python -m venv ./venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
conan install . -if build
conan build . -bf build
```

* Open package/DocAsCodeManaulHtml/index.html

### How shall I edit documentation of docAsCode source code

* Go to chapter **How to use onboarding template**
* Get a hands-on experiance with onboarding template

### How shall I publish documentation from docAsCode source code

* Go to chapter **How to publish documents**
* Read all relevant chapters

### How shall I become familiar with syntax of reStructuredText

* Go to chapter **User guide reStructuredText**
* Read all relevant chapters

### What should I do to setup in my repository to build my repository using CICD setup

* Go to chapter CICD Setup

## The folder structure

The following is the recommended folder structure. The folder structure has been used under this
repository (Technical-Documents\user_guide)

```
Technical-Documents\user_guide
- conanfile.py
- conf.py
- IncludeLists.csv
- index.rst
- jenkinsfile
- Readme.md
- source
- style
- tools
- requirements.txt
```

### Root folder

| Folder/File                                   | Contents/Significance                                                    |
| ------------------------------------------    | ------------------------------------------------------------------------ |
| conanfile.py                                  | 1. to render the doc (in .rst) to target                                 |
|                                               | 2. target can be html and confluence                                     |
| conf.py                                       | 1. this file configures sphinx                                           |
|                                               | 2. transforms rst to html or to a specified build type                   |
|                                               | 3. current build type format is html                                     |
|                                               | 4. For more info visit conf.py                                           |
| IncludeLists.csv                              | csv file to decide which file/folder will be rendered to what            |
| index.rst                                     | 1. master document                                                       |
|                                               | 2. serves welcome page                                                   |
|                                               | 3. used to connect multiple files to a single hierarchy of documents     |
| Readme.md                                     | Readme.md for the beginners                                              |
| source                                        | The placeholder which contains the literature of methodology doc-as-code |
| style                                         | describes individual reStructuredText syntaxes                           |
| tools                                         | describes individual reStructuredText syntaxes                           |
| requirements.txt                              | containes all the required python packages to generate the documentation |

### source

The following is the recommended folder structure.

```
Technical-Documents\user_guide\source
- CHANGELOG.md
- cicd_setup.rst
- documents
- how-to_configure_conanfile.rst
- how-to_configure_doc_as_code_folder_structure.rst
- how-to_publish_documents.rst
- how-to_publish_documents_to_confluence.rst
- how-to_render_doc_as_code_to_html.rst
- how-to_render_doc_as_code_to_pdf.rst
- how-to_use_onboarding_template.rst
- images
- IncludeLists.csv
- known_issues_onboarding_template.rst
- miscellaneous
- miscellaneous.rst
- prerequisites.rst
- spelling_wordlist.txt
- user_guide
- user_guide.rst
```

| Folder/File                                       | Contents/Significance                                                |
| ------------------------------------------        | ---------------------------------------------------------------------|
| CHANGELOG.md                                      | specific template to document the changelog                          |
| cicd_setup.rst                                    | describes how to setup cicd to generate or to publish the documents  |
| documents                                         | place holder for documents                                           |
| images                                            | place holder for images                                              |
| how-to_configure_conanfile.rst                    | describes how to configure the doc-as-code form scratch              |
| how-to_configure_doc_as_code_folder_structure.rst | place holder for documents                                           |
| how-to_publish_documents.rst                      | describes how to publish or to render documents to any target        |
| how-to_publish_documents_to_confluence.rst        | describes how to publish documents to confluence                     |
| how-to_render_doc_as_code_to_html.rst             | describes how to render documents to html                            |
| how-to_render_doc_as_code_to_pdf.rst              | describes how to render documents to pdf                             |
| how-to_use_onboarding_template.rst                | describes how to get hands-on experiance with onboarding template    |
| images                                            | place holder for images                                              |
| IncludeLists.csv                                  | csv file to decide which file/folder will be rendered to what        |
| known_issues_onboarding_template.rst              | describes known issues and workaround                                |
| miscellaneous                                     | place holder for miscellaneous (nice to have features)               |
| miscellaneous.rst                                 | implements tree hierarchy of miscellaneous documents                 |
| prerequisites.rst                                 | describes prerequisites (requirements)                               |
| spelling_wordlist.txt                             | list of worlds to be ignored                                         |
| user_guide                                        | place holder for step by step guide                                  |
| user_guide.rst                                    | implements tree hierarchy of  r step by step guide                   |
