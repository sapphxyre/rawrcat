# rawrcat v1.0
# 'pkcs1_oaep.py' -> cryptogtaphic function library -> v1.3
# rsa cryptography via the PKCS1_OAEP cipher method
# python version 3.13.5
# dependencies: 'rsa' 'pycrypto' 'pycryptodome'
# [!] required dependencies are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# object 'keyman' { (takes no parameters) -> null }
class keyman:

    # method 'scandir' - search directory for existing '.pem' files
    def scandir(dir):
        files = list(Path(dir).rglob("*.pem"))
        if len(files) == 0:
            return False
        return files

    # method 'newkey' - create new rsa key pair and '.pem' files
    def newkey(publicKeyTarget, privateKeyTarget, publicKeyIdentifier, privateKeyIdentifier):
        key_value = RSA.generate(2048)
        public_key_identifier = str(publicKeyIdentifier)
        private_key_identifier = str(privateKeyIdentifier)
        if publicKeyIdentifier == privateKeyIdentifier:
            if publicKeyTarget == privateKeyTarget:
                public_key_identifier = str("p" + publicKeyIdentifier)
                private_key_identifier = str("s" + privateKeyIdentifier)
                print("(!) key identifiers modified to resolve ambiguous filenames in target directory")
        public_key_path = os.path.join(publicKeyTarget, public_key_identifier + '.pem')
        private_key_path = os.path.join(privateKeyTarget, private_key_identifier + '.pem')
        if os.path.exists(public_key_path) or os.path.exists(private_key_path):
            onNext = input("(?) overwrite existing keyfile? (y/N) >>> ")
            if onNext.lower() == 'y':
                os.remove(public_key_path)
            else:
                print("(!) keyfile already exists. key creation aborted")
                return
        try:
            f = open(public_key_path, 'wb')
            f.write(key_value.publickey().exportKey('PEM'))
            f.close()
            f = open(private_key_path, 'wb')
            f.write(key_value.exportKey('PEM'))
            f.close()
        except:
            print("failed to create keys. check target file permissions.")
        finally:
            return
        
    # method 'importkey' - import rsa key pair from '.pem' file
    def importkey(publicKeyTarget, privateKeyTarget):
        if os.path.exists(publicKeyTarget) == False or os.path.exists(privateKeyTarget) == False:
            print("failed to import keys. specified keys could not be located in specified directory")
            return
        else:
            public_key_fileobj = open(publicKeyTarget, 'rb')
            private_key_fileobj = open(privateKeyTarget, 'rb')
            public_key_value = RSA.importKey(public_key_fileobj.read())
            private_key_value = RSA.importKey(private_key_fileobj.read())
            PUBLIC_KEY = public_key_value.publickey().exportKey('PEM')
            PRIVATE_KEY = private_key_value.export_key('PEM')
            return PUBLIC_KEY, PRIVATE_KEY

# object 'function' { (takes no parameters) -> null }
class function:
    
    # method 'encrypt' - encrypt plaintext using public key
    def encrypt(publicKey, plaintext):
        ptxt = str.encode(plaintext)
        rsa_public_key = RSA.importKey(publicKey)
        rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(ptxt)
        return encrypted_text
    
    # method 'encryptfile' - encrypt plaintext using public key and write to file
    def encryptfile(publicKey, plaintext, fileTarget):
        encrypted_text = function.encrypt(publicKey, plaintext)
        x = open(fileTarget, "wb")
        x.write(encrypted_text)
        x.close()
        return
    
    # method 'decrypt' - decrypt ciphertext using private key
    # [!] requires input paramater dataclass to be bytes
    def decrypt(privateKey, ciphertext):
        ctxt = ciphertext
        rsa_private_key = RSA.importKey(privateKey)
        rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
        decrypted_text = rsa_private_key.decrypt(ctxt)
        return decrypted_text
    
    # method 'decryptfile' - decrypt ciphertext using private key from existing file
    def decryptfile(privateKey, fileTarget):
        x = open(fileTarget, "rb")
        ciphertext = x.read()
        x.close()
        decrypted_rtext = function.decrypt(privateKey, ciphertext)
        decrypted_text = (str(decrypted_rtext)).replace('b\'','')
        return decrypted_text
