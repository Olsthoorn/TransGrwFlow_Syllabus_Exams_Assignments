# TO 2024-02-15
import sys, os
#sys..path.append(os.path.abspath('sphinxext'))
#extensions=['extensions']

project = "Transient Grounwater Course IHE Delft"
author = "TN Olsthoorn"
copyright = '2006-2024, TN Olsthoorn'
version = '2024'
release = '2024.0rc1'


html_theme = 'sphinx_rtd_theme'

extensions=['myst_parser', 'nbsphinx']
source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'restructuredtext',
  '.md': 'markdown',
}
source_encoding = 'UTF-8'
source_parcers = []
root_doc = 'index'
exclude_pattersn = []
include_patterns = ['*.md', '*.rst', '*.txt', 'notebooks/*.ipynb']
numfig = True
numfig_secnum_dpeth = 1


