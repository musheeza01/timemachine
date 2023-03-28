# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ligadata'
copyright = '2022, Musheeza'
author = 'Ligadata'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = [
   'sphinx_rtd_theme_ext_color_contrast',
       'sphinxcontrib.confluencebuilder',
  'linuxdoc.rstFlatTable',

]
confluence_publish = True
confluence_space_key = '~630ceba209bc6014ea8aac28'
confluence_ask_password = False
confluence_server_url = 'https://ligadata.atlassian.net/wiki/'
confluence_server_user = 'm.saeed@ligadata.com'
confluence_parent_page = 'Documentation'
confluence_server_pass = 'eEhhl9RNWXci3L7acVo31419'
confluence_page_hierarchy = True

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    'css/theme.css',
]

