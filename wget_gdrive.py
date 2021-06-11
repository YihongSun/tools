import sys, os, argparse
from subprocess import call
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--link', default=None, 
    help="Google Drive Link")
args = parser.parse_args(sys.argv[1:])

if args.link == None:
    print('Please enter the gdrive download link: \'python3 wget_drive.py --link=<gdrive download link>')

link_parts = args.link.split('/')

try:
    gcom_idx = link_parts.index('drive.google.com')
    assert gcom_idx > -1 and link_parts[gcom_idx+2] == 'd'
    FILEID = link_parts[gcom_idx+3]
except:
    print('Error: Invalid Link.')

savename = '{}'.format(datetime.now().strftime("%Y_%m_%d__%H_%M"))

bash_file = open('./tmp.sh', 'w')
bash_file.write("#!/bin/sh\n")
bash_file.write("wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={0}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p')&id={0}\" -O {1} && rm -rf /tmp/cookies.txt\n".format(FILEID, savename))
bash_file.close()

os.chmod('./tmp.sh', 0o744)
call('./tmp.sh')

os.remove('./tmp.sh')

print('Download Completed! File saved under \'{}\''.format(savename))
