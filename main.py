import os
print("Script initialsiert")
print("es wird gearbeitet")
import re

dir = "export"

def fetch():
    fileName = "img"
    fileExtension = "html"
    loop = 0
    dir = "export"

    while True:
        myFile = "export/" + str(fileName) + str(loop) + "." + str(fileExtension)
        if (os.path.isfile(myFile)):
            with open(myFile, encoding="utf8", errors='ignore') as f:
                contents = f.read()
            with open(myFile, "w") as fu:
                fu.write('<link rel="stylesheet" type="text/css" href="iframe.css">' + contents)
        else:
            break
        loop = loop + 1

os.system("cp iframe.css "+dir+"/iframe.css")
fetch()
print("Done")

# scp export/* root@5.45.101.7:/root/docker/fiatools/fiapresentWeb/data/var/www/html/fia93/presenter/LF4/Raid/
