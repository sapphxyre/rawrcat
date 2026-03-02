# rawrcat v1.0
# 'fsutil.py' -> file system management utility -> v1.0
# application resource file control management
# python version 3.13.5
# dependencies: 'os'
# [!] undefined exception handling rules

# import dependencies
import os, uuid

# import local packages
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl

# object 'init' { (takes no parameters) -> null }
class init:

    # method 'keychain' - attempt to locate *.pem keyfiles
    def keychain():
        if cryptography.keyman.scandir(os.getcwd()) == False:
            xcnsl.log('no keys were found in the current directory or its subdirectories\n \\..  ' + str(os.getcwd()))
            keypath = xcnsl.update('set key file target directory or press <enter> to create a new rsa key pair')
            if keypath == True:
                xcnsl.log('', 5, 'create new keys:')
                publickey_path = xcnsl.input(' set public key target or press <enter> to use the current directory\n')
                privatekey_path = xcnsl.input(' set private key target or press <enter> to use the current directory\n')
                cryptography.keyman.newkey(publickey_path, privatekey_path, uuid.uuid4().hex, uuid.uuid4().hex)
            else:
                if os.path.exists(keypath):
                    if cryptography.keyman.scandir(keypath) == False:
                        pass