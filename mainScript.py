import os
import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
dst = os.path.abspath(".\\")

dst + "\\"

for drive in drives:
    for root, dirs, files in os.walk(drive):
        for name in files:
            if name.endswith((".kkk", ".mmm")):
                src = root + os.sep + name
                print(src)
                os.system("copy " + "\"" + src + "\"" + " " + "\"" + dst + "\"")
