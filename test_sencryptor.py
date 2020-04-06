from unittest import TestCase
import sencryptor
import os
class Test(TestCase):

    def get_key(self):
        password = "test12345"
        return sencryptor.get_key(password)

    def test_encrypt_file(self):
        sencryptor.encrypt_file(self.get_key(), "Test/test.txt","out")
        existsPath = os.path.isdir("out")
        self.assertTrue(existsPath)
        existsFile = os.path.exists("out/test")
        self.assertTrue(existsFile)

    def test_decrypt_file(self):
        path = sencryptor.decrypt_file(self.get_key(), "out/test")
        print(path)
        self.assertTrue(self, os.path.exists(path))