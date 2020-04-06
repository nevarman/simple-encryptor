# Simple Encryptor

A simple cli tool that encrypts and decrypts files with a password using AES encryption.

This tool can be used to encrypt files before uploading them to a cloud instance.

## Usage

- Add an alias to your bash file, in my case inside .zshrc file: _alias sencryptor='python3 PycharmProjects/simple-encrptor/sencryptor.py'_
- In your terminal emulator use sencryptor with parameters: 
```
-e  for encryption
-d  for decryption

after parameter specifiy an input folder or a file to encrypt of decrypt
after input folder specifiy an output folder(if left empty a temp folder will be used, such as /tmp)
```

Examples:
```
sencryptor -e /media/sda/GoogleExport/Photos /media/test/Photos 
```
will encrypt all files
```
sencryptor -d /media/sda/Photos/2013-10-06/IMG_20131006_211033.jpg.enc
```
will decrypt the photo into /tmp folder