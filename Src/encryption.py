from email.policy import strict
from PyPDF4 import PdfFileReader


def file_encrypted(file):
    with open(file,"rb") as pdffile:
        dfile = PdfFileReader(pdffile,strict=False)
        return dfile.isEncrypted


print(file_encrypted("C:/Users/Jarvis/Desktop/Homes/Target/Resume-JairoPerez.pdf"))

import pyAesCrypt as ac
from os import stat, remove

#textfile = r"C:\Users\Jarvis\Desktop\Homes\Target\2nd Shift Notes 1-28-22.txt"
textfile = r"C:/Users/Jarvis/Desktop/Homes/Target/Resume-JairoPerez.pdf"
sectextfile = r"C:\Users\Jarvis\Desktop\Homes\Target\crypt__"+"Resum-JairoPerez"+"_.txt"
newText = r"C:/Users/Jarvis/Desktop/Homes/Target/Resume-JairoPerez__decrypted__.txt"

buff = 64*2048

pwd ="archivo"

with open(textfile, "rb") as rf:
    print(rf)
    with open(sectextfile,"wb") as wfe:
        ac.encryptStream(rf,wfe,pwd,buff)


encFileSize = stat(sectextfile).st_size
print(encFileSize)
# decrypt
with open(sectextfile, "rb") as fIn:
    try:
        with open(newText, "wb") as fOut:
            # decrypt file stream
            ac.decryptStream(fIn, fOut, pwd, buff, encFileSize)
    except ValueError:
        # remove output file on error
        remove(newText)