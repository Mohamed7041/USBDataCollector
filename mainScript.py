import os
import win32api

config_file = open(".\\config.cfg", "r")
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

config = config_file.readlines()

dst = os.path.abspath(".\\") + config[0]


def convert(list):
    if len(list) == 1:
        return list[0]
    else:
        return tuple(i for i in list)


file_ext = config[1].split(';')[:-1]
print(file_ext)
file_to_extract = convert(file_ext)
print(file_to_extract)
for drive in drives:
    for root, dirs, files in os.walk(drive):
        for name in files:
            if name.endswith(file_to_extract):
                src = root + os.sep + name
                print(src)
                cmd = "copy " + "\"" + src + "\"" + " " + "\"" + dst + "\""
                print(cmd)
                os.system(cmd)

exit(0)
