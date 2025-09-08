# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Albania'
copyright = '2025, sfa'
author = 'sfa'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
]

pdf_documents = [('index', project, project, author),]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_with_keys': True,
}

html_logo = 'media/Flag_of_Albania.png'
html_title = "Albania"
html_favicon = "media/Flag_of_Albania.png"

html_show_sourcelink = False

latex_documents = [
    (
        'index',       # source start file
        'MyProject.tex', # target .tex file
        project,   # document title
        author,  # author
        'manual',       # document class ('manual' or 'howto')
    ),
]

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'\usepackage{graphicx}',
    'figure_align': 'H',
}