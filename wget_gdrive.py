import sys, os
from subprocess import call

try:
    link = sys.argv[1]
    FILENAME = sys.argv[2]
    print('Link: {}\nFile Name: {}'.format(link, FILENAME))
except:
    print('Please enter link and desired file name as a command link argument.')

link_parts = link.split('/')

try:
    gcom_idx = link_parts.index('drive.google.com')
    assert gcom_idx > -1 and link_parts[gcom_idx+2] == 'd' and link_parts[gcom_idx+4] == 'view?usp=sharing'
    FILEID = link_parts[gcom_idx+3]
except:
    print('Error: Invalid Link.')

bash_file = open('./tmp.sh', 'w')
bash_file.write("#!/bin/sh\n")
bash_file.write("wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={0}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p')&id={0}\" -O {1} && rm -rf /tmp/cookies.txt\n".format(FILEID, FILENAME))
bash_file.close()

os.chmod('./tmp.sh', 0o744)
call('./tmp.sh')

os.remove('./tmp.sh')
