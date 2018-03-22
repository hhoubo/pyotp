import base64, datetime, hashlib, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import pyotp

class PasswordGenerator():
    def __init__(self, sharedSecret):
        self.totp = pyotp.TOTP(sharedSecret, digits=10, interval=30, digest=hashlib.sha512)

    def get(self):
        return self.totp.now()



if __name__ == '__main__':
    sharedSecret = 'hhoubo@gmail.comHDECHALLENGE003'
    base32SharedSecret = 'NBUG65LCN5AGO3LBNFWC4Y3PNVEEIRKDJBAUYTCFJZDUKMBQGM======'
    generater = PasswordGenerator(base32SharedSecret)
    password = generater.get()
    print(password)
