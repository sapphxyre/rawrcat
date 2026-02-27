# rawrcat v1.0
# 'main.py' -> primary runtime logic and initial execution call -> v1.0
# python version 3.13.5
# dependencies:
#  global -> 'os' 'rsa' 'pycrypto' 'pycryptodome' 'colorama' 'platform'
#  local-packages -> 'iomgr' 'pkcs1_oaep'
#  self -> 'os'
# [!] some local packages require dependencies that are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
import os

# import local packages
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl
from lib.iomgr import shell as xcnslfunc

########  < INIT >  ########

def main():
    xcnslfunc.clear()
    xcnsl.log('', 3, "\n                       _,-'""`-._        \n  rawrcat v1.0    |`._,'(       |\\`-/|   \n                   `-.-' \\ )-`( , o o)   \n                        ^^^^^^^^^^^^^^   \n")
    xcnsl.log('initializing...')


main()