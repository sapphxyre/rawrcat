# rawrcat v1.0
# 'main.py' -> primary runtime logic and initial execution call -> v1.6
# python version 3.13.5
# dependencies:
#  global -> 'os' 'rsa' 'pycrypto' 'pycryptodome' 'colorama' 'platform' 'pathlib' 'uuid'
#  local-packages -> 'iomgr' 'pkcs1_oaep'
#  self -> 'os' 'platform' 'uuid'
# [!] some local packages require dependencies that are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
import os, platform, uuid

# import local packages
import fsutil as filesystem
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl
from lib.iomgr import shell as xcnslfunc

########  < INIT >  ########

# clear command line and display splash text
xcnslfunc.clear()
xcnsl.log('\n\ninitializing...', 3, "\n\n\n                       _,-'""`-._        \n  rawrcat v1.0    |`._,'(       |\\`-/|   \n                   `-.-' \\ )-`( , o o)   \n                        ^^^^^^^^^^^^^^   ")

# initialization script 
ostype = str(platform.system().lower())
xcnsl.log(str('ostype = \'' + str(ostype) + '\''))

filesystem.init.keychain()