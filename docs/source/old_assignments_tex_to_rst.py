#! Python3

# Gegenerating documentation from the old Exam bundels 
# TO 2022-5-27

# Convert the bundels to rst Files using pandoc

import os
from collections import Counter


def get_nextLine(fin, counter):
    while True:
        s = fin.readline()
        if not s:
            print('Done, {} lines read, {} figures found'.
                  format(counter['lines'], counter['figures']))
        yield s
        counter.update(['lines'])

source   = '/Users/Theo/Entiteiten/IHE/ReadTheDocsSyllabus/docs/source/'
docs     = os.path.join(source, '../')
root     = os.path.join(docs, '../')
syllabus = os.path.join(root, 'SyllabusUptoDate/')
build    = os.path.join(docs, 'build/') # not needed here

for d in [source, docs, root, syllabus, build]:
    assert os.path.isdir(d), FileExistsError(d)

os.chdir(source)
os.getcwd()

basename_1 = 'old_assignments'

texfile_1  = os.path.join(syllabus, basename_1 + '.tex')
tmpfile_1  = os.path.join(source,   basename_1 + '.tmp')
rstfile_1  = os.path.join(source,   basename_1 + '.rst')

for fname in [texfile_1]:  #, texfile_2, texfile_3]:
    assert os.path.isfile(fname), FileNotFoundError(fname)

# pandoc command setup for converting tex to rst
options = ' '.join([
    '-s',
    '-f latex',
    '-t rst',
    '--verbose',
    '--wrap=none',
    '--default-image-extension=png',
    '-o',
    ])

# pandoc commands
pandoc_cmd_1 = ' '.join(['pandoc', options, tmpfile_1, texfile_1])

# executed them
os.system(pandoc_cmd_1)

counter = Counter()

# Add title of file as TOC top entry
with open(tmpfile_1, 'r') as fin:
    with open(rstfile_1, 'w') as fout:
        # Put title on top of .rst file
        fout.write('====================\n')
        fout.write('Previous Assignments\n')
        fout.write('====================\n')
        fout.write('\n')
        
        line = get_nextLine(fin, counter)
        
        for i in range(6):
            s = next(line)
        
        while True:
            s = next(line)
            if not s:
                break
            
            fout.write(s) 

# Remove all duplicate lavels
# These labels staart with_           
# Add title of file as TOC top entry 
#with open(tmpfile_2, 'r') as fin:
#    with open(rstfile_2, 'w') as fout:
#        # Put title on top of .rst file.
#        fout.write('======================================\n')
#        fout.write('Previous Assignmentsexams with answers\n')
#        fout.write('======================================\n')
#        fout.write('\n')
#        
#        line = get_nextLine(fin, counter)
#        
#        for i in range(6):
#            s = next(line)        
#        
#        while True:
#            s = next(line)
#            if not s:
#                break
#            
#            fout.write(s) 
            
# Add title of file as TOC top entry 
#with open(tmpfile_3, 'r') as fin:
#    with open(rstfile_3, 'w') as fout:
#        # Put title on top of .rst file.
#        fout.write('============================================================================\n')
#        fout.write('Usefule tecniques when using Python to solve (groundwater analysis) problems\n')
#        fout.write('============================================================================\n')
#        fout.write('\n')
#        
#        line = get_nextLine(fin, counter)
#        
#        for i in range(6):
#            s = next(line)        
#        
#        while True:
#            s = next(line)
#            if not s:
#                break
#            
#            fout.write(s) 

os.system(' '.join(['rm', tmpfile_1]))   # , tmpfile_2, tmpfile_3]
print('Done.')    
    
