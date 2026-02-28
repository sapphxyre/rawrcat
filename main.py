# rawrcat v1.0
# 'main.py' -> primary runtime logic and initial execution call -> v1.2
# python version 3.13.5
# dependencies:
#  global -> 'os' 'rsa' 'pycrypto' 'pycryptodome' 'colorama' 'platform' 'pathlib'
#  local-packages -> 'iomgr' 'pkcs1_oaep'
#  self -> 'os' 'platform'
# [!] some local packages require dependencies that are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
import os, platform

# import local packages
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl
from lib.iomgr import shell as xcnslfunc

########  < INIT >  ########

# clear command line and display splash text
xcnslfunc.clear()
xcnsl.log('\n\ninitializing...', 3, "\n\n\n                       _,-'""`-._        \n  rawrcat v1.0    |`._,'(       |\\`-/|   \n                   `-.-' \\ )-`( , o o)   \n                        ^^^^^^^^^^^^^^   ")

# initialization script 
ostype = str(platform.system().lower())
xcnsl.log(str('set ostype = \'' + str(ostype) + '\''))

if cryptography.keyman.scandir(os.getcwd()) == False:
    xcnsl.log('no key files were found in current directory')



