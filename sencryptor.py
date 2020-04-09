import hashlib
import os, getopt, tempfile, webbrowser, sys, getpass
import shutil
import aes
from pathlib import Path

def encrypt_files(key, path, out_path):
    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    shutil.copytree(path, out_path)
    for root, dirs, files in os.walk(out_path):
        for name in files:
            p = (os.path.join(root, name))
            print(p)
            aes.encrypt(key, p)
            os.remove(p)


def decrypt_files(key, path, out_path):
    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    shutil.copytree(path, out_path)
    for root, dirs, files in os.walk(out_path):
        for name in files:
            p = (os.path.join(root, name))
            print(p)
            aes.decrypt(key, p)
            os.remove(p)


def encrypt_file(key, file, out=None):
    if out is None:
        out = tempfile.gettempdir()
    else:
        if not os.path.isdir(out):
            os.makedirs(out)
    filename = os.path.basename(file)
    print(filename)
    aes.encrypt(key, file, os.path.join(out, filename))
    webbrowser.open(out)

def decrypt_file(key, file, out=None):
    if out is None:
        out = tempfile.gettempdir()
    else:
        if not os.path.isdir(out):
            os.makedirs(out)
    print('Output directory: %s' % out)
    filename = Path(file).stem
    path = os.path.join(out, filename)
    aes.decrypt(key, file, path)
    webbrowser.open(out)
    return path

def get_key(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

if __name__ == "__main__":
    # read commandline arguments, first
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    unixOptions = "hedo"
    gnuOptions = ["help", "encrypt", "decrypt", "outdir"]
    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    if len(values) > 2 or len(values) < 1:
        print("Too many or less arguments!")
        sys.exit(2)
    # get dirs
    inp = values[0]
    try:
        out = values[1]
        if "." in out:
            raise NotADirectoryError("Please provide a directory instead of a file name")
    except IndexError:
        print("Output directory not specified, a temp location will be used.")
        out = None

    if os.path.isdir(inp) and out == None:
        raise NotADirectoryError("Provided input is directory, please provide an output directory as well")

    password = getpass.getpass("Password:")
    key = get_key(password)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("Help!!")
        elif currentArgument in ("-e", "--encrypt"):
            print(("encrypting: %s") % (inp))
            if os.path.isdir(inp):
                encrypt_files(key, inp, out)
            else:  # file
                encrypt_file(key, inp, out)
        elif currentArgument in ("-d", "--decrypt"):
            print(("decrypting: %s") % (inp))
            if os.path.isdir(inp):
                decrypt_files(key, inp, out)
            else:
                decrypt_file(key, inp, out)