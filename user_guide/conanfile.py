from conans import ConanFile, python_requires

import os
import sys
import shutil
import subprocess
import platform
from packaging import version

docu_generation_type = os.environ.get('DOCU_GENERATION_TYPE')
if docu_generation_type is None:
    docu_generation_type = 'generate_html'

# standard attributes
var_name = "Doc_as_Code_Tools_Documents"
var_version = "0.0.2"
var_description = "Doc-as-Code User manual"

# customized attribute
# adjust var_parent_dir_config_file accordingly if it is not a single folder
var_parent_dir_config_file = 'Tools-Documents'
var_folder_html = "Doc_as_Code_Tools-DocumentsHtml"
var_folder_spelling = "Doc_as_Code_Tools-DocumentsSpelling"
var_folder_confluence = "Doc_as_Code_Tools-DocumentsConfluence"
var_folder_pdf = "Doc_as_Code_Tools-DocumentsPDF"
var_tex_file = "Doc_as_Code_Tools-Documents.tex"

"""
# TODO: The following part can be ignored
Read all the publish-related settings
1. CONFLUENCE_SPACE_NAME is the confluence space name.
2. CONFLUENCE_SERVER_URL is the confluence server url. 
3. CONFLUENCE_PARENT_PAGE is the confluence parent page.
"""

os.environ["CONFLUENCE_SPACE_NAME"] = ''
os.environ["CONFLUENCE_SERVER_URL"] = ''
os.environ["CONFLUENCE_PARENT_PAGE"] = ''

class ConanRecipe(ConanFile):
    name            = var_name
    version         = var_version
    generators      = "txt"
    description     = var_description
    settings        = "os", "arch"
    scm             = { "type": "git", "url": "auto", "revision": "auto" }
    no_copy_source  = True
    options = {"publish_confluence": [True, False],
               "generate_pdf": [True, False]}
    default_options = {
        "publish_confluence": False,
        "generate_pdf" : False}

    # Set version in configuration file conf.py
    os.environ["version"] = version

    def build_requirements(self):
        print('self.options.generate_pdf:', self.options.generate_pdf)

        command = subprocess.check_output(['sphinx-build', '--version']).decode("utf8")
        if not (version.parse(command.strip()) == version.parse("sphinx-build 2.4.4") or
                version.parse(command.strip()) > version.parse("sphinx-build 2.4.4")):
            self.output.error("Sphinx Requirements are not satisfied")
            exit(1)

    def requirements(self):
        pass

    def build(self):
        # self.source_folder and self.build_folder are different in conan build method
        # but there are same in conan create method

        input_folder = None
        configuration_file = os.path.join(self.source_folder, var_parent_dir_config_file, 'conf.py')

        output_folder = os.path.join(self.build_folder, 'package', var_folder_html)
        os.makedirs(output_folder, exist_ok=True)

        # Adjust the parent folder of config file path for both conan build and conan create method
        if os.path.exists(configuration_file):
            input_folder = os.path.join(self.source_folder, var_parent_dir_config_file)
        else:
            input_folder = self.source_folder

        # -- target build html ----------------------------------------
        print("Begin generating html")
        try:
            os.environ["DOCU_GENERATION_TYPE"] = 'generate_html'
            command = subprocess.run(['sphinx-build', '-b', 'html', input_folder, output_folder],
                                     check=True)

            # make archieve
            shutil.make_archive(var_folder_html, 'zip', output_folder)
        except subprocess.CalledProcessError as err:
            print(err.output)

        print("End generating html")

        # -- target build spelling ----------------------------------------
        print("Begin spelling check")
        output_folder = os.path.join(self.build_folder, 'package', var_folder_spelling)
        os.makedirs(output_folder, exist_ok=True)

        try:
            os.environ["DOCU_GENERATION_TYPE"] = 'spell_check'
            command = subprocess.run(['sphinx-build', '-b', 'spelling', input_folder, output_folder],
                                     check=True)
            output_folder = os.path.join(self.build_folder, 'package', var_folder_spelling)
            os.makedirs(output_folder, exist_ok=True)
            # make archieve
            shutil.make_archive(var_folder_spelling, 'zip', output_folder)
        except subprocess.CalledProcessError as err:
            print(err.output)
        print("End spelling check")

        # -- target build confluence ----------------------------------
        if (self.options.publish_confluence):
            print("Begin publishing to confluence")
            os.environ["DOCU_GENERATION_TYPE"] = 'publish_confluence'
            output_folder = os.path.join(self.build_folder, 'package', var_folder_confluence)
            os.makedirs(output_folder, exist_ok=True)
            try:
                command = subprocess.run(['sphinx-build', '-b', 'confluence', input_folder,
                                            output_folder], check=True)
                # make archieve
                shutil.make_archive(var_folder_confluence, 'zip', output_folder)
            except subprocess.CalledProcessError as err:
                print(err.output)
            print("End publishing to confluence")

        # -- target build pdf ----------------------------------------
        if (self.options.generate_pdf):
            print("Begin generating pdf")
            os.environ["DOCU_GENERATION_TYPE"] = 'generate_pdf'
            output_folder = os.path.join(self.build_folder, 'package', var_folder_pdf)
            os.makedirs(output_folder, exist_ok=True)

            print("Log: folders have been created")

            try:
                print("Log: Run sphinx-build -b latex")
                # Build to target latex first
                command = subprocess.run(['sphinx-build', '-b', 'latex', input_folder, output_folder],
                                        check=True)

                print("Log: find tex file")
                # Identify the tex file
                tex_file = os.path.join(output_folder, var_tex_file)
                print("Log: file exists")

                if os.path.exists(tex_file):
                    # Get current directory
                    current_dir = os.getcwd()
                    # Change directory where tex file is located
                    parent_dir_texfile = os.path.dirname(tex_file)
                    os.chdir(parent_dir_texfile)

                    cmd_generate_pdf = ["pdflatex", tex_file]

                    """
                    It is known issue that the Miktex console command pdflatex will not generate
                    the index in PDF file. So it is required to run the same command twice
                    """
                    command = subprocess.check_output(cmd_generate_pdf).decode("utf8")
                    command = subprocess.check_output(cmd_generate_pdf).decode("utf8")

                    # Change directory
                    os.chdir(current_dir)
                    shutil.make_archive(var_folder_pdf, 'zip', output_folder)
                else:
                    print("Unable to locate the tex file %s" % tex_file)
                print("End generating pdf")

            except:
                output = sys.exc_info()[0]
                print(sys.exc_info())
                print(output)
