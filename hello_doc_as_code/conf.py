#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Doc-as-Code-Documents documentation build configuration file, created by
# sphinx-quickstart on Mon Aug  6 09:09:54 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

"""This script is used to set the configuration file

- author: Veeresh Katageri
- status: alpha
- e-mail: veeersh.mcis@gmail.com
"""

import sys
import os
import csv
from distutils import util
import glob
import platform
import re
import sphinx

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# customized variables

# path plant uml
path_plantuml = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'Technical-Documents',
                                                             'onboarding_template', 'tools', 'plantuml.jar')
print('path_plantuml', path_plantuml)
plantuml = "java -jar " + path_plantuml

# spelling wordlists
spelling_word_list_filename = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),
                                                           'Technical-Documents', 'hello_doc_as_code',
                                                           'source', 'spelling_wordlist.txt')

# customized variables

DOCU_GENERATION_TYPE = os.environ.get('DOCU_GENERATION_TYPE')
print('DOCU_GENERATION_TYPE:', DOCU_GENERATION_TYPE)
if DOCU_GENERATION_TYPE is None:
    DOCU_GENERATION_TYPE = 'generate_html'

# customized methods

def find_exclude_patterns():
    """ This method is used to find the pattern to include and to exclude the documents. Basically
    it reads all IncludeLists.csv files from doc_source folder. In IncludeLists.csv files, required
    folders and reStructuredText files will be included with the options to either to include or to
    exclude it in e2e manual or while publishing to confluence.

    return values are exclude_lists and include_lists
    exclude_lists: will be used by exclude_patterns in order to exclude the selected source files
    during build process.
    include_patterns: will be used by confluence_publish_subset to publish required (multiple html)
    documents to confluence

    distutils: the method distutils.util.strtobool() has been used to use multiple options in
    IncludeLists.csv
    True values are 'y', 'yes', 't', 'true', 'on', and '1';
    false values are 'n', 'no', 'f', 'false', 'off', and '0'.
    Raises ValueError if 'val' is anything else.
    
    :rtype: tuple (exclude_lists, include_lists)
    """

    print('Find exclude patterns for DOCU_GENERATION_TYPE %s' % DOCU_GENERATION_TYPE)
    regex_file_pattern = os.getcwd() + '/**/IncludeLists.csv'

    # Collect all IncludeLists.csv recursively
    list_csv_include_lists = glob.glob(regex_file_pattern, recursive=True)

    #for csv_file in glob.glob(regex_file_pattern, recursive=True):
    #    list_csv_include_lists.append(csv_file)

    # patterns to include and to exclude
    exclude_lists = []
    include_lists = []

    # Define field names
    fieldnames = ['file_name', 'generate_html', 'publish_confluence', 'generate_pdf']

    for file_include_list in list_csv_include_lists:
        if os.path.exists(file_include_list):
            # get the parent folder of chosen IncludeLists.csv and the content inside parent folder
            file_path_csv = os.path.dirname(file_include_list)
            contents_dir = os.listdir(file_path_csv)
            content_csv = []

            # prepare unwanted list to exclude for the comparison
            list_unwanted = ['documents', 'images', 'IncludeLists.csv', 'conf.py', 'conanfile.py',
                             'style', 'tools', '.git', 'spelling_wordlist.txt', 'build']
            contents_dir = set(contents_dir).difference(list_unwanted)

            # Read csv file
            with open(file_include_list) as csv_file:
                csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter=';')

                if platform.system() == "Windows":
                    pattern_file_name = file_include_list.replace((os.getcwd() + "\\"), '')
                    pattern_file_name = pattern_file_name.replace('IncludeLists.csv', '')
                    if pattern_file_name.endswith('\\'):
                        pattern_file_name = pattern_file_name[:-1]
                    pattern_file_name = pattern_file_name.replace('\\', '/')
                else:
                    pattern_file_name = file_include_list.replace((os.getcwd()), '')
                    pattern_file_name = pattern_file_name.replace('IncludeLists.csv', '')
                    if pattern_file_name.startswith('/'):
                        pattern_file_name = pattern_file_name[1:]

                # Skip first line
                row = next(csv_reader)
                # Read columns 'publish_confluence', 'generate_html' or 'generate_pdf' based on DOCU_GENERATION_TYPE
                for row in csv_reader:
                    content_csv.append(row['file_name'])

                    if not bool(util.strtobool(row[DOCU_GENERATION_TYPE])):
                        # Exclude file or folder
                        if len(pattern_file_name) == 0:
                            exclude_lists.append(row['file_name'])
                        else:
                            if platform.system() == "Windows":
                                exclude_lists.append((pattern_file_name + '/' + row['file_name']))
                            else:
                                exclude_lists.append((pattern_file_name + row['file_name']))
                        # Exclude IncludeLists.csv file if it is folder and if this folder is set to
                        # False in parent directory
                        if not (row['file_name'].endswith('.rst') or row['file_name'].endswith('.md')):
                            excluded_file = os.path.join(
                                os.path.dirname(file_include_list),
                                row['file_name'],
                                'IncludeLists.csv')
                            print('excluded_file', excluded_file)
                            if excluded_file in list_csv_include_lists:
                                list_csv_include_lists.remove(excluded_file)
                    else:
                        # Append relevant file or folder to include_lists
                        # later it will be by confluence publish mechanism
                        if len(pattern_file_name) == 0:
                            include_lists.append(row['file_name'])
                        else:
                            if pattern_file_name.endswith('/'):
                                include_lists.append((pattern_file_name + row['file_name']))
                            else:
                                include_lists.append((pattern_file_name + '/' + row['file_name']))

            difference = set(contents_dir) - set(content_csv)
            # Report missing file to console
            if bool(difference) is True:
                print('These files %s are not included yet in %s' % (list(difference),
                                                                    file_include_list))
        else:
            print('No such file %s is found' % file_include_list)

    # remove postfile .rst from
    include_patterns = []
    for item in include_lists:
        print('item in include lists', item)

    # as source_suffix is set to .md and .rst, the include pattern should not contain the file extension.
    for item in include_lists:
        if item.endswith('.rst'):
            include_patterns.append(item.split('.rst')[0])
        elif item.endswith('.md'):
            include_patterns.append(item.split('.md')[0])

    for item in exclude_lists:
        print('excluded item is', item)
    for item in include_patterns:
        print('included item is', item)

    return exclude_lists, include_patterns

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
              'sphinx.ext.autosummary', 'sphinx.ext.extlinks',
              'sphinx.ext.viewcode', 'sphinxcontrib.confluencebuilder',
              'sphinxcontrib.imagesvg', 'sphinxcontrib.plantuml', 'sphinx.ext.graphviz',
              'sphinx_git', 'sphinx_tabs.tabs', 'sphinxcontrib.excel',
              'sphinxcontrib.excel_table', 'recommonmark', 'sphinx_markdown_tables',
              'sphinx_copybutton', 'crate.sphinx.csv']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['style/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
### Markdown parser

source_suffix = ['.rst']

#todo: support markdown in sphinx
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Demo Doc-As-Code'
copyright = '2021, Doc-as-Code'
author = 'katageri, Veeresh <veeresh.mcis@gmail.com>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

# Note: Do not the change the following version will be always set by conanfile.py
version = ('[Release %s]' % os.environ.get('version'))
# The full version, including alpha/beta/rc tags.
release = os.environ.get('version')

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
if DOCU_GENERATION_TYPE == 'spell_check':
    excluded_patterns, included_patterns = ['venv'], None
else:
    excluded_patterns, included_patterns = find_exclude_patterns()

exclude_patterns = []
if excluded_patterns is not None:
    exclude_patterns.extend(excluded_patterns)

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

print('included_patterns', included_patterns)

# -- Options for Confluence Output ----------------------------------------
"""
    confluence_server_user : confluence user name
    confluence_server_pass : confluence user pass
    confluence_publish : A boolean that decides whether or not to allow publishing
    confluence_space_name : Key of the space in Confluence to be used to publish generated
                            documents to.
    confluence_server_url : The URL for Confluence. The URL should be prefixed with
                            https:// or http:// (depending on the URL target). 
    confluence_parent_page : The root page found inside the configured space
    confluence_publish_subset : Provides the ability for a publisher to explicitly list a subset
                                of documents to be published to a Confluence instance.
    confluence_asset_override: Provides an override for asset publishing to allow a user publishing
                               to either force re-publishing assets or disable asset publishing.
    confluence_page_hierarchy : A boolean value to whether or not nest pages in a hierarchical
                                ordered.
"""

if DOCU_GENERATION_TYPE == 'publish_confluence':
    # if it is jenkins job then, Username and passoword will be substitued by Jenkins system user
    # credentials during switching mechanism
    # For local build, these values should be provided manually using set command.
    confluence_server_user = os.environ.get('CI_TECH_USER_CONFLUENCE')
    confluence_server_pass = os.environ.get('CI_TECH_PWD_CONFLUENCE')
    if confluence_server_user is not None and confluence_server_pass is not None:
        print("Credentials are passed correctly")
        try:
            print("Publish documentation to Confluence")
            # TODO: Default space name should be set by conanfile.py
            confluence_space_name = os.environ.get('CONFLUENCE_SPACE_NAME')
            # TODO: Default server_url should be set by conanfile.py
            confluence_server_url = os.environ.get('CONFLUENCE_SERVER_URL')
            # Default parent page is Doc-As-Code and it set by conanfile.py
            confluence_parent_page = os.environ.get('CONFLUENCE_PARENT_PAGE')
            confluence_publish_subset = included_patterns
            confluence_asset_override = True
            confluence_page_hierarchy  = True
            confluence_publish_dryrun = True
            confluence_publish = True
        except:
            print("Unable to publish the documents to confluence")
    else:
        print("Credentials are not passed correctly")

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
    #"rightsidebar": "false"
    #"relbarbgcolor": "black"
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['style/_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Sphinx-phpdoc'

html_js_files = [
    'js/custom.js'
]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    'figure_align': 'htbp',

    # Avoid printing with consistent empty pages
    'extraclassoptions': 'openany,oneside'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Doc-as-Code-Tools-Documents.tex', 'Doc-as-Code Documentation',
     'Generated by Veeresh Katageri', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = False

# Documents to append as an appendix to all manuals.
latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True


autodoc_member_order = 'groupwise'
todo_include_todos = True
extlinks = {'duref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'restructuredtext.html#%s', ''),
            'durole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'roles.html#%s', ''),
            'dudir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'directives.html#%s', '')}

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Doc-as-Code-Documents', 'Doc-as-Code-Documents Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Doc-as-Code-Documents', 'Doc-as-Code-Documents Documentation',
     author, 'Doc-as-Code-Documents', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# rst_epilog is a string of reStructuredText that will be included at the end of every source file that is read.
# This is a possible place to add substitutions that should be available in every file

rst_epilog = """.. |ProjectVersion| replace:: version {versionnum}""".format(versionnum = version)

# -- Extension interface -------------------------------------------------------

from sphinx import addnodes  # noqa

event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')


def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    from sphinx.util.docfields import GroupedField
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    fdesc = GroupedField('parameter', label='Parameters',
                         names=['param'], can_collapse=True)
    app.add_object_type('event', 'event', 'pair: %s; event', parse_event,
                        doc_field_types=[fdesc])