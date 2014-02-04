# coding: utf-8
import sys
import os

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.insert(0, project_root)

import fbads
import sphinx_rtd_theme

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'
project = u'fbads ' + fbads.__version__
copyright = u'2014, Renato Pedigoni'
version = fbads.__version__
release = fbads.__version__

exclude_patterns = ['_build']

pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'fbadsdoc'


latex_elements = {
}

latex_documents = [
    ('index', 'fbads.tex', u'fbads Documentation', u'Renato Pedigoni', 'manual'),
]

man_pages = [
    ('index', 'fbads', u'fbads Documentation',
     [u'Renato Pedigoni'], 1)
]

texinfo_documents = [
    ('index', 'fbads', u'fbads Documentation', u'Renato Pedigoni', 'fbads', 'One line description of project.', 'Miscellaneous'),
]
