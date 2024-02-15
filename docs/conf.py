# TO 2024-02-15
project="Transient Grounwater Course IHE Delft"
author = "TN Olsthoorn"
copyright='2006-2024, TN Olsthoorn'
version='2024'
release='2024.0rc1'

import sys, os
#sys..path.append(os.path.abspath('sphinxext'))
#extensions=['extensions']
extensions=[]
source_suffix={
  '.rst': 'restructuredtext',
  '.txt': 'restructuredtext',
  '.md': 'markdown',
}
source_encoding='UTF-8'
source_parcers=['.md', 'recommonmark.parser.CommonMarkParser']
root_doc='index'
exclude_pattersn=[]
include_patterns=[]
numfig=True
numfig_secnum_dpeth=1


