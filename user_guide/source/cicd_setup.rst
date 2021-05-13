.. _cicd_setup:

How to setup CICD
+++++++++++++++++

The scope of this document is to cover how to setup CICD infrastructure can be used to generate \
documents continuously.

.. contents:: Table of contents
    :local:

What should be avoided
======================

Github actions provide 2000 Minutes per Month on free account.

For more info visit `About billing for GitHub Actions <https://docs.github.com/en/github/setting-up-and-managing-billing-and-payments-on-github/about-billing-for-github-actions>`_

It is not recommended to generate the documents on every single commit and for every branches.

Please make sure that you make a strategy to generate the documents using one branch for \
example master branch only.


Working steps
=============

The onboarding_template is equipped with ready to use **.github\workflows*\main.yml** file.
This yml file can be taken as an example when you want to setup your own document generation \
mechanism using Github actions.

Original content
----------------

.. code-block:: bash

    # This is a basic workflow to help you get started with Actions

    name: CI

    # Controls when the action will run. 
    on:
      # Triggers the workflow on push or pull request events but only for the master branch
      push:
        branches: [ master ]
      pull_request:
        branches: [ master ]

      # Allows you to run this workflow manually from the Actions tab
      workflow_dispatch:

    # A workflow run is made up of one or more jobs that can run sequentially or in parallel
    jobs:
      # This workflow contains a single job called "build"
      build:
        # The type of runner that the job will run on
        runs-on: ubuntu-latest

        # Steps represent a sequence of tasks that will be executed as part of the job
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python 3.x
            uses: actions/setup-python@v2
            with:
              # Semantic version range syntax or exact version of a Python version
              python-version: '3.x'
              # Optional - x64 or x86 architecture, defaults to x64
              architecture: 'x64'
          - name: Install miktex
            shell: bash
            run: |
              sudo apt install -y texlive texlive-latex-extra
            # Render documentation to HTML format
          - name: Generate HTML/PDF
            shell: bash
            run: |
              ls -l ${{github.workspace}}
              python -m venv ./${{github.workspace}}/onboarding_template/venv
              source ./${{github.workspace}}/onboarding_template/venv/bin/activate
              pip install -r ${{github.workspace}}/onboarding_template/requirements.txt
              conan install ${{github.workspace}}/onboarding_template -if ${{github.workspace}}/onboarding_template/build -o generate_pdf=True
              conan build ${{github.workspace}}/onboarding_template -bf ${{github.workspace}}/onboarding_template/build

          - name: Check contents
            shell: bash
            run: |
              ls -l ${{github.workspace}}
              ls -l ${{github.workspace}}/onboarding_template
              ls -l ${{github.workspace}}/onboarding_template/build
              ls -l ${{github.workspace}}/onboarding_template/build/package/
              ls -l ${{github.workspace}}/onboarding_template/build/package/Doc-as-Code-Tools-DocumentsPDF

          # Upload zip (HTML)
          - name: Upload zip (HTML)
            uses: actions/upload-artifact@v1
            with:
              name: Doc-as-Code-Tools-DocumentsHtml.zip
              path: ${{github.workspace}}/onboarding_template/build/Doc-as-Code-Tools-DocumentsHtml.zip

          # Upload PDF
          - name: Upload PDF
            uses: actions/upload-artifact@v1
            with:
              name: Doc-as-Code-Tools-Documents.pdf
              path: ${{github.workspace}}/onboarding_template/build/Doc-as-Code-Tools-DocumentsPDF/Doc-as-Code-Tools-Documents.pdf


What to modify
--------------

For example consider your repository name is **hello_world**. The repository name \
**onboarding_template** must be replaced by **hello_world** in the above yml file.
